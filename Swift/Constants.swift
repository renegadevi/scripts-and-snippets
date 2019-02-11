// Using a case-less enum for global/namespaced constants
//
// https://www.natashatherobot.com/swift-enum-no-cases/


enum ColorPalette {
    static let Red = UIColor(red: 1.0, green: 0.1491, blue: 0.0, alpha: 1.0)
    static let Green = UIColor(red: 0.0, green: 0.5628, blue: 0.3188, alpha: 1.0)
    static let Blue = UIColor(red: 0.0, green: 0.3285, blue: 0.5749, alpha: 1.0)

    enum Gray {
        static let Light = UIColor(white: 0.8374, alpha: 1.0)
        static let Medium = UIColor(white: 0.4756, alpha: 1.0)
        static let Dark = UIColor(white: 0.2605, alpha: 1.0)
    }
}

// This still works as expected!
let red = ColorPalette.Red
let darkGray = ColorPalette.Gray.Dark
