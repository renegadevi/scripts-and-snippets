//
// BoolExtensions.swift
//
// By making a 'extension' a 'public extension', we can use it everywhere where
//

import Foundation

public extension Bool {

    /// Convert bool value to a Yes/No-string
    var boolToString: String {
        if self == true {
            return String("Yes")
        }
        return String("No")
    }

}
