// subfolder/Filename.swift - Very brief description
//
// Long description
//
// Copyright (c) 2019 CompanyName
// Licensed under Apache License v2.0 with Runtime Library Exception
//
// See LICENSE.txt for license information
// See CONTRIBUTORS.txt for the list of project authors
//
// -----------------------------------------------------------------------------
///
/// This file contains stuff that I am describing here in the header and will
/// be sure to keep up to date.
///
// -----------------------------------------------------------------------------



//
//  FileName.swift
//  AppName
//
//  Created by FirstName LastName on 2019-02-04.
//  Copyright © 2019 FirstName LastName. All rights reserved.
//



// MARK: Section of the code
// MARK:- Group section of the code with a horizontal divider
// TODO: Connect to user data
// FIXME: This should not be hard coded



// QuickHelp documentation
// https://nshipster.com/swift-documentation/

/**
 Creates a personalized greeting for a recipient.

 - Parameter recipient: The person being greeted.

 - Throws: `MyError.invalidRecipient`
           if `recipient` is "Derek"
           (he knows what he did).

 - Returns: A new string saying hello to `recipient`.
 */
func greeting(to recipient: String) throws -> String {
    guard recipient != "Derek" else {
        throw MyError.invalidRecipient
    }

    return "Greetings, \(recipient)!"
}

/// Returns the magnitude of a vector in three dimensions
/// from the given components.
///
/// - Parameters:
///     - x: The *x* component of the vector.
///     - y: The *y* component of the vector.
///     - z: The *z* component of the vector.
func magnitude3D(x: Double, y: Double, z: Double) -> Double {
    return sqrt(pow(x, 2) + pow(y, 2) + pow(z, 2))
}
