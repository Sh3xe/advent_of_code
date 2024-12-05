
fn main() {
    let _test_input = std::fs::read_to_string("test_input").unwrap();
    let _input = std::fs::read_to_string("input").unwrap();

    // get the order of the elements
    let mut sum = 0;
    let mut order_section = true;
    let mut order = Vec::<(i32,i32)>::new(); 
    for line in _input.lines() {
        // order section is over
        if line == "" {
            order_section = false;
            continue;
        }

        if order_section {
            let split: Vec::<&str> = line.split("|").collect();
            order.push((split[0].parse::<i32>().unwrap(), split[1].parse::<i32>().unwrap()));
        } else {

            let split: Vec::<i32> = line
                .split(",")
                .into_iter()
                .map(|a| a.parse::<i32>().unwrap()).collect();

            let mut valid = true;
            for i in 1..split.len() {
                for (before, after) in &order {
                    if split[i-1] == *after && split[i] == *before {
                        valid = false;
                    }
                }
            }

            if valid {
                sum += split[split.len() / 2];
            }
        }
    }

    println!("sum: {sum}");
}
