//
// DateExtensions.swift
//

//
// Collection of Date extensions
//
// By making a 'extension' a 'public extension', we can use it everywhere where
// Date is used depending on what project or use case you have.
//

public extension Date {

    /// Get localized String with DateFormatter
    var localizedStringTime: String {
        return DateFormatter.localizedString(from: self, dateStyle: .none, timeStyle: .short)
    }

    /// Return the amount of centuries from another date
    func centuries(from date: Date) -> Int {
        return Int(floor(Double((Calendar.current.dateComponents([.year], from: date, to: self).year ?? 0) / 100)))
    }

    /// Returns the amount of decades from another date
    func decades(from date: Date) -> Int {
        return Int(floor(Double((Calendar.current.dateComponents([.year], from: date, to: self).year ?? 0) / 10)))
    }

    /// Returns the amount of years from another date
    func years(from date: Date) -> Int {
        return Calendar.current.dateComponents([.year], from: date, to: self).year ?? 0
    }

    /// Returns the amount of months from another date
    func months(from date: Date) -> Int {
        return Calendar.current.dateComponents([.month], from: date, to: self).month ?? 0
    }

    /// Returns the amount of weeks from another date
    func weeks(from date: Date) -> Int {
        return Calendar.current.dateComponents([.weekOfMonth], from: date, to: self).weekOfMonth ?? 0
    }

    /// Returns the amount of days from another date
    func days(from date: Date) -> Int {
        return Calendar.current.dateComponents([.day], from: date, to: self).day ?? 0
    }

    /// Returns the amount of hours from another date
    func hours(from date: Date) -> Int {
        return Calendar.current.dateComponents([.hour], from: date, to: self).hour ?? 0
    }

    /// Returns the amount of minutes from another date
    func minutes(from date: Date) -> Int {
        return Calendar.current.dateComponents([.minute], from: date, to: self).minute ?? 0
    }

    /// Returns the amount of seconds from another date
    func seconds(from date: Date) -> Int {
        return (Calendar.current.dateComponents([.minute], from: date, to: self).minute ?? 0) * 60
    }

    /// Returns the amount of milliseconds from another date
    func milliseconds(from date: Date) -> Int {
        return (Calendar.current.dateComponents([.minute], from: date, to: self).minute ?? 0) * 60 * 1000
    }

    /// Returns the a custom time interval description from another date
    func offset(from date: Date) -> String {
        let formatter = DateComponentsFormatter()
        formatter.allowedUnits = [.day, .month, .year, .hour, .minute]
        formatter.unitsStyle = .full
        return formatter.string(from: date, to: self)!
    }

}
