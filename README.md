# Firefox-Mod

**New search bar with some changes and fixes. 75.0+ version**
```html
'userChrome.css'
or 'userChrome_searchbar_noBlur.css' for no blur search bar.
```
![alt text](https://i.redd.it/wpubm02rzfr41.png)

**NEW. Added One Line config 'userChrome-ONE-LINER.css'**
![alt text](https://i.imgur.com/k6Yhsgl.png)


**If you dont like the changes to URL/SEARCH bar it can be reverted with these about:config tweaks. (this will be disabled soon)**

```css
browser.urlbar.update1; set to False
browser.urlbar.openViewOnFocus; set to False (your preference, this disables opening on focus, need to type to open search)
```
and use  'userChrome_old_searchbar.css' for browsers older than 75.0 version.
dont forget to rename to 'userChrome.css'



Tested on:
```html
 Windows 10 / 73.0.1 / 74.0 / 74.0.1 / 75.0.0 / Default Dark Theme
 Linux 74.0.1 / Default Dark Theme
```

Dont forget to enable 'toolkit.legacyUserProfileCustomizations.stylesheets' in about:config for your custom themes to work.

![alt text](https://i.imgur.com/Hi1ocvT.png)

You can find more in 'userChrome.css'
```css
/* Comment this to show min/max/close buttons. I use OS style firefox plugin. */
  #TabsToolbar > .titlebar-buttonbox-container {visibility: collapse !important;}
```

```css
/* Width of the tabs. Change it to 100% to get full 
width style tabs. But it looks funny, make search 
bar transparent so it looks better with full width */
	.tabbrowser-tab[fadein]:not([pinned]) {max-width: 135px !important;}  
```  
![alt text](https://i.imgur.com/8IUIq2g.png)

Blur style search and bookmarks bar. Used the search method found here 

Need about:config 'layout.css.backdrop-filter.enabled' = true
and it could require the 'gfx.webrender.enabled' to true. But if it works with the 'backdrop-filter' leave this one.
```
https://www.reddit.com/r/FirefoxCSS/comments/ddi4dc/testing_the_backdropfilter_in_the_url_dropdown/
```  
 ![alt text](https://i.imgur.com/bU7ahnk.png)
 
 ![alt text](https://i.imgur.com/OasXFqd.png)
 
 I use Flexible space for spacing https://imgur.com/a/Gd82v0H 
 
 
 Linux (blur works too after enabling both options mentioned above).
 
 ![alt text](https://i.imgur.com/0pxPFnW.png)
