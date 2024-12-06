use std::collections::HashMap;

fn _print_map(map: &Vec::<Vec<char>>) {
    for line in map {
        for c in line {
            print!("{c}");
        }
        print!("\n");
    }
}

fn _step(map: &mut Vec::<Vec<char>>, width: usize, height: usize, guard_x: usize, guard_y: usize) -> Option<(usize,usize)> {
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

    let guard_dir = map[guard_y][guard_x];
    if "<>v^".contains(guard_dir) {
        let (dy, dx) = deltas.get(&guard_dir).unwrap();
        let (nx, ny): (i32, i32)= ((guard_x as i32) + dx, (guard_y as i32) + dy);

        if !(0 <= nx && nx < width as i32 && 0 <= ny && ny < height as i32) {
            return None;
        }

        if map[ny as usize][nx as usize] != '#' {
            map[ny as usize][nx as usize] = guard_dir;
            return Some((nx as usize, ny as usize));
        } else {
            map[guard_y][guard_x] = next_direction.get(&guard_dir).unwrap().clone();
            return Some((guard_x, guard_y));
        }
    }

    // sorry for this monstrosity
    println!("SHOULD NOT BE REACEHED");
    _print_map(&map);
    None
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

fn find_guard_position(map: &Vec::<Vec<char>>, width: usize, height: usize) -> Option<(usize, usize)> {
    for x in 0..width {
        for y in 0..height {
            if "<>v^".contains(map[y][x]) {
                return Some((x,y));
            }
        }
    }

    None
}

fn is_position_valid(
    map: &Vec::<Vec<char>>,
    width: usize, height: usize,
    position: (usize, usize),
    guard_pos: (usize, usize) ) -> bool {

    let mut map_cpy = map.clone();
    map_cpy[position.1][position.0] = '#';

    let mut previous_positions = HashMap::<(usize,usize,char), bool>::new();

    let mut current_pos = guard_pos;
    for _ in 0..width*height {
        match _step(&mut map_cpy, width, height, current_pos.0, current_pos.1) {
            None => return false,
            Some(pos) => {
                let key = (pos.0, pos.1, map_cpy[pos.1][pos.0]);
                match previous_positions.get(&key) {
                    None => {
                        current_pos = pos;
                        previous_positions.insert(key, true);
                    },
                    Some(_) => return true
                }
            },
        }
    }
    
    true
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
    let width = map[0].len();
    let height = map.len();
    let guard_position = find_guard_position(&map, width, height).unwrap();

    let mut valid_position_count = 0;
    for x in 0..width {
        for y in 0..height {
            if (x,y) != guard_position && map[y][x] != '#' && is_position_valid(&map, width, height, (x, y), guard_position) {
                valid_position_count += 1;
            }
        }
    }

    println!("{valid_position_count}");
}
