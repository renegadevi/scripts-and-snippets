//
//  BuildInfo.swift
//s
//

import Foundation

public struct BuildInfo {

    static func versionNumber() -> String {
        return Bundle.main.infoDictionary!["CFBundleShortVersionString"] as! String
    }

    static func buildNumber() -> String {
        return Bundle.main.infoDictionary!["CFBundleVersion"] as! String
    }

    static func longVersionBuild() -> String {
        return "\(versionNumber()) build \(buildNumber())"
    }

}

