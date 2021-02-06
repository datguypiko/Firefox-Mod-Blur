# Firefox-Mod-Blur
`Firefox ver.` `85.0.0` `/` [`Installation guide below`](https://github.com/datguypiko/Firefox-Mod-Blur/blob/master/README.md#installation) `Windows 10` `Mac OS` `Linux`
![alt text](https://i.imgur.com/Hi1ocvT.png) 

##### Changed tabs design `'userChrome-imUsingThis.css'` `Folder icons removed in Bookmarks bar`
![alt text](https://i.imgur.com/6ZKkYxn.png)

##### One line config `'userChrome-ONE-LINER.css'`
![alt text](https://i.imgur.com/YwrbCxm.png)

##### Blurred search bar and bookmarks bar
![alt text](https://i.imgur.com/GklKQ6v.png)

![alt text](https://i.imgur.com/OasXFqd.png)

##### Last Tested version: `85.0.0`
```html
Tested on:
 	Default Theme and Default Dark Theme
	Windows 10 - 73.0.1 / 74.0 / 74.0.1 / 75.0.0 / 77.0.1 / 80.0 /  84.0.1 / 85.0.0
 	Linux - 74.0.1 | Default Dark Theme
```

</br>

## Installation

**`Dont forget to rename the chosen template file to`** *`'userChrome.css'`*

1. Enable *`toolkit.legacyUserProfileCustomizations.stylesheets`* in *`about:config`* for your custom themes to work.
2. You can find your profile place by going to *`about:support`* and using *`Open folder`* in *`Profile folder`* section.
3. File Structure (Create *`chrome`* folder inside your main profile folder if it doesnt exist):

	>`...` `/` `chrome` `/` `userChrome.css`

	>`...` `/` `chrome` `/` `userContent.css`

	>`...` `/` `chrome` `/` `image` `/`
    

4. For blur style search dropdown and bookmarks bar to work:
	
    Go to *`about:config`* and enable *`layout.css.backdrop-filter.enabled`* (change to *`true`*).
    > Optional: if it still doesnt show up try enabling *`gfx.webrender.enabled`* (change to *`true`*).
    
    > It could even require updated GPU drivers but that's rarely an issue.

5. I use firefox integrated Flexible space for spacing [`https://imgur.com/a/Gd82v0H`](https://imgur.com/a/Gd82v0H).

6. Mac os style buttons for firefox:

    [`Mac OS Style https://addons.mozilla.org/en-US/firefox/user/12528072/`](https://addons.mozilla.org/en-US/firefox/user/12528072/)  (go to customization mode in firefox to move them around.
    
   > or [`Windows Style https://addons.mozilla.org/en-US/firefox/user/13253983/`](https://addons.mozilla.org/en-US/firefox/user/13253983/)

7. Optional. Enable default window min/max buttons:  
    
    Open *`userChrome.css`* file with any text edditor and remove or comment out first lines:
    <ul><pre>
      /* MIN MAX CLOSE Remove */
      #TabsToolbar > .titlebar-buttonbox-container {
      visibility: collapse !important;}
    </pre></ul>  
</br>

---

**`Source for backdropfilter:`** `https://www.reddit.com/r/FirefoxCSS/comments/ddi4dc/testing_the_backdropfilter_in_the_url_dropdown/`
