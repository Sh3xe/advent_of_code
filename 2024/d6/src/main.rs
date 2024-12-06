use std::collections::HashMap;

fn _print_map(map: &Vec::<Vec<char>>) {
    for line in map {
        for c in line {
            print!("{c}");
        }
        print!("\n");
    }
}

fn _step(map: &mut Vec::<Vec<char>>) -> bool {
    let height = map.len();
    let width = map[0].len();
    let deltas: HashMap<char, (i32, i32)> = HashMap::from([
        ('v', (1, 0)),
        ('>', (0, 1)),
        ('<', (0, -1)),
        ('^', (-1, 0))
    ]);
    let next_direction: HashMap<char, char> = HashMap::from([
        ('v', '<'),
        ('>', 'v'),
        ('<', '^'),
        ('^', '>')
    ]);

    for x in 0..width {
        for y in 0..height {
            let guard_dir = map[y][x];
            if "<>v^".contains(guard_dir) {
                let (dy,dx) = deltas.get(&guard_dir).unwrap();
                if !(0 <= (x as i32) + dx && (x as i32) + dx < width as i32 && 0 <= y as i32 + dy && y as i32 + dy < height as i32) {
                    return true;
                }

                if map[(y as i32+dy) as usize][(x as i32+dx) as usize] != '#' {
                    map[y][x] = 'A';
                    map[(y as i32+dy) as usize][(x as i32+dx) as usize] = guard_dir;
                } else {
                    map[y][x] = next_direction.get(&guard_dir).unwrap().clone();
                }
            }
        }
    }

    false
}

fn _count_positions(map: &Vec::<Vec<char>>) -> usize {
    let height = map.len();
    let width = map[0].len();

    let mut count: usize = 0;
    for x in 0..width {
        for y in 0..height {
            if map[y][x] == 'A' {
                count += 1;
            }
        }
    }

    count
}

fn main() {
    // File parsing
    let input_filepath = "input";
    let input_str = std::fs::read_to_string(input_filepath).unwrap();

    let mut map = Vec::<Vec::<char>>::new();
    for line in input_str.lines() {
        let mut line_vec = Vec::<char>::new();
        for c in line.chars() {
            line_vec.push(c);
        }

        map.push(line_vec);
    }

    // Algorithm
    for _ in 0..map.len() * map[0].len() {
        if _step(& mut map) {
            break;
        }
    }

    let ans = _count_positions(&map);

    println!("{ans}");
}
