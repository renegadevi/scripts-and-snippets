# Troubleshooting Mac App Store

Always open `Console.app` and search for *"App Store"* to reveal real time data. If you notice something consistent, then inspect that and google the issue which could help or steer you in the right direction. 

Here's just a small list of a couple of common issues and possible solutions. Some issues can also be depending on which version of MacOS you're running, so nothing is always a definitive answer with Apple's services.


## Are you having issues with multiple Apple services?
-   Check Apple system status if anything is down: 
    https://www.apple.com/support/systemstatus/
-   Official Apple instructions: 
    https://support.apple.com/en-gb/HT201400



## Is it just a specific application?

-   Try download another application, if it works, then delete the application with problems and re-install/download again



## Are you getting the infinite spinning circle?
- Check MacOS version if there's been some security updates etc.
- Try force kill `appstoreagent` from Activity Monitor. 
- Try log in/out from your iCloud account and restart your computer.



## Are you unable to connect to AppStore?

-   Check your trusted certificates in Keychain access. (`/Library/Security/Trust Settings`)



## Are you getting Error 500?

This is commonly a issue with `com.apple.commerce.client`. To fix that issue you open `Terminal.app`and type:

```sh
defaults write com.apple.appstore.commerce Storefront -string \
    "$(defaults read com.apple.appstore.commerce Storefront | sed s/,8/,13/)"
```



## Are you unsable to sign in? 

-   Try log in/out from your iCloud account and restart your computer.



## Are you getting a blank page/unable to load?

-   Check your network settings, try restarting the network interface. 



## Clear cache folders

```
~/Library/Caches/storeaccount
~/Library/Caches/storeassets
~/Library/Caches/storedownload
~/Library/Caches/storeinappd
```



## Reset NVRAM

https://support.apple.com/en-gb/HT204063