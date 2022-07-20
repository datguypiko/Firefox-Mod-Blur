##### `20/07/2022` [`Last Updates`](https://github.com/datguypiko/Firefox-Mod-Blur#last-updates)
> ##### Changed wallpaper on a blank loading screen to a solid dark color for the "userContent-WallpaperEdition".
##### `19/07/2022`
> ##### Added new theme with background wallpaper and blur effect. 
> ##### Download `userContent-WallpaperEdition.css` rename it to `userContent.css` file, put "wallpaper.jpg" inside `image` folder. If you are using 'png' image file dont forget to rename to "wallpaper.png" in `userContent.css` on line 39. There are some minor graphical glitches that happen sometimes on the blur effect because of the firefox implementation. 

![alt text](https://i.imgur.com/CTOqtpN.jpg) 




# Updated for PROTON - Firefox-Mod-Blur
`Last tested ver. 102.0.1` `/` [`Installation guide below`](https://github.com/datguypiko/Firefox-Mod-Blur#installation) `/` `Designed for Windows 10/11` `/` [`Last Updates`](https://github.com/datguypiko/Firefox-Mod-Blur#last-updates)

###### :warning: :warning: :warning: The Blur effect is still disabled for UI elements by firefox. Only works for website content. (19/07/2022) :warning: :warning: :warning: 

![alt text](https://i.imgur.com/RngH3GW.png) 

###### Mac OS style buttons (left side by default)
![alt text](https://i.imgur.com/kHRVq3Q.gif)

###### `MacOS Style Buttons:` Right *'userChrome-NoBlur-MacOsStyleButtonsRightSide.css'* ---- Left *'userChrome-NoBlur-MacOsStyleButtonsLeftSide.css'*

![alt text](https://i.imgur.com/vda7CNM.png)

###### `Default Operating System Buttons` Right *'userChrome-NoBlur-DefaultOSButtonsRightSide.css'* ---- Left *'userChrome-NoBlur-DefaultOSButtonsLeftSide.css'*

![alt text](https://i.imgur.com/Z9MD1ym.png)

###### One line config: 'userChrome-ONE-LINER.css' For Firefox versions below 89.0.0
![alt text](https://i.imgur.com/YwrbCxm.png)

###### Blurred search bar and bookmarks bar (Still disabled by firefox, use nonBlur or older firefox version)
![alt text](https://i.imgur.com/GklKQ6v.png)

![alt text](https://i.imgur.com/OasXFqd.png)

###### Last Tested version: `102.0.1` (Proton)
```html
Tested on:
 	-- Default Dark Theme
	NEW PROTON 
		-- Windows 10/11 - 102.0.1 / 102.0 / 101.0 / 100.0 / 99.0.1/ 98.0 / 97.0.1 / 96.0.3 / 96.0 / 95.0 / 94.0.1 / 93.0 / 91.0.2 / 90.0.1 / 90.0 / 89.0.1 / 89.0.0

	Old Firefox Versions:
		-- Windows - 73.0.1 / 74.0 / 74.0.1 / 75.0.0 / 77.0.1 / 80.0 /  84.0.1 / 85.0.0
 		-- Linux - 74.0.1 | Default Dark Theme
```

</br>

## Installation

###### Use *`Dark`* theme for firefox to avoid any color issues. https://i.imgur.com/yFZbyo7.png
###### Use "userContent-Windows11_DefaultSizeScrollbar.css" if you have windows 11 because they changed the scrollbar.
**`Dont forget to rename the chosen template files to`** *`'userChrome.css'`* and *`'userContent.css'`*

1. Enable *`toolkit.legacyUserProfileCustomizations.stylesheets`* in *`about:config`* for your custom themes to work.
2. You can find your profile place by going to *`about:support`* and using *`Open folder`* in *`Profile folder`* section.
3. File Structure (Create *`chrome`* folder inside your main profile folder if it doesnt exist):

	>`...` `/` `chrome` `/` `userChrome.css`

	>`...` `/` `chrome` `/` `userContent.css`

	>`...` `/` `chrome` `/` `image` `/`
	
	>`...` `/` `chrome` `/` `window` `/`
    

4. For blur style search dropdown and bookmarks bar to work:
	
    Go to *`about:config`* and enable *`layout.css.backdrop-filter.enabled`* (change to *`true`*).
    > Optional: if it still doesnt show up try enabling *`gfx.webrender.enabled`* (change to *`true`*).
    
    > It could even require updated GPU drivers but that's rarely an issue.

5. I use firefox integrated Flexible space for spacing [`https://imgur.com/a/Gd82v0H`](https://imgur.com/a/Gd82v0H).

   
</br>


---

###### Source for Backdrop filter: [`https://www.reddit.com/r/FirefoxCSS/comments/ddi4dc/testing_the_backdropfilter_in_the_url_dropdown/`](https://www.reddit.com/r/FirefoxCSS/comments/ddi4dc/testing_the_backdropfilter_in_the_url_dropdown/)

###### Source for Windows Control buttons: [`https://github.com/aminomancer/uc.css.js/tree/master/resources/window`](https://github.com/aminomancer/uc.css.js/tree/master/resources/window)

## Last Updates


###### `10/06/2022` Fixed padding in fullscreen after recent version changes.
###### `14/05/2022` Fixed after an update broken popup menu background color for 100.x versions of firefox.
###### `13/02/2022` Added new optional file for default size scrollbar. The color stays dark. Works best with new Windows 11 scrollbar. </br>Use "userContent-Windows11_DefaultSizeScrollbar.css" file and rename it to "userContent.css".
