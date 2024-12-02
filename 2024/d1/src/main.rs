use std::fs::read_to_string;

fn fill_left_right_vec(left: &mut Vec<i32>, right: &mut Vec<i32>, file_name: &str) {
    let file_content = read_to_string(file_name).unwrap();

    for line in file_content.lines() {
        let parts = line.split("   ");
        let mut is_first = true;
        for part in parts {
            let val = part.parse::<i32>().unwrap();

            if !is_first {
                left.push(val);
            } else {
                is_first = !is_first;
                right.push(val);
            }
        }
    }
}

fn solve_problem_p1(file_name: &str) -> i32 {
    let mut left: Vec<i32> = Vec::new();
    let mut right: Vec<i32> = Vec::new();

    fill_left_right_vec(&mut left, &mut right, file_name);

    left.sort();
    right.sort();

    let mut sum = 0;
    for i in 0..left.len() {
        sum += (left[i] - right[i]).abs();
    }

    sum
}

fn solve_problem_p2(file_name: &str) -> i32 {
    let mut left: Vec<i32> = Vec::new();
    let mut right: Vec<i32> = Vec::new();

    fill_left_right_vec(&mut left, &mut right, file_name);

    let mut score = 0;
    for l_el in left {
        let mut similarity = 0;
        for r_el in &right {
            if l_el == *r_el {
                similarity += 1;
            }
        }

        score += l_el * similarity;
    }

    score
}

fn main() {
    let solution = solve_problem_p2("input");
    println!("Solution: {solution}");
}
