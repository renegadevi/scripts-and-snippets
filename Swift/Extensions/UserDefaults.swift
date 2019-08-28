//
//  UserDefaults.swift
//
//  Prints a list of UserDefaults sorted by key to the log output
//

import Foundation

extension UserDefaults {

    static func getUserDefaults() {
        let sortedKeys = UserDefaults.standard.dictionaryRepresentation().sorted{ $0.key < $1.key }
        for (key, value) in sortedKeys {
            NSLog("\(key) = \(value)")
        }
    }

}
