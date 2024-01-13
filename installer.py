#!/usr/bin/env python3
import filecmp
import inquirer
from inquirer.errors import ValidationError
import json
import os
from os import path
import shutil
import sys
import time

CONF_NAME = '.firefox-mod-blur.jsonc'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'

def color_print(msg, color=''):
    print(f'{color}{msg}\033[39m')

def copy_file_or_dir(src_path, dst_dir):
    name = path.basename(src_path)
    if path.isdir(src_path):
        shutil.copytree(src_path, path.join(dst_dir, name))
    else:
        shutil.copy(src_path, dst_dir)

def remove_file_or_dir(p):
    if path.isdir(p):
        shutil.rmtree(p)
    else:
        os.remove(p)

def turn_into_backup(file_path):
    ts = int(time.time())
    backup_path = f'{file_path}.{ts}.bak'
    os.rename(file_path, backup_path)
    return backup_path

class Config:
    def __init__(self, conf_path):
        self.conf_path = conf_path

        if not path.exists(conf_path):
            self.config = json.loads('{}')
            return

        with open(conf_path) as f:
            f.readline()  # first line is a comment
            self.config = json.load(f)

    def __getitem__(self, key):
        return self.config[key]
    def __setitem__(self, key, val):
        self.config[key] = val
    def __delitem__(self, key):
        del self.config[key]
    def __contains__(self, key):
        return key in self.config

    def keys(self):
        return self.config.keys()

    def write(self):
        with open(self.conf_path, 'w') as f:
            f.write('// This file is maintained by Firefox Mod Blur Installer. ')
            f.write('You should not modified it by yourself!\n')
        with open(self.conf_path, 'a') as f:
            json.dump(self.config, f)

class Menu:
    def __init__(self, base_dir, profile_dir):
        self._base_dir = base_dir
        self._profile_dir = profile_dir
        self._chrome_dir = path.join(self._profile_dir, 'chrome')
        self._conf_path = path.join(self._chrome_dir, CONF_NAME)
        self._config = Config(self._conf_path)

        self._single_choice_categories = [
            'Auto hide Mods',
            'Compact extensions menu',
            'Min-max-close control buttons',
        ]

    def _single_choice_validation(self, _, selection):
        if len(selection) <= 1:
            return True
        raise ValidationError('', reason='You can only choose 1 of them!')

    def _get_files_to_be_installed(self, dir):
        all_css = [entry for entry in os.listdir(dir) if '.css' in entry]

        extra_files = []
        extra_path = path.join(dir, '.extra')
        if path.exists(extra_path):
            with open(extra_path) as f:
                extra_files = [line.rstrip() for line in f]

        return all_css + extra_files

    def _install_files(self, mod_dir, files):
        for rel_path in files:
            # Contents listed in .extra are relative paths of extra files or directories with respect to `mod_dir`.
            # A path prefixed with '-' indicates that it will not get updated, so users can put their content.
            # For example, this is useful for wallpaper/.
            if rel_path[0] == '-':
                rel_path = rel_path[1:]
            copy_file_or_dir(path.join(mod_dir, rel_path), self._chrome_dir)

    def _compare_and_update(self, mod_dir, old_files, new_files):
        to_add = [p for p in new_files if p not in old_files]
        to_remove = [p for p in old_files if p not in new_files]
        to_check = [(p, path.basename(p)) for p in new_files if p in old_files]  # (src_rel_path, dst_rel_path)

        for rel_path in to_add:
            if rel_path[0] == '-':
                rel_path = rel_path[1:]
            file_path = path.join(mod_dir, rel_path)
            copy_file_or_dir(file_path, self._chrome_dir)

        for rel_path in to_remove:
            preserve = False
            if rel_path[0] == '-':
                rel_path = rel_path[1:]
                preserve = True

            file_name = path.basename(rel_path)
            file_path = path.join(self._chrome_dir, file_name)

            if preserve:
                backup_path = turn_into_backup(file_path)
                color_print(f"From now on, '{file_path}' will get updated, so the original '{file_name}' was backuped as '{backup_path}'.", YELLOW)
                return

            remove_file_or_dir(file_path)

        has_modified = False

        while len(to_check) > 0:
            src_rel_path, dst_rel_path = to_check.pop()
            if src_rel_path[0] == '-':
                continue

            src_file_path = path.join(mod_dir, src_rel_path)
            dst_file_path = path.join(self._chrome_dir, dst_rel_path)

            if path.isdir(src_file_path):
                dcmp = filecmp.dircmp(src_file_path, dst_file_path)

                for file_name in dcmp.right_only:
                    file_path = path.join(dst_file_path, file_name)
                    remove_file_or_dir(file_path)
                for file_name in dcmp.left_only:
                    file_path = path.join(src_file_path, file_name)
                    copy_file_or_dir(file_path, dst_file_path)
                for file_name in dcmp.common:
                    new_src_rel_path = path.join(src_rel_path, file_name)
                    new_dst_rel_path = path.join(dst_rel_path, file_name)
                    to_check.append((new_src_rel_path, new_dst_rel_path))

                if dcmp.right_only != [] or dcmp.left_only != []:
                    has_modified = True
            elif not filecmp.cmp(src_file_path, dst_file_path):
                shutil.copy(src_file_path, dst_file_path)
                has_modified = True

        return to_add != [] or to_remove != [] or has_modified

    def _handle_selection(self, category_dir, category, choices, single_choice=False):
        readme_path = path.join(category_dir, 'README.md')
        if path.exists(readme_path) and path.basename(category_dir) != 'EXTRA THEMES':
            with open(readme_path) as f:
                color_print(f.read(), YELLOW)

        default = None
        if category in self._config:
            default = list(self._config[category].keys())
        else:
            self._config[category] = {}

        validate = self._single_choice_validation if single_choice else True 

        sel = inquirer.checkbox('[Space]: toggle a selection [Enter]: submit selections',
            choices=choices, default=default, validate=validate, carousel=True)

        to_uninstall = [mod for mod in self._config[category].keys() if mod not in sel]
        to_install = [mod for mod in sel if mod not in self._config[category].keys()]

        for mod in to_uninstall:
            mod_dir = path.join(category_dir, mod)
            readme_path = path.join(mod_dir, 'README.md')

            for rel_path in self._config[category][mod]:
                preserve = False
                if rel_path[0] == '-':
                    rel_path = rel_path[1:]
                    preserve = True
                file_path = path.join(self._chrome_dir, path.basename(rel_path))
                if preserve:
                    backup_path = turn_into_backup(file_path)
                    color_print(f"'{file_path}' was backuped as '{backup_path}'", YELLOW)
                    continue
                remove_file_or_dir(file_path)
            color_print(f"[-] '{mod}' was successfully uninstalled!", GREEN)

            # show README if this mod requires manual operation, e.g., Centered bookmarks bar items
            if self._config[category][mod] == [] and path.exists(readme_path):
                color_print(f"Notes of '{mod}':", YELLOW)
                with open(readme_path) as f:
                    color_print(f.read().rstrip(), YELLOW)

            del self._config[category][mod]

        for mod in to_install:
            mod_dir = path.join(category_dir, mod)
            readme_path = path.join(mod_dir, 'README.md')

            files = self._get_files_to_be_installed(mod_dir)
            self._install_files(mod_dir, files)
            color_print(f"[+] '{mod}' was successfully installed!", GREEN)

            # show README
            if path.exists(readme_path):
                color_print(f"Notes of '{mod}':", YELLOW)
                with open(readme_path) as f:
                    color_print(f.read().rstrip(), YELLOW)

            self._config[category][mod] = files

        print()

        if len(self._config[category]) == 0:
            del self._config[category]
        self._config.write()

    def main(self):
        print('Firefox Mod Blur Installer starts...')
        print()

        if path.exists(self._conf_path):
            choices = ['Manage Mods', 'Manage Themes', 'Update', 'Uninstall', 'Quit']
        else:
            choices = ['Install', 'Quit']

        keep = True
        while keep:
            sel = inquirer.list_input('What do you want to do?', choices=choices, carousel=True)

            if sel == 'Install':
                self.install()
                keep = False
            elif sel == 'Manage Mods':
                self.mods()
            elif sel == 'Manage Themes':
                self.themes()
            elif sel == 'Update':
                self.update()
            elif sel == 'Uninstall':
                self.uninstall()
                keep = False
            else:
                keep = False

    def install(self):
        # create chrome/ in profile directory
        if path.exists(self._chrome_dir):
            backup_path = turn_into_backup(self._chrome_dir)
            color_print(f"'{self._chrome_dir}' already exists, so it was renamed to '{backup_path}'", YELLOW)

        os.mkdir(self._chrome_dir)

        # copy essential files
        files = self._get_files_to_be_installed(self._base_dir)
        self._install_files(self._base_dir, files)
        self._config['essential'] = files
        self._config.write()
        color_print(f"Successfully installed to '{self._chrome_dir}'!", GREEN)
        print()

        confirm_to_install = inquirer.confirm('Do you want to install any extra mod?', default=True)
        if confirm_to_install:
            self.mods()
        confirm_to_install = inquirer.confirm('Do you want to install any extra theme?', default=True)
        if confirm_to_install:
            self.themes()

        color_print('Remember to set `toolkit.legacyUserProfileCustomizations.stylesheets` to `True` in `about:config`!', YELLOW)

    def mods(self):
        extra_mod_dir = path.join(self._base_dir, 'EXTRA MODS')
        categories = next(os.walk(extra_mod_dir))[1]
        categories.append('Quit')

        while True:
            category = inquirer.list_input('Select Extra Mods', choices=categories, carousel=True)

            if category == 'Quit':
                return
             
            category_dir = path.join(extra_mod_dir, category)
            mods = sorted([dir[0][len(category_dir) + 1:] for dir in os.walk(category_dir)])
            mods = mods[1:]  # ignore category directory

            self._handle_selection(category_dir, category, mods, category in self._single_choice_categories)

    def themes(self):
        extra_theme_dir = path.join(self._base_dir, 'EXTRA THEMES')
        excluded_dirs = ['wallpaper']
        themes = sorted([
            dir[0][len(extra_theme_dir) + 1:]
            for dir in os.walk(extra_theme_dir)
            if dir[1] == [] and path.basename(dir[0]) not in excluded_dirs
        ])

        self._handle_selection(extra_theme_dir, 'theme', themes, True)

    def update(self):
        has_updated = False

        # update essential files
        old_files = self._config['essential']
        new_files = self._get_files_to_be_installed(self._base_dir)
        updated = self._compare_and_update(self._base_dir, old_files, new_files)
        if updated:
            has_updated = True
            color_print('[^] essential files were successfully updated!', GREEN)
        else:
            print('[=] there is no update for essential files.')

        # update mods/themes
        categories = list(self._config.keys())  # prevent modifying the dictionary during iteration
        for category in categories:
            if category == 'essential':
                continue

            mods = list(self._config[category].keys())
            old_files_of_each_mod = list(self._config[category].values())

            for mod, old_files in zip(mods, old_files_of_each_mod):
                category_dir = 'EXTRA THEMES' if category == 'theme' \
                    else path.join(self._base_dir, 'EXTRA MODS', category)
                mod_dir = path.join(category_dir, mod)
                new_files = self._get_files_to_be_installed(mod_dir)
                updated = self._compare_and_update(mod_dir, old_files, new_files)
                if updated:
                    has_updated = True
                    color_print(f'[^] {mod} was successfully updated!', GREEN)
                else:
                    print(f"[=] there is no update for '{mod}'.")

        print()
        if not has_updated:
            color_print('Note: you have to pull the repository by yourself!', YELLOW)
        print()

    def uninstall(self):
        color_print("The directory 'chrome/' will be removed, including your own files.", YELLOW)
        confirm_to_uninstall = inquirer.confirm('Are you sure you want to uninstalled Firefox Mod Blur?', default=False)
        if not confirm_to_uninstall:
            return
        shutil.rmtree(self._chrome_dir)
        color_print(f"'{self._chrome_dir}' was successfully removed!", GREEN)
        color_print("You have to manually rename 'chrome.xxx.bak/' (if exists) to 'chrome/' for recovering your previous configuration.", YELLOW)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <Firefox profile directory>')
        exit()

    script_dir = path.dirname(path.realpath(__file__))
    menu = Menu(script_dir, sys.argv[1])
    menu.main()
