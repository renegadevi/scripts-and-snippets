//
// StringExtensions.swift
//
// By making a 'extension' a 'public extension', we can use it everywhere where
//

import Foundation

public extension String {

    /// Remove prefix in string
    func removePrefix(_ prefix: String) -> String {
        guard self.hasPrefix(prefix) else { return self }
        return String(self.dropFirst(prefix.count))
    }

    /// Return only digits
    var stripNonDigits: String {
        return String(self.filter("0123456789".contains))
    }

    /// Capitalize first letter in string
    var capitalizingFirstLetter: String {
        return String(self.prefix(1)).capitalized + String(self.dropFirst())
    }

    /// Remove whitespaces from string
    var removeWhitespaces: String {
        return self.components(separatedBy: .whitespaces).joined()
    }

    /// Check for valid email address (based on RFC 5322 standard from https://emailregex.com/)
    var isValidEmail: Bool {
        let emailRegex = "[A-Z0-9a-z._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,64}"
        let emailPredicate = NSPredicate(format: "SELF MATCHES %@", emailRegex)
        return emailPredicate.evaluate(with: self)
    }

    /// Check if Alphanumeric
    var isAlphanumeric: Bool {
        return !isEmpty && range(of: "[^a-zA-Z0-9]", options: .regularExpression) == nil
    }

}
