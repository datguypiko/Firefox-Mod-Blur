Fixing homepage logos.

Download logo images images from [here](https://github.com/datguypiko/Firefox-Mod-Blur/tree/master/old/LibreWolf) and put it inside `/image/` folder.

</br>

Open userContent.css file and change these:

1. Add this code around line `120` below "body {...}" needs to be inside `@-moz-document url("about:home"), url("about:newtab") {` 



```css
.search-wrapper .logo-and-wordmark .wordmark {
    background: url("image/Logo.png") no-repeat center center !important;
}
.search-wrapper .logo-and-wordmark .logo {
    background: url("image/icon_transparent.svg")  no-repeat center !important;
}
```

2. And for private page

```css
CHANGE THIS CODE AROUND LINE 34

#about-private-browsing-logo.logo {
    background-image: url("image/about-logo-private-changed.png") !important;
    opacity: 0.9 !important;
}

CHANGE TO ---->

#about-private-browsing-logo.logo {
    background-image: url("image/icon_transparent_private.svg") !important;
    opacity: 0.9 !important; 
}
.logo-and-wordmark .wordmark {
    background: url("image/Logo_Private.png") no-repeat center center !important;
    background-size: 172px !important;
}
.logo-and-wordmark {margin-bottom: 50px !important;}
```


