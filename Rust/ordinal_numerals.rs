/// Originally written by Felix S. Klock II
/// Updated by annodomini 
/// Rewritten by by Trevor Spiteri
fn num_to_ordinal_expr(x: u32) -> String {
    format!("{}{}", x, match (x % 10, x % 100) {
        (_, 4...20) => "th",
        (1, _) => "st",
        (2, _) => "nd",
        (3, _) => "rd",
        _ => "th",
    })
}
