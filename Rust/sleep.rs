use std::{thread, time};

/// Sleep snippet using duration
pub fn sleep() {
    thread::sleep(time::Duration::from_secs(5));
}