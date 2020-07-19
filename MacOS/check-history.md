## View Downloads history 
```sh
sqlite3 ~/Library/Preferences/com.apple.LaunchServices.QuarantineEventsV* 'select LSQuarantineDataURLString from LSQuarantineEvent' | awk NF
```

### Clear downloads history 
```sh
# Delete
sqlite3 ~/Library/Preferences/com.apple.LaunchServices.QuarantineEventsV* 'delete from LSQuarantineEvent'

# Rebuild
sqlite3 ~/Library/Preferences/com.apple.LaunchServices.QuarantineEventsV* 'vacuum LSQuarantineEvent'
```


## Clear history command
```sh
# Mojave and older
rm ~/.bash_history

# Catalina and newer
rm ~/.zsh_history
```
