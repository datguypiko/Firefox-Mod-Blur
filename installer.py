#!/usr/bin/env python3
import configparser
import inquirer
import os
from os import path
import shutil
import sys
import time

CONF_NAME = '.firefox-mod-blur.conf'
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
        self.config = configparser.ConfigParser()
        self.config.optionxform = str
        self.config.read(conf_path)

    def get_config(self):
        return self.config

    def write(self):
        with open(self.conf_path, 'w') as f:
            f.write('; This file is maintained by Firefox Mod Blur Installer. ')
            f.write('You should not modified it by yourself!\n')
        with open(self.conf_path, 'a') as f:
            self.config.write(f)

class Menu:
    def __init__(self, base_dir, profile_dir):
        self.base_dir = base_dir
        self.profile_dir = profile_dir
        self.chrome_dir = path.join(self.profile_dir, 'chrome')
        self.conf_path = path.join(self.chrome_dir, CONF_NAME)
        self.config = Config(self.conf_path)

        self.single_choice_mods = [
            'Auto hide Mods',
            'Compact extensions menu',
            'Min-max-close control buttons',
        ]

    def _single_choice_validation(self, _, selection):
        if len(selection) <= 1:
            return True
        raise inquirer.errors.ValidationError('', reason='You can only choose 1 of them!')

    def _handle_selection(self, section, choices, single_choice, mod_dir):
        readme_path = path.join(mod_dir, 'README.md')
        if path.exists(readme_path) and mod_dir.split('/')[-1] != 'EXTRA THEMES':
            with open(readme_path) as f:
                color_print(f.read(), YELLOW)

        default = None
        config = self.config.get_config()
        if section in config:
            default = list(config[section].keys())
        else:
            config[section] = {}

        validate = self._single_choice_validation if single_choice else True 

        sel = inquirer.checkbox('[Space]: toggle a selection [Enter]: submit selections',
            choices=choices, default=default, validate=validate, carousel=True)

        to_uninstall = [mod for mod in config[section] if mod not in sel]
        to_install = [mod for mod in sel if mod not in config[section]]

        for mod in to_uninstall:
            sub_mod_dir = path.join(mod_dir, mod)
            all_css = all_css_under_dir(sub_mod_dir)
            readme_path = path.join(sub_mod_dir, 'README.md')
            extra_path = path.join(sub_mod_dir, '.extra')

            # uninstall all .css files
            for name in all_css:
                os.remove(path.join(self.chrome_dir, name))
            # uninstall extra files
            if path.exists(extra_path):
                with open(extra_path) as f:
                    for line in f:
                        name = line.rstrip().split('/')[-1]
                        extra_file_path = path.join(self.chrome_dir, name)
                        if path.isdir(extra_file_path):
                            shutil.rmtree(extra_file_path)
                        else:
                            os.remove(extra_file_path)

            color_print(f"[-] '{mod}' was successfully uninstalled!", GREEN)

            # show README if this mod requires manual operation, e.g., Centered bookmarks bar items
            if all_css == [] and not path.exists(extra_path) and path.exists(readme_path):
                color_print(f"Notes of '{mod}':", YELLOW)
                with open(readme_path) as f:
                    color_print(f.read().rstrip(), YELLOW)

            del config[section][mod]

        for mod in to_install:
            sub_mod_dir = path.join(mod_dir, mod)
            all_css = all_css_under_dir(sub_mod_dir)
            readme_path = path.join(sub_mod_dir, 'README.md')
            extra_path = path.join(sub_mod_dir, '.extra')

            # install all .css files
            for name in all_css:
                shutil.copy(path.join(sub_mod_dir, name), self.chrome_dir)
            # install extra files
            if path.exists(extra_path):
                with open(extra_path) as f:
                    for line in f:
                        name = line.rstrip().split('/')[-1]
                        extra_file_path = path.join(sub_mod_dir, line.rstrip())

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

            config[section][mod] = 'y'

        print()

        if len(config[section]) == 0:
            del config[section]
        self.config.write()

    def main(self):
        print('Firefox Mod Blur Installer starts...')
        print()

        if path.exists(self.conf_path):
            choices = ['Manage Mods', 'Manage Themes', 'Update', 'Uninstall', 'Quit']
        else:
            choices = ['Install', 'Quit']

        sel = inquirer.list_input('What do you want to do?', choices=choices, carousel=True)

        if sel == 'Install':
            self.install()
        elif sel == 'Manage Mods':
            self.mods()
        elif sel == 'Manage Themes':
            self.themes()
        elif sel == 'Update':
            self.update()
        elif sel == 'Uninstall':
            self.uninstall()

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
        mods = [entry for entry in os.listdir(mod_base_dir) if path.isdir(path.join(mod_base_dir, entry))]
        mods.append('Quit')

        while True:
            mod = inquirer.list_input('Select Extra Mods', choices=mods, carousel=True)

            if mod == 'Quit':
                return
             
            mod_dir = path.join(mod_base_dir, mod)
            sub_mods = sorted([dir[0][len(mod_dir) + 1:] for dir in os.walk(mod_dir)])
            sub_mods = sub_mods[1:]  # remove mod directory

            self._handle_selection(mod, sub_mods, mod in self.single_choice_mods, mod_dir)

    def themes(self):
        theme_base_dir = path.join(self.base_dir, 'EXTRA THEMES')
        excluded_dirs = ['wallpaper']
        themes = sorted([
            dir[0][len(theme_base_dir) + 1:]
            for dir in os.walk(theme_base_dir)
            if dir[1] == [] and dir[0].split('/')[-1] not in excluded_dirs
        ])

        self._handle_selection('theme', themes, True, theme_base_dir)

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
