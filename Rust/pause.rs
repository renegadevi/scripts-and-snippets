use std::io::{stdout, stdin, Write};

/// Pause code, until user interaction
///
/// # Arguments
/// - message: optional message to the user
///
/// # Example
/// ```rust
/// pause(None)
/// pause(Some("Hello there"))
/// ```
pub fn pause(message: Option<&str>) {

    // Create a new output handler
    let mut stdout = stdout();

    // Print optional message
    match message {
        Some(p) => { stdout.write(p.as_bytes()).unwrap(); },
        None => {}
    }

    // Print message to the user
    stdout.write(b"\nPress Enter to continue...").unwrap();

    // Flush the console
    stdout.flush().unwrap();

    // Write to output
    stdin()
        .read_line(&mut String::new())
        .unwrap();
}

fn main() {
    // Example
    pause(Some("Hello there"));
    pause(None);

}