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

def single_choice_validation(_, selection):
    if len(selection) <= 1:
        return True
    raise inquirer.errors.ValidationError('', reason='You can only choose 1 style!')

def find_css_under_dir(dir):
    for entry in os.listdir(dir):
        if '.css' in entry:
            return entry
    return None

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
            sub_mods = [dir[0][len(mod_dir) + 1:] for dir in os.walk(mod_dir)]
            sub_mods = sub_mods[1:]  # remove mod directory

            default = None
            config = self.config.get_config()
            if mod in config:
                default = list(config[mod].keys())
            else:
                config[mod] = {}

            validate = True
            # Only one style can be selected for these mods
            if mod in ['Auto hide Mods', 'Compact extensions menu', 'Min-max-close control buttons']:
                validate = single_choice_validation
                color_print('Select only 1 style', YELLOW)

            sel = inquirer.checkbox('[Space]: toggle a selection [Enter]: submit selections',
                choices=sub_mods, default=default, validate=validate, carousel=True)

            mods_to_install = [sub_mod for sub_mod in sel if sub_mod not in config[mod]]
            mods_to_uninstall = [sub_mod for sub_mod in config[mod] if sub_mod not in sel]

            for sub_mod in mods_to_install:
                sub_mod_dir = path.join(mod_dir, sub_mod)
                css_name = find_css_under_dir(sub_mod_dir)
                readme_path = path.join(sub_mod_dir, 'README.md')

                if css_name is not None:
                    shutil.copy(path.join(sub_mod_dir, css_name), self.chrome_dir)
                    color_print(f"[+] '{sub_mod}' was successfully installed!", GREEN)

                if path.exists(readme_path):
                    color_print(f"Notes of '{sub_mod}':", YELLOW)
                    with open(readme_path) as f:
                        color_print(f.read(), YELLOW)

                config[mod][sub_mod] = 'y'

            for sub_mod in mods_to_uninstall:
                sub_mod_dir = path.join(mod_dir, sub_mod)
                css_name = find_css_under_dir(sub_mod_dir)

                if css_name is None:
                    color_print(f"Notes of '{sub_mod}':", YELLOW)
                    with open(path.join(sub_mod_dir, 'README.md')) as f:
                        color_print(f.read(), YELLOW)
                else:
                    os.remove(path.join(self.chrome_dir, css_name))
                    color_print(f"[-] '{sub_mod}' was successfully uninstalled!", GREEN)

                del config[mod][sub_mod]

            print()

            if len(config[mod]) == 0:
                del config[mod]
            self.config.write()

    def themes(self):
        # TODO
        pass

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
