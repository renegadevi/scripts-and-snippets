
# Disable image smoothing on Firefox

Depending on what use u may hjave, you may want to disable image-smoothening in the browser. For me, I did not want PNG to be smoothened because it's often used for design which would blur images on a site like Dribbble.

This is a guide based on the source: https://nullsleep.tumblr.com/post/16417178705/how-to-disable-image-smoothing-in-modern-web

## 1. Locate your `userContent.css` file

1. Go to "about:support" in your address bar to get to the Troubleshooting-information page.
2. In the table you should see "Profile-folder", open the path.
3. If a folder name `chrome` doesn't exist, create it.
4. Create a file called userContent.css

In the end it should be something like this:
`/Users/renegadevi/Library/Application Support/Firefox/Profiles/{id}.default/chrome/userContent.css`

## 2. Edit the CSS file

Depending on how you want to manage it, you can specify a image format, or just apply on every images as it's just CSS. Because of different browser-versions in the original source, browsers can behave differently, even depending on the OS you're using. 

Read more over at Mozilla how u can optimize it for your personal preference: <br>
https://developer.mozilla.org/en-US/docs/Web/CSS/image-rendering


### Example of `userContent.css` that affects ALL images
```css
img {
    image-rendering: optimizeSpeed;
    image-rendering: -moz-crisp-edges;
    image-rendering: -o-crisp-edges;
    image-rendering: -webkit-optimize-contrast;
    image-rendering: optimize-contrast;
    image-rendering: pixelated;
    -ms-interpolation-mode: nearest-neighbor;
}
```

### Example of `userContent.css` that affects only PNG images (the one I use)
```css
img[src$=".png"] {
    image-rendering: optimizeSpeed;
    image-rendering: -moz-crisp-edges;
    image-rendering: -o-crisp-edges;
    image-rendering: -webkit-optimize-contrast;
    image-rendering: optimize-contrast;
    image-rendering: pixelated;
    -ms-interpolation-mode: nearest-neighbor;
}
```
Save the file.


## 3. Enable use of userContent in Firefox settings

1. Go to  "about:config" in the addressbar
2. Search for "stylesheets"
3. Double-click on `toolkit.legacyUserProfileCustomizations.stylesheets` to make it set to true.


.. Restart Firefox to take affect.
