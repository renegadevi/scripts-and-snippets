//
// FirstLaunch.swift
//
// Check if a user is launching the app for the first time.
//
// Note:
// - Tested using Xcode 11.0 beta 6 on MacOS Mojave 10.14.5
// - Tested by original author using Swift 3
//
// Original source:
// - jalone (https://stackoverflow.com/a/39459520)
//
// "Just use it wherever you want as UIApplication.isFirstLaunch() and be sure
// to reach it at least once during first execution."
//

import UIKit

private var firstLaunch : Bool = false

extension UIApplication {

    static func isFirstLaunch() -> Bool {
        let firstLaunchFlag = "isFirstLaunchFlag"
        let isFirstLaunch = UserDefaults.standard.string(forKey: firstLaunchFlag) == nil
        if (isFirstLaunch) {
            firstLaunch = isFirstLaunch
            UserDefaults.standard.set("false", forKey: firstLaunchFlag)
            UserDefaults.standard.synchronize()
        }
        return firstLaunch || isFirstLaunch
    }
}
