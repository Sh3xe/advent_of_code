fn get_connections(input: &str) -> Vec<(String, String)> {
    input
        .lines()
        .filter(|l| l.len() != 0)
        .map(|l| {
            let mut split = l.split("-");
            (
                String::from(split.next().unwrap()),
                String::from(split.next().unwrap()),
            )
        })
        .collect()
}



fn main() {
    let input = std::fs::read_to_string("../test_input.txt").unwrap();
    let connections = get_connections(&input);


}
