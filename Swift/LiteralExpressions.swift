// Literal Expressions
//
// #file         String              The name of the file in which it appears.
// #line         Int                 The line number on which it appears.
// #column       Int                 The column number in which it begins.
// #function     String              The name of the declaration in which it appears.
// #dsohandle    UnsafeRawPointer    The DSO (dynamic shared object) handle in use where it appears.
//
// https://docs.swift.org/swift-book/ReferenceManual/Expressions.html#ID390


// Print the filename
print(URL(fileURLWithPath: #file).lastPathComponent)

// Print the path with filename
print("\(#file)")

// Print whole string 
print("Filename: \(URL(fileURLWithPath: #file).lastPathComponent) \nPath: \(#file) \nLine: \(#line) \nColumn: \(#column) \nFunction: \(#function)")