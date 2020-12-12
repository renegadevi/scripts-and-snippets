# How to install MacOS BigSur in VMWare Fusion

You do not need to be running BigSur to be able to use a BigSur in a VM and not even newest version of VMWare Fusion, neither latest updates. This works tested and used this on VMWare Fusion 11 on Mojave.

Note: Due to the nature of MacOS and nature of virtualization you won't get full GPU performance.

## 1. Downloading MacOS BigSur

### Alternative 1: Mac App Store
https://apps.apple.com/us/app/macos-big-sur/id1526878132?mt=12

### Alternative 2: Installer assistent
If you don't want to use the App Store you can download the Installer assistent directly from Apple. 

http://swcdn.apple.com/content/downloads/50/49/001-79699-A_93OMDU5KFG/dkjnjkq9eax1n2wpf8rik5agns2z43ikqu/InstallAssistant.pkg

Once downloaded and you have run the pkg, it will end up in your `/Applications` folder just like if you had downloaded from the Mac App Store in the first place.


## 2. Prepare a ISO for VMWare

Open up `Terminal.app` and let's get started

### Create a volume
```sh
hdiutil create -o BigSur2 -size 13000m -volname BigSur2 -layout SPUD -fs HFS+J
```

### Attach volume
```sh
hdiutil attach BigSur2.dmg -noverify -mountpoint /Volumes/BigSur2
```

### Create install media
```sh
sudo /Applications/Install\ macOS\ Big\ Sur.app/Contents/Resources/createinstallmedia --volume /Volumes/BigSur2 --nointeraction
```

### Eject it
```sh
hdiutil eject -force /Volumes/Install\ macOS\ Big\ Sur
```

### Convert to UDTO as a DVD master
```sh
hdiutil convert BigSur2.dmg -format UDTO -o BigSur2
```

### Rename to ISO
```sh
mv -v BigSur2.cdr BigSur2.iso
```

## 3. Let's create our VM

1. Start up VMWare Fusion.

2. File > New

3. Drag your newly made ISO to the window

4. Select Apple OS X > macOS 10.5 as your operating system.

5. Press next, press "Customize Settings", **make sure to dedicate at least 4GB RAM** to your VM. I usually make it a 8GB ram and a 60GB drive.

6. Press Finish and name the VM whatever you want.


## 4. Installing MacOS BigSur

1. Boot the VM

2. Once installer is started, select your language and press next.

3. Open Disk Utility

4. Select the VM drive, press Erase and choose APFS and rename the name if you want.

5. Close Disk Utility, continue installation, and proceed with the initial setup post-install.

6. Once you reach the MacOS desktop. Eject the Install DVD from desktop.

6. Done.


## 5. Optional steps

Take a Snapshot in VMWare to save a clean installation to have something to duplicate and or revert back to.

### VMware Tools

This will enable better VM and window scaling and make some good GPU enhancements that make it way more more usable in daily use and fixes laggy graphics and mouse movement behaviour.

1. Shut down the VM

2. Open Virtual Machine > Settings > Display

3. Select Accelerate 3D Graphics. I use 512MB as shared graphics memory. 

4. Start the VM again.

5. Virtual Machine > Install VMWare Tools, Press Install, then "Install VMWare Tools"

6. Continue with the VMware Tools installer

7. You'll get popup(s) with "System Extension Blocked" during the installer. 
    1. Press "Open Security Preferences" and unlock the settings to press "Allow"
    2. The VMWare Tools Installer will finish as system preferences will prompt to require you rebooting before it can be used, press "Restart" to reboot.

8. Once rebooted, Accessibility Access will propmt you to allow it. 
    1. Press "Open System Preferences", unlock settings and mark the checkbox to allow VMWare to control the behaviour.

9. Done. Take a new Snapshot.
























