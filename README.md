# Firefox-Mod-Blur
![alt text](https://i.imgur.com/Hi1ocvT.png)

**Tested latest: 84.0.1**
Tested on:
```html
 Windows 10 - 73.0.1 / 74.0 / 74.0.1 / 75.0.0 / 77.0.1 / 80.0 /  84.0.1 | Default Dark Theme
 Linux - 74.0.1 | Default Dark Theme
```
![alt text](https://i.imgur.com/GklKQ6v.png)

**One Line config 'userChrome-ONE-LINER.css'** (dont forget to rename to 'userChrome.css')
![alt text](https://i.imgur.com/k6Yhsgl.png)


Dont forget to enable 'toolkit.legacyUserProfileCustomizations.stylesheets' in about:config for your custom themes to work.

Mac os style buttons addon for firefox 
```html
https://addons.mozilla.org/en-US/firefox/user/12528072/
```

#Blur style search and bookmarks bar.

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

You can find more in 'userChrome.css'
```css
/* Comment this to show min/max/close buttons. I use MAC OS style firefox plugin. ( -> https://addons.mozilla.org/en-US/firefox/user/12528072/ */
  #TabsToolbar > .titlebar-buttonbox-container {visibility: collapse !important;}
```
