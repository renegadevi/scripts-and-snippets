# How to properly fix MacOS font-rendering (such as Mojave)

## Introduction

Starting with MacOS Mojave, Apple has decided to change things up when it comes to font rendering. It looks fine on HiDPI/Retina displays but once you plug in a non-retina display such as 1080p or 1440p display it can look blurry/pixellated and/or text is too thin.

> According to Apple, the removal of subpixel-antialiasing has to do with the use of newer displays technologies is using different types of subpixel-arrangement. Apple's subpixel-antialiasing was made for LCDs in the early 00s which depends on a specific subpixel-arrangement, while newer display technologies such as OLED (iPhone) does not conform to this.

There's two ways to fix this in Mojave. The easy one is to enable font smoothening which applies a linear blend of gray shades. I addition to that, the bit more advanced is to make MacOS render HiDPI to then scale that image down. See my results below.

![screenshot-01](https://gitlab.com/renegadevi/scripts-and-snippets/raw/master/MacOS/screenshots/fix-font-rendering-01.png)

**Closeup Before (Mojave/1440p):**

![Mojave-OFF](https://gitlab.com/renegadevi/scripts-and-snippets/raw/master/MacOS/screenshots/fix-font-rendering-HiDPi_Mojave-OFF.jpg)

**Closeup After - HiDPi/Retina mode (Mojave/1440p):**

![Mojave-OFF](https://gitlab.com/renegadevi/scripts-and-snippets/raw/master/MacOS/screenshots/fix-font-rendering-HiDPi_Mojave-ON.jpg)


---


## Enable Font smoothing 

1. Open `Terminal.app` and type:

```sh
defaults write -g CGFontRenderingFontSmoothingDisabled -bool NO
```

2. Press Enter, when it's done, close `Terminal.app`, log out and in again or reboot to make it take affect. 

3. Go to **"System Preferences > General"** and you'll see the checkbox "Use font smoothing when avaiable" at the bottom. By checking and unchecking you can see the difference. The effect can look slighty different on different monitors.



### Adjust thickness (Optional)

When Font smoothning is enabled we can also adjust the thickness by setting a value with `defaults`.

Open `Terminal.app`and for the wanted font weight you want, type:

**Light**

```sh
defaults -currentHost write -globalDomain AppleFontSmoothing -int 1
```

**Medium**

```sh
defaults -currentHost write -globalDomain AppleFontSmoothing -int 2
```

**Bold**

```sh
defaults -currentHost write -globalDomain AppleFontSmoothing -int 3
```

**Regular *(Revert changes)*:**

```sh
defaults -currentHost delete -globalDomain AppleFontSmoothing
```

Press enter. Afterwards, close `Terminal.app`, log out and in again or reboot to make it take affect. 



## Render using HiDPi/Retina mode

*__Note__: This can or will affect your GPU performance.*

If you're still not happy with the font-rendering you can go yet another step and use this more advanced method. With this method we tell the system that we have a HiDPI display by rendering twice the resolution which then scales down to our monitor. This will enable the Retina sharp font-rendering and if you like me rely on the **Accessibility zoom** feature, this will make zoom as well as screenshots sharper.

Example for my personal setup I use  2x1440p displays, this method will result in instead of rendering 2560x1440px per display, we will render 5120x2880px per display. I use a *Sapphire Radeon RX580* as my primary GPU and when using this method it constantly lays around 20-30% usage.

As this is built-in to MacOS, this method can be applied by different type of software and ways to accomplish same thing. In this guide I'll be using **SwitchResX** because I find it to be the most reliable and consistent software for MacOS. It cost 14eur but offers a free trial-period. It lets you take full control of your displays. I've been using it for around a decade by now for all my Macs to control the display output.



### Walktrough

*__Note:__ In order to later on add a custom resolution, we first need to make sure SIP is diabled.* 

1. Reboot your computer and boot into "Recovery mode" *(Command + R)*
2. Select Utilities from the menu and select "Terminal"
3. To check SIP status, type:

```sh
csrutil status
```

4. To disable SIP, type:

```sh
csrutil disable
```

5. Close and reboot your computer.

6. Download and install SwitchResX from https://www.madrau.com/

7. Open SwitchResX inside System Preferences

8. In the sidebar, select your monitor.

![screenshot-02](https://gitlab.com/renegadevi/scripts-and-snippets/raw/master/MacOS/screenshots/fix-font-rendering-02.png)

9. Press on the tab for "Custom resolutions"
10. Press on the [+] button in the bottom left corner to add a custom resolution
11. In the dropdown, select "Scaled resolution"
12. Enter twice the amount of pixels for your display horizontal and vertical. (For a 1080p display, that would be: 3840 x 2160, for my 1440p displays that would be 5120 x 2880)

![screenshot-03](https://gitlab.com/renegadevi/scripts-and-snippets/raw/master/MacOS/screenshots/fix-font-rendering-03.png)

13. Press OK
14. Log out and in/reboot if needed.
15. In SwitchResX, Select the "Current Resolutions" tab
16. Now you should see a entry where it say "1920x1080" or in my case "2560x1440" that has a "HiDPI" label next to it. Select it and you're up and running with HiDPI mode.

![screenshot-04](https://gitlab.com/renegadevi/scripts-and-snippets/raw/master/MacOS/screenshots/fix-font-rendering-04.png)

17. Select and then close SwitchResX. 
18. Reboot your computer and boot into "Recovery mode" *(Command + R)*
19. Select Utilities from the menu and select "Terminal"
20. To enable SIP, type:

```sh
csrutil enable
```

21. Reboot your computer. Done!
