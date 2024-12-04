fn _find_xmas(lines: &Vec::<&str>, delta: (i32, i32)) -> usize {
    let word = "XMAS";

    let size_i = lines.len();
    let size_j = lines[0].len();

    let mut count = 0;
    for i in 0..size_i {
        for j in 0..size_j {
            let mut found = true;

            for k in 0..4 {
                let ip = i as i32 + k*delta.0;
                let jp = j as i32 + k*delta.1;
                if ( ip < size_i as i32) && (ip >= 0) && 
                    ( jp < size_j as i32) && (jp >= 0) &&
                    (lines[ip as usize].chars().nth(jp as usize) == word.chars().nth(k as usize)){
                } else {
                    found = false;
                }
            }

            if found {
                count += 1;
            }
        }
    }

    count
}

fn find_x_mas(lines: &Vec::<&str>) -> i32{
    let patterns = vec![
        vec!["M.S", ".A.", "M.S"],
        vec!["M.M", ".A.", "S.S"],
        vec!["S.M", ".A.", "S.M"],
        vec!["S.S", ".A.", "M.M"]
    ];

    let mut count = 0;
    // For each possible position
    for i in 0..lines.len()-2 {
        for j in 0..lines[0].len()-2 {
            // For each patern
            for pattern in &patterns {
                // Test the 3 by 3 pattern
                let mut found = true;
                for di in 0..3 {
                    for dj in 0..3 {
                        if !(pattern[di].chars().nth(dj).unwrap() == '.') &&
                            !(pattern[di].chars().nth(dj).unwrap() == lines[i+di].chars().nth(j+dj).unwrap()) {
                                found = false;
                        }
                    }
                }
                if found {
                    count += 1;
                }
            }
        }
    }
    
    count
}

fn main() {
    let _test_lines: Vec::<&str> = "MMMSXXMASM\nMSAMXMSMSA\nAMXSXMAAMM\nMSAMASMSMX\nXMASAMXAMM\nXXAMMXXAMA\nSMSMSASXSS\nSAXAMASAAA\nMAMMMXMMMM\nMXMXAXMASX".lines().collect();

    let _input_str = std::fs::read_to_string("input").unwrap();
    let _input_lines = _input_str.lines().collect();

    // let deltas = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)];

    // let mut res = 0;
    // for delta in deltas {
    //     res += find_xmas(&_input_lines, delta);
    // }

    let res = find_x_mas(&_input_lines);
    println!("{res}");
}
