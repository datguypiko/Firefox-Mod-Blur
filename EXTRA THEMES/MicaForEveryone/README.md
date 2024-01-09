 ### DEPRECATED WITH FIREFOX v117 and up ⚠️⚠️⚠️⚠️⚠️
 To continue using MicaForEveryone you can use Firefox v115 ESR - Extended Support Release 
 version which will be supported and have security updates for at least a year.
 https://www.mozilla.org/en-US/firefox/all/#product-desktop-esr

<br>
 

Read main readme file or follow below:

    1.Download the portable or installation file from https://github.com/MicaForEveryone/MicaForEveryone
    2.Install the extra files it asks you to install. And run the program.
    3.At the bottom left corner press Add Rule -> Add Process Rule, type firefox -> add.
    4.On the left panel select and open firefox section. Change Mica to Acrylic for better blur effect.
    5.Dont forget to download my css file acrylic_micaforeveryone.css and put it inside Chrome folder (and my main files).
    6.Remove and dont use any other min-max-close window button files.
    7.Expermental⚠️ In MicaForEveryone settings firefox section enable Blur Behind so when the window is not active it will still be blurred.

### Min-max-close and OS Scaling Issue
TDLR anything other than 100% scaling in windows will probably cause issues with the min-max-close window button positioning. 
Because of the firefox implementation for transparency there is nothing you can do dynamically to fix it. 
Firefox creates a second set of icons that you cant interact with, move or remove when setup for transparent window.

Different scaling probably requires different button positioning (resolution could affect it too)

What I did is hide the icons except the close button. The hover effect still works this way.

<br>

If you want to make the hover more centered and 'close' button not jumping on hover, try 
moving them to left, right, top or bottom depending on your situation.

> [!TIP]
> If you dont know how position elements with css, write in Issue I will help.

Example: 

In `acrylic_micaforeveryone.css`:
```css
/*  Moves all icons. Moves 4 pixels down from the top*/
#navigator-toolbox .titlebar-button .toolbarbutton-icon {
  margin-top:4px !important; 
}

/* minimize button */
#navigator-toolbox .titlebar-button.titlebar-min .toolbarbutton-icon { 
 
}

/* max and restore button */
#navigator-toolbox .titlebar-button.titlebar-max .toolbarbutton-icon,
#navigator-toolbox .titlebar-button.titlebar-restore .toolbarbutton-icon { 
  
}

/* close button */
#navigator-toolbox .titlebar-button.titlebar-close .toolbarbutton-icon { 

}
```

**If you want to see the buttons you are trying to position on top**,
remove the line `list-style-image: none !important;` in file `acrylic_micaforeveryone.css` from:
```css
#navigator-toolbox .titlebar-button:not(.titlebar-close),
#navigator-toolbox .titlebar-close:not(:hover) {
	list-style-image: none !important;
}
```

Dont forget to add it later. 
