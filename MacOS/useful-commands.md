# Install Brew package manager
```sh
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

## Install brew packages from list
```sh
brew install $(<packages.txt)
```

**packages.txt**
```
htop
ffmpeg
youtube-dl
httpie
neofetch
sshfs
vim
tldr
python3
pyenv
zsh
zsh-syntax-highlightning
```


# Show hidden files

**Note:** You can also toggle this by using cmd+shift+. (period) inside Finder in recent versions of MacOS.

```sh
defaults write com.apple.finder AppleShowAllFiles -bool TRUE; killall Finder
```

# Gatekeeper
```sh
# Status
spctl --status

# Disable
spctl --master-disable

# Enable
spctl --master-enable
```


# SIP (System Integrity Protection)
```sh
# Status
csrutil status

# Disable
csrutil disable

# Enable
csrutil enable
```


# Remote mount drive
```sh
sshfs username@server:/path-on-server/ ~/path-to-mount-point -ovolname=NAME
```

# List Kernel-extensions
```sh
kexstat
``` 
## List all non-apple loaded kexts
```sh
kextstat | grep -v com.apple
```

# Convert audio to iPhone format (SMS/Ringtone etc.)
```sh
afconvert input.mp3 output.m4r -f m4af 
```

# Show stored Wifi password
```sh
security find-generic-password -D "AirPort network password" -a "NETWORKNAME-SSID" -gw
```

# Change Launchpad (Springboard) grid size
**8 x 5 fits 1440p displays the best**
```sh
# Columns
defaults write com.apple.dock springboard-columns -int 8

# Rows
defaults write com.apple.dock springboard-rows -int 5

# Restart
killall Dock
```

# Show Library folder
```sh
chflags nohidden ~/Library/
```

# Enable Airdrop on older/unsupported Macs
```sh
defaults write com.apple.NetworkBrowser BrowseAllInterfaces 1; killall Finder
```

# Enable Sidecar on unsupported Macs (Catalina)
```sh
# Connect your iPad to your Mac, then run this. 
defaults write com.apple.sidecar.display AllowAllDevices -bool true
defaults write com.apple.sidecar.display hasShownPref -bool true
open /System/Library/PreferencePanes/Sidecar.prefPane
```

# Display file extensions in Finder
```sh
defaults write NSGlobalDomain AppleShowAllExtensions -bool true; killall Finder
```
