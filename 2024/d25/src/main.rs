
#[derive(Debug)]
enum InEnumType {
    KEY,
    LOCK
}

#[derive(Debug)]
struct InType {
    nums: [i32;5],
    in_type: InEnumType
}

fn parse_input(input: &str) -> (Vec<InType>, Vec<InType>) {
    let mut keys = Vec::<InType>::new();
    let mut locks = Vec::<InType>::new();

    for in_mat in input.split("\n\n") {
        // ignore empty lines
        if in_mat.len() == 0 {
            continue;
        }

        // tranform into InType
        let in_type = if in_mat.chars().nth(0).unwrap() == '#' { InEnumType::KEY } else {InEnumType::LOCK};
        let mut nums = [-1,-1,-1, -1, -1];
        for line in in_mat.lines() {
            line.chars().enumerate().for_each(|(i,e)| {nums[i] += (e == '#') as i32;});
        }

        match in_type {
            InEnumType::LOCK => locks.push(InType{nums, in_type}),
            InEnumType::KEY=> keys.push(InType{nums, in_type}),
        }
    }

    (keys, locks)
}

fn key_lock_fit(key: &InType, lock: &InType) -> bool {
    for i in 0..5 {
        if key.nums[i] + lock.nums[i] > 5 {
            return false;
        }
    }

    true
}

fn main() {
    let input = std::fs::read_to_string("input.txt").unwrap();
    let (keys, locks) = parse_input(&input);

    let mut total_fit = 0;
    for k in &keys {
        for l in &locks {
            total_fit += (key_lock_fit(&k, &l)) as i32;
        }
    }
    println!("Total fit: {total_fit}");
}