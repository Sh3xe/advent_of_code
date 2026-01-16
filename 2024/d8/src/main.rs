fn main() {
    // Loading the input
    let _input = std::fs::read_to_string("input").unwrap();
    
    // Parsing the positions of the antenas
    let mut positions: Vec::<(isize, isize, char)> = vec![];
    let mut input_copy: Vec::<Vec::<char>> = vec![];
    let lines: Vec::<&str> = _input.lines().collect();
    for i in 0..lines.len() {
        let mut line_copy: Vec<char> = vec![];
        for j in 0..lines[0].len() {
            let c = lines[i].chars().nth(j).unwrap();
            if c != '.' {
                positions.push((i as isize, j as isize, c));
            }
            line_copy.push(c);
        }
        input_copy.push(line_copy);
    }

    // for each pair of same antenna type, add if necessary a '#'
    for i in 0..positions.len() {
        for j in 0..positions.len() {
            let (pbi,pbj,cb): (isize, isize, char) = positions[i];
            let (pai,paj,ca): (isize, isize, char) = positions[j];

            // same type, look for space to place a '#'
            if ca != cb || i == j{
                continue;
            }

            // find delta
            let (di , dj) = (pbi - pai, pbj - paj);

            let mut iter = 1;
            loop {
                let (pi, pj) = (pbi + di*iter, pbj + dj*iter);
                iter += 1;

                // in bound
                if !(pi >= 0 && pi < input_copy.len() as isize && pj >= 0 && pj < input_copy[0].len() as isize) {
                    break;
                }

                // empty space, place a '#'
                input_copy[pi as usize][pj as usize] = '#';
            }
        }
    }
    
    // count the number of '#'
    let mut count = 0;
    for i in 0..lines.len() {
        for j in 0..lines[0].len() {
            if input_copy[i][j] != '.' {
                count += 1;
            }
            print!("{}", input_copy[i][j]);
        }
        println!("");
    }

    println!("{count}");
}
