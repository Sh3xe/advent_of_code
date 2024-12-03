fn _part_1(input_content: &str) {
    let reg = regex::Regex::new(r"mul\((?<l>[0-9]+),(?<r>[0-9]+)\)").unwrap();

    let res = reg.captures_iter(&input_content)
        .map(
            |m| 
            m.name("l").unwrap().as_str().parse::<i32>().unwrap() *
            m.name("r").unwrap().as_str().parse::<i32>().unwrap()
        )
        .reduce(|a, b| a + b).unwrap();
        
    println!("res: {res}");
}

fn part_2(input_content: &str) {
    let mul_reg = regex::Regex::new(r"mul\((?<l>[0-9]+),(?<r>[0-9]+)\)").unwrap();
    let do_reg = regex::Regex::new(r"do\(\)").unwrap();
    let dont_reg = regex::Regex::new(r"don't\(\)").unwrap();

    let mut indices = Vec::<(usize, usize)>::new();

    let first_dont = dont_reg.find(&input_content).unwrap().start();
    indices.push((0,first_dont));

    for do_match in do_reg.find_iter(&input_content) {
        let next_dont = match dont_reg.find_at(&input_content, do_match.start()) {
            None => input_content.len(),
            Some(m) => m.start()
        };

        indices.push((do_match.start(), next_dont));
    }


    let mut filtered_indices = Vec::<(usize, usize)>::new();
    let mut i = 0;
    while i < indices.len() {
        let (start, end) = indices[i];
        for j in i+1..indices.len() {
            let (_, other_end) = indices[j];
            if other_end != end {
                continue
            }
            else {
                i = j;
            }
        }
        filtered_indices.push((start, end));
        i += 1;
    }

    let mut sum = 0;
    for (start, end) in filtered_indices {
        println!("{start} {end}");
        let str_slice = &input_content[start..end];
        sum += mul_reg.captures_iter(str_slice)
        .map(
            |m| 
            m.name("l").unwrap().as_str().parse::<i32>().unwrap() *
            m.name("r").unwrap().as_str().parse::<i32>().unwrap()
        )
        .reduce(|a, b| a + b).unwrap();
    }

    println!("{sum}");
}

fn main() {
    let _input_content = std::fs::read_to_string("input").unwrap();
    let _test_input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))";
    part_2(&_input_content);
}
    