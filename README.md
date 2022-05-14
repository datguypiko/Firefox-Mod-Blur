##### `14/05/2022`
> ##### Fixed after an update broken popup menu background color for 100.x versions of firefox.

##### `13/02/2022`
> ##### Added new optional file for default size scrollbar. The color stays dark. Works best with new Windows 11 scrollbar. </br>Use "userContent-Scrollbar-DefaultSize.css" file and rename it to "userContent.css".


</br>

:warning: 
> If you want to use version from after 96.0. I made multiple files without blur effect. Use any of selected styles with the tag *'-NoBlur-'* until they fix the issue. More about the issue why it's disabled for now https://bugzilla.mozilla.org/show_bug.cgi?id=1749625.

:warning:
> *If you update to :x:**96.0 or newer** you will lose blur effect and everything will be transparent. Use at least :heavy_check_mark:**95.0.2** or downgrade to it https://support.mozilla.org/en-US/kb/install-older-version-firefox untill they fix it. Or use the one without blur.* 

:warning:

</br>


# Updated for PROTON - Firefox-Mod-Blur
`No blur for 100.x yet` `Last tested ver. 100.0` `/` [`Installation guide below`](https://github.com/datguypiko/Firefox-Mod-Blur/blob/master/README.md#installation) `/` `Designed for Windows 10/11`

![alt text](https://i.imgur.com/RngH3GW.png) 

###### Mac OS style buttons (left side by default)
![alt text](https://raw.githubusercontent.com/datguypiko/Firefox-Mod-Blur/master/preview/titlebar.gif)

###### `MacOS Style Buttons:` Right *'userChrome-NoBlur-MacOsStyleButtonsRightSide.css'* ---- Left *'userChrome-NoBlur-MacOsStyleButtonsLeftSide.css'*

![alt text](https://i.imgur.com/vda7CNM.png)

###### `Windows Style Buttons` Right *'userChrome-NoBlur-WindowsButtonsRightSide.css'* ---- Left *'userChrome-NoBlur-WindowsButtonsLeftSide.css'*

![alt text](https://i.imgur.com/Z9MD1ym.png)

###### One line config: 'userChrome-ONE-LINER.css' For Firefox versions below 89.0.0
![alt text](https://i.imgur.com/YwrbCxm.png)

###### Blurred search bar and bookmarks bar
![alt text](https://i.imgur.com/GklKQ6v.png)

![alt text](https://i.imgur.com/OasXFqd.png)

###### Last Tested version: `100.0` (Proton)
```html
Tested on:
 	-- Default Dark Theme
	NEW PROTON 
		-- Windows 10/11 - 100.0 / 99.0.1/ 98.0 / 97.0.1 / 96.0.3 / 96.0 / 95.0 / 94.0.1 / 93.0 / 91.0.2 / 90.0.1 / 90.0 / 89.0.1 / 89.0.0

	Old Firefox Versions:
		-- Windows - 73.0.1 / 74.0 / 74.0.1 / 75.0.0 / 77.0.1 / 80.0 /  84.0.1 / 85.0.0
 		-- Linux - 74.0.1 | Default Dark Theme
```

</br>

## Installation

###### Use *`Dark`* theme for firefox to avoid any color issues. https://i.imgur.com/yFZbyo7.png
**`Dont forget to rename the chosen template file to`** *`'userChrome.css'`*

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

###### Optional. Download 'userChrome-With_Windows_Buttons.css' to have windows default buttons.
   
</br>

---

**`Source for Backdrop filter:`** [`https://www.reddit.com/r/FirefoxCSS/comments/ddi4dc/testing_the_backdropfilter_in_the_url_dropdown/`](https://www.reddit.com/r/FirefoxCSS/comments/ddi4dc/testing_the_backdropfilter_in_the_url_dropdown/)

**`Source for Windows Control buttons:`** [`https://github.com/aminomancer/uc.css.js/tree/master/resources/window`](https://github.com/aminomancer/uc.css.js/tree/master/resources/window)
