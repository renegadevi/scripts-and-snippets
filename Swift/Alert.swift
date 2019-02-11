// Apple has made an ViewController for popup-alerts called "UIAlertController"
// We also need a dismiss button, which we create trough "UIAlertAction"

@IBAction func showAlert() {

    // Create a alert
    let alert = UIAlertController(
        title: "Hello, World!",
        message: "This is my first app!",
        preferredStyle: .alert
    )

    // Create a alert button, a dismiss button for now
    let action = UIAlertAction(
        title: "Done",
        style: .default,
        handler: nil
    )

    // Add button(s) to alert
    alert.addAction(action)

    // Return/Present/Show the alert
    present(alert, animated: true, completion: nil)

}


// Event handler
// By using a handler, we can pause the application until the user eg. has
// dismissed the button
handler: {
    action in
    self.startNewGame() // Example
}
