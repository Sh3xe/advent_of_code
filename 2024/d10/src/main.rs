use std::collections::HashMap;

fn line_to_vec(line: &str) -> Vec<i32> {
    let mut vec = vec![];
    for c in line.chars() {
        vec.push(c.to_digit(10).unwrap() as i32);
    }
    vec
}

fn trailhead_score_unique(
    map: &Vec<Vec<i32>>,
    i: i32, j: i32,
    starts_at: i32,
    reachable: &mut HashMap::<(i32,i32), bool>) {
    // Not a trailhead
    if map[i as usize][j as usize] != starts_at {
        return;
    }
    
    // End of trailhead
    if starts_at == 9 {
        reachable.insert((i,j), true);
        return;
    }

    for (di,dj) in [(0,1), (1,0), (0,-1), (-1, 0)] {
        if 
            i + di < 0 || 
            i + di >= map.len() as i32 ||
            j + dj < 0 ||
            j + dj >= map[0].len() as i32 {
            continue;
        }

        trailhead_score_unique(map, i+di, j+dj, starts_at+1, reachable);
    }
}

fn trailhead_score_total(
    map: &Vec<Vec<i32>>,
    i: i32, j: i32,
    starts_at: i32) -> i32 {
    // Not a trailhead
    if map[i as usize][j as usize] != starts_at {
        return 0;
    }
    
    // End of trailhead
    if starts_at == 9 {
        return 1;
    }

    let mut total = 0;
    for (di,dj) in [(0,1), (1,0), (0,-1), (-1, 0)] {
        if 
            i + di < 0 || 
            i + di >= map.len() as i32 ||
            j + dj < 0 ||
            j + dj >= map[0].len() as i32 {
            continue;
        }

        total += trailhead_score_total(map, i+di, j+dj, starts_at+1);
    }

    total
}

#[allow(unused)]
fn part_1(map: &Vec<Vec<i32>>) {
    let mut total_score = 0;
    for i in 0..map.len() {
        for j in 0..map[0].len() {
            let mut reachable = HashMap::<(i32,i32), bool>::new();
            trailhead_score_unique(&map, i as i32, j as i32, 0, &mut reachable);
            let score = reachable.keys().count();
            total_score += score;
        }
    }

    println!("Score: {total_score}");
}

#[allow(unused)]
fn part_2(map: &Vec<Vec<i32>>) {
    let mut total_score = 0;
    for i in 0..map.len() {
        for j in 0..map[0].len() {
            total_score += trailhead_score_total(&map, i as i32, j as i32, 0);
        }
    }

    println!("Score: {total_score}");
}

fn main() {
    let input = std::fs::read_to_string("input").unwrap();
    let map: Vec<Vec<i32>> = input.lines().filter(|a| a.len() > 0).map(line_to_vec).collect();

    part_1(&map);
    part_2(&map);
}