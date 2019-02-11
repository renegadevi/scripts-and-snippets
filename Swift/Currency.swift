// Get currency based on country (Xcode 10, Swift 4.2 or later)
//
// Solution by Leo Dabus
// https://stackoverflow.com/a/47172167/10572532

extension Locale {
    static let currency = Locale.isoRegionCodes.reduce(into: [:]) {
        let locale = Locale(identifier: Locale.identifier(fromComponents: [NSLocale.Key.countryCode.rawValue: $1]))
        $0[$1] = (locale.currencyCode, locale.currencySymbol)
    }
}

Locale.currency["US"]   // (code "USD", symbol "US$")
Locale.currency["BR"]   // (code "BRL", symbol "R$")
Locale.currency["GB"]   // (code "GBP", symbol "£")
