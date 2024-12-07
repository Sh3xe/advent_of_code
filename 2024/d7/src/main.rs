fn is_possible(result: i64, rest: &mut [i64]) -> bool {
    if rest.len() == 1 {
        result == rest[0]
    } else {
        let second_value = rest[1];
        rest[1] = rest[0] * second_value;
        let case_mul = is_possible(result, &mut rest[1..]);
        rest[1] = rest[0] + second_value;
        let case_add = is_possible(result, &mut rest[1..]);
        rest[1] = (rest[0].to_string() + &second_value.to_string()).parse::<i64>().unwrap();
        let case_concat = is_possible(result, &mut rest[1..]);
        rest[1] = second_value;
        case_add || case_mul || case_concat
    }
}

fn main() {
    let _input: String = std::fs::read_to_string("input").unwrap();
    let _test_input = std::fs::read_to_string("test_input").unwrap();

    let mut sum = 0;
    for line in _input.lines() {
        let split: Vec::<&str> = line.split(": ").collect();
        let result = split[0].parse::<i64>().unwrap();
        let mut rest: Vec::<i64> = split[1].split(" ").map(|el| el.parse::<i64>().unwrap()).collect();

        if is_possible(result, &mut rest[..]) {
            sum += result;
        }
    }

    println!("{sum}");
}
