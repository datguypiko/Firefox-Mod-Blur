# Updated for PROTON - Firefox-Mod-Blur
`Last tested ver. 95.0` `/` [`Installation guide below`](https://github.com/datguypiko/Firefox-Mod-Blur/blob/master/README.md#installation) `/` `Designed for Windows 10/11`

![alt text](https://i.imgur.com/i0xLJR1.png) 

###### Mac OS style buttons
![alt text](https://raw.githubusercontent.com/datguypiko/Firefox-Mod-Blur/master/preview/titlebar.gif)

###### Windows Buttons 'userChrome-With_Default_Windows_Buttons-Left-Side.css'

![alt text](https://i.imgur.com/Z9MD1ym.png)

###### One line config 'userChrome-ONE-LINER.css' For Firefox versions below 89.0.0
![alt text](https://i.imgur.com/YwrbCxm.png)

###### Blurred search bar and bookmarks bar
![alt text](https://i.imgur.com/GklKQ6v.png)

![alt text](https://i.imgur.com/OasXFqd.png)

###### Last Tested version: `95.0` (Proton)
```html
Tested on:
 	-- Default Theme and Default Dark Theme
	NEW PROTON 
		-- Windows 10/11 - 95.0 / 94.0.1 / 93.0 / 91.0.2 / 90.0.1 / 90.0 / 89.0.1 / 89.0.0

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
