# Firefox-Mod

75.0.0 version broke some stuff. Blur isnt working anymore. URL bar changed. 
You can use beta version 'testing_userChrome75-77ver.css' for nigtly and for stable 75.0.0 version. 


```html
Tested on:
 Windows 10 / 73.0.1 / 74.0 / 74.0.1 / Default Dark Theme
 Linux 74.0.1 / Default Dark Theme
```

Dont forget to enable 'toolkit.legacyUserProfileCustomizations.stylesheets' in about:config for your custom themes to work.

![alt text](https://i.imgur.com/Hi1ocvT.png)

You can find more in userChrome.css
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
