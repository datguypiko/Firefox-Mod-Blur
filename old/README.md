#OLDER VERSION

# <p align="center"> [![firefox](https://user-images.githubusercontent.com/61329159/197364522-ffdb607c-f634-4ddd-a234-7ccc3833d8b6.png)](https://github.com/datguypiko/Firefox-Mod-Blur#wrench-installation) Updated for Proton - Firefox-Mod-Blur </p> 

<p align="center"><a href="#wrench-installation"><img alt="Installation Guide" src="https://img.shields.io/badge/Installation%20Guide-informational?style=flat"></a> <img alt="Version" src="https://img.shields.io/badge/Last%20tested%20ver.-106.0.1-blue?style=flat&logo=firefox&logoColor=white"> <a href="#shield-last-updates"><img alt="Installation Guide" src="https://img.shields.io/badge/Last%20update-20/07/2022-bightgreen?style=flat"></a> <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/datguypiko/Firefox-Mod-Blur?color=green&logo=github&style=flat"> <a href="https://www.reddit.com/r/Firefox/"><img alt="Subreddit subscribers" src="https://img.shields.io/reddit/subreddit-subscribers/Firefox?label=r%2FFirefox&logo=reddit&style=flat&logoColor=white"></a> <a href="https://www.reddit.com/r/FirefoxCSS/"><img alt="FirefoxCSS reddit" src="https://img.shields.io/reddit/subreddit-subscribers/FirefoxCSS?label=More%20r%2FFirefoxCSS&logo=reddit&style=social"></a> </p>

###### <p align="center"> <sup>  :warning: :warning: :warning: :warning: :warning:  The Blur effect is still disabled for UI elements by firefox. Only works for website content or home screen tab. (22/10/2022) :warning: :warning: :warning: :warning: :warning: </sup>
</p>

![alt text](https://i.imgur.com/RngH3GW.png) 

<details><summary>

##### WALLPAPER EDITION <sup>[read more]</sup></summary>

> ##### Download *'userContent-WallpaperEdition-Windows11DefaultScrollbar.css'* (better for win11 scrollbar) or *'userContent-WallpaperEdition-ThinScrollbar.css'*

> ##### Downloaded `WallpaperEdition` rename it to `userContent.css` file, put "wallpaper.jpg" inside `image` folder. If want to use 'png' image dont forget to rename to "wallpaper.png" in `userContent.css` on code line 39.
</details>
 
![alt text](https://i.imgur.com/CTOqtpN.jpg) 

##### MACOS STYLE BUTTONS
![alt text](https://i.imgur.com/kHRVq3Q.gif)

![alt text](https://i.imgur.com/vda7CNM.png)

##### DEFAULT OS BUTTONS

![alt text](https://i.imgur.com/Z9MD1ym.png)

##### ~~BLURRED MOD~~ (Still disabled by firefox)
![alt text](https://i.imgur.com/GklKQ6v.png)

![alt text](https://i.imgur.com/OasXFqd.png)


</br>

## :wrench: Installation

<details><summary>Use <code>Dark</code> theme for firefox to avoid any color issues <sup>[show image]</sup></summary>

![image](https://user-images.githubusercontent.com/61329159/197360837-503f8d50-b2c1-4c29-94d7-870adb1c3ab0.png)</details>

<details><summary><code>Windows 11</code> works best with default size scrollbar so use: <sup>[read more]</sup></summary><p>Use <code>userContent-WallpaperEdition-Windows11DefaultScrollbar.css</code> or <code>userContent-Windows11DefaultScrollbar.css</code></p></details>

<details><summary>I use firefox integrated Flexible space for spacing <sup>[show image]</sup></summary>

![image](https://user-images.githubusercontent.com/61329159/197362629-b5c6e49a-92c4-4d08-aada-f8883e7c471f.png)</details>

1. :exclamation:Rename the chosen template files to `userChrome.css` and `userContent.css`.
2. Enable `toolkit.legacyUserProfileCustomizations.stylesheets` in `about:config` for your custom themes to work.
3. You can find your profile folder by writing `about:support` in URL bar and using `Open folder` in `Profile folder` section.
4. File Structure (Create `chrome` folder inside your main profile folder if it doesnt exist):

	 :open_file_folder: `...` `/` `chrome` `/` `userChrome.css`

	 :open_file_folder: `...` `/` `chrome` `/` `userContent.css`

	 :open_file_folder: `...` `/` `chrome` `/` `image` `/`
	
	 :open_file_folder: `...` `/` `chrome` `/` `window` `/`
	
5. For blur to work in new tab homepage [Wallpaper edition].
	
    - ***[It's now Enabled by default]*** - Go to `about:config` and enable `layout.css.backdrop-filter.enabled` (change to `true`).	
  
6. For blur style search dropdown and bookmarks bar to work [Doesnt work for now since firefox changed it].
	
    - ***[It's now Enabled by default]*** - Go to `about:config` and enable `layout.css.backdrop-filter.enabled` (change to `true`).

</br>

## :shield: Last Updates 

<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/datguypiko/Firefox-Mod-Blur"> <a href="https://github.com/datguypiko/Firefox-Mod-Blur/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/datguypiko/Firefox-Mod-Blur?color=yellow&logo=github&logoColor=white"> </a>

 `20/07/2022` > Changed wallpaper on a blank loading screen to a solid dark color for the "userContent-WallpaperEdition".

 `19/07/2022` > Added new theme with background wallpaper and blur effect. 

 `10/06/2022` > Fixed padding in fullscreen after recent version changes.

 `14/05/2022` > Fixed after an update broken popup menu background color for 100.x versions of firefox.

 `13/02/2022` > Added new optional file for default size scrollbar. The color stays dark. Works best with new Windows 11 scrollbar. </br>Use "userContent-Windows11_DefaultSizeScrollbar.css" file and rename it to "userContent.css".

</br>

## :page_facing_up: Other

<details><summary>Old Firefox versions <sup>[read more]</sup></summary>

> One line config: 'userChrome-ONE-LINER.css' For Firefox versions below 89.0.0
![alt text](https://i.imgur.com/YwrbCxm.png)</details>
<details><summary>Tested versions <sup>[read more]</sup></summary>

```html
Last Tested on:
 	-- Default Dark Theme
	NEW PROTON 
		-- Windows 10/11 - 106.0.1 / 105 / 104.0.1 / 102.0.1 / 102.0 / 101.0 / 100.0 / 99.0.1/ 98.0 / 97.0.1 / 96.0.3 / 96.0 / 95.0 / 94.0.1 / 93.0 / 91.0.2 / 90.0.1 / 90.0 / 89.0.1 / 89.0.0

	Old Firefox Versions:
		-- Windows - 73.0.1 / 74.0 / 74.0.1 / 75.0.0 / 77.0.1 / 80.0 /  84.0.1 / 85.0.0
 		-- Linux - 74.0.1 | Default Dark Theme
```
</details>
<details><summary>Sources <sup>[read more]</sup></summary>

> Source for Backdrop filter: [`https://www.reddit.com/r/FirefoxCSS/comments/ddi4dc/testing_the_backdropfilter_in_the_url_dropdown/`](https://www.reddit.com/r/FirefoxCSS/comments/ddi4dc/testing_the_backdropfilter_in_the_url_dropdown/)

> Source for Windows Control buttons: [`https://github.com/aminomancer/uc.css.js/tree/master/resources/window`](https://github.com/aminomancer/uc.css.js/tree/master/resources/window)
</details>
