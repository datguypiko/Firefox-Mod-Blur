#!/usr/bin/env python3
import inquirer
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

def all_css_under_dir(dir):
    return [entry for entry in os.listdir(dir) if '.css' in entry]

class Config:
    def __init__(self, conf_path):
        self.conf_path = conf_path
        self.config = json.loads('{}')

        if not path.exists(conf_path):
            return

        with open(conf_path) as f:
            lines = f.readlines()
        json_str = ''.join(lines[1:])
        self.config = json.loads(json_str)

    def __getitem__(self, key):
        return self.config[key]
    def __setitem__(self, key, val):
        self.config[key] = val
    def __delitem__(self, key):
        del self.config[key]
    def __contains__(self, key):
        return key in self.config

    def write(self):
        with open(self.conf_path, 'w') as f:
            f.write('// This file is maintained by Firefox Mod Blur Installer. ')
            f.write('You should not modified it by yourself!\n')
        with open(self.conf_path, 'a') as f:
            json.dump(self.config, f)

class Menu:
    def __init__(self, base_dir, profile_dir):
        self.base_dir = base_dir
        self.profile_dir = profile_dir
        self.chrome_dir = path.join(self.profile_dir, 'chrome')
        self.conf_path = path.join(self.chrome_dir, CONF_NAME)
        self.config = Config(self.conf_path)

        self.single_choice_categories = [
            'Auto hide Mods',
            'Compact extensions menu',
            'Min-max-close control buttons',
        ]

    def _single_choice_validation(self, _, selection):
        if len(selection) <= 1:
            return True
        raise inquirer.errors.ValidationError('', reason='You can only choose 1 of them!')

    def _install_mod(self, category_dir, category, mod):
        mod_dir = path.join(category_dir, mod)
        all_css = all_css_under_dir(mod_dir)
        readme_path = path.join(mod_dir, 'README.md')
        extra_path = path.join(mod_dir, '.extra')

        # install all .css files
        for name in all_css:
            shutil.copy(path.join(mod_dir, name), self.chrome_dir)
        # install extra files
        extra_files = []
        if path.exists(extra_path):
            with open(extra_path) as f:
                extra_files = [line.rstrip() for line in f]
        for rel_file_path in extra_files:
            extra_file_path = path.join(mod_dir, rel_file_path)
            name = rel_file_path.split('/')[-1]

            if path.isdir(extra_file_path):
                shutil.copytree(extra_file_path, path.join(self.chrome_dir, name))
            else:
                shutil.copy(extra_file_path, self.chrome_dir)

        color_print(f"[+] '{mod}' was successfully installed!", GREEN)

        # show README
        if path.exists(readme_path):
            color_print(f"Notes of '{mod}':", YELLOW)
            with open(readme_path) as f:
                color_print(f.read().rstrip(), YELLOW)

        self.config[category][mod] = all_css + extra_files

    def _uninstall_mod(self, category_dir, category, mod):
        mod_dir = path.join(category_dir, mod)
        readme_path = path.join(mod_dir, 'README.md')

        for rel_path in self.config[category][mod]:
            file_name = rel_path.split('/')[-1]
            file_path = path.join(self.chrome_dir, file_name)

            if path.isdir(file_path):
                shutil.rmtree(file_path)
            else:
                os.remove(file_path)

        color_print(f"[-] '{mod}' was successfully uninstalled!", GREEN)

        # show README if this mod requires manual operation, e.g., Centered bookmarks bar items
        if self.config[category][mod] == [] and path.exists(readme_path):
            color_print(f"Notes of '{mod}':", YELLOW)
            with open(readme_path) as f:
                color_print(f.read().rstrip(), YELLOW)

        del self.config[category][mod]

    def _handle_selection(self, category_dir, category, choices, single_choice=False):
        readme_path = path.join(category_dir, 'README.md')
        if path.exists(readme_path) and category_dir.split('/')[-1] != 'EXTRA THEMES':
            with open(readme_path) as f:
                color_print(f.read(), YELLOW)

        default = None
        if category in self.config:
            default = list(self.config[category].keys())
        else:
            self.config[category] = {}

        validate = self._single_choice_validation if single_choice else True 

        sel = inquirer.checkbox('[Space]: toggle a selection [Enter]: submit selections',
            choices=choices, default=default, validate=validate, carousel=True)

        to_uninstall = [mod for mod in self.config[category].keys() if mod not in sel]
        to_install = [mod for mod in sel if mod not in self.config[category].keys()]

        for mod in to_uninstall:
            self._uninstall_mod(category_dir, category, mod)
        for mod in to_install:
            self._install_mod(category_dir, category, mod)
        print()

        if len(self.config[category]) == 0:
            del self.config[category]
        self.config.write()

    def main(self):
        print('Firefox Mod Blur Installer starts...')
        print()

        if path.exists(self.conf_path):
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
        if path.exists(self.chrome_dir):
            ts = int(time.time())
            chrome_backup_path = path.join(self.profile_dir, f'chrome.{ts}.bak')

            os.rename(self.chrome_dir, chrome_backup_path)
            color_print(f"'{self.chrome_dir}' already exists, and it was renamed to '{chrome_backup_path}'", YELLOW)

        os.mkdir(self.chrome_dir)

        # copy essential files
        shutil.copy(path.join(self.base_dir, 'userChrome.css'), self.chrome_dir)
        shutil.copy(path.join(self.base_dir, 'userContent.css'), self.chrome_dir)
        shutil.copytree(path.join(self.base_dir, 'image'), path.join(self.chrome_dir, 'image'))

        color_print(f"Successfully installed to '{self.chrome_dir}'!", GREEN)
        print()

        # create a config file to maintain installed mods & themes
        self.config.write()

        res = inquirer.confirm('Do you want to install any extra mod?', default=True)
        if res:
            self.mods()
        res = inquirer.confirm('Do you want to install any extra theme?', default=True)
        if res:
            self.themes()

        color_print('Remember to set `toolkit.legacyUserProfileCustomizations.stylesheets` to `True` in `about:config`!', YELLOW)

    def mods(self):
        mod_base_dir = path.join(self.base_dir, 'EXTRA MODS')
        categories = [entry for entry in os.listdir(mod_base_dir) if path.isdir(path.join(mod_base_dir, entry))]
        categories.append('Quit')

        while True:
            category = inquirer.list_input('Select Extra Mods', choices=categories, carousel=True)

            if category == 'Quit':
                return
             
            category_dir = path.join(mod_base_dir, category)
            mods = sorted([dir[0][len(category_dir) + 1:] for dir in os.walk(category_dir)])
            mods = mods[1:]  # ignore category directory

            self._handle_selection(category_dir, category, mods, category in self.single_choice_categories)

    def themes(self):
        theme_base_dir = path.join(self.base_dir, 'EXTRA THEMES')
        excluded_dirs = ['wallpaper']
        themes = sorted([
            dir[0][len(theme_base_dir) + 1:]
            for dir in os.walk(theme_base_dir)
            if dir[1] == [] and dir[0].split('/')[-1] not in excluded_dirs
        ])

        self._handle_selection(theme_base_dir, 'theme', themes, True)

    def update(self):
        # TODO
        pass

    def uninstall(self):
        confirm_to_uninstall = inquirer.confirm('Are you sure you want to uninstalled Firefox Mod Blur?', default=False)
        if not confirm_to_uninstall:
            return
        shutil.rmtree(self.chrome_dir)
        color_print(f"'{self.chrome_dir}' was successfully removed!", GREEN)
        color_print("You have to manually rename 'chrome.xxx.bak/' (if exists) to 'chrome/' for recovering your previous configuration.", YELLOW)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <Firefox profile directory>')
        exit()

    script_dir = path.dirname(path.realpath(__file__))
    menu = Menu(script_dir, sys.argv[1])
    menu.main()
