fn is_safe(line: &Vec<i32>, ignore_id: usize) -> bool {
    let mut is_ascending = true;
    let mut is_descending = true;

    for i in 1..line.len() {
        if i == ignore_id || (i==1 && ignore_id == 0){
            continue;
        }

        let current_id = i;
        let last_id = if i-1 == ignore_id {
            i-2
        } else {
            i-1
        };

        // 1st rule: delta should be between 1 and 3
        if (line[current_id]-line[last_id]).abs() >= 4 || line[current_id] == line[last_id] {
            return false
        }

        // 2nd rule, should alwase be ascending or descending
        if line[current_id] >= line[last_id] {
            is_descending = false;
        }
        else {
            is_ascending = false;
        }

        if !is_ascending && !is_descending {
            return false
        }
    }

    return true;
}

fn main() {
    let file_content = std::fs::read_to_string("input").unwrap();
    
    let mut safe_count = 0;
    for line in file_content.lines() {
        let split = line.split(" ");
        let mut line_as_vec = Vec::<i32>::new();
        for num_str in split {
            line_as_vec.push(num_str.parse::<i32>().unwrap());
        }

        let mut is_line_safe = false;
        for i in 0..line_as_vec.len() {
            if is_safe(&line_as_vec, i) {
                is_line_safe = true;
                break;
            }
        }

        if is_line_safe {
            safe_count += 1;
        }
    }

    println!("Answer: {safe_count}");
}
