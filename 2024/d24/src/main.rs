use std::collections::HashMap;

fn part_1(str_input: &str) -> usize {
    let mut split = str_input.split("\n\n");
    let inputs = split.next().unwrap();
    let logic_gates = split.next().unwrap();

    let mut registers = HashMap::<String, bool>::new();
    for line in inputs.lines() {
        let mut split = line.split(": ");
        let key = String::from(split.next().unwrap());
        let value = if split.next().unwrap().parse::<i32>().unwrap() == 1 {true} else {false};

        registers.insert(key, value);
    }

    let mut operations = Vec::<(&str, &str, &str, &str)>::new();

    for line in logic_gates.lines() {
        let mut split = line.split(" -> ");
        let left = split.next().unwrap();
        let output_reg = split.next().unwrap();

        split = left.split(" ");
        let in_a = split.next().unwrap();
        let op_code = split.next().unwrap();
        let in_b = split.next().unwrap();

        operations.push((in_a, op_code, in_b, output_reg));
    }

    // Try all operations until it works instead of actually sorting them
    // because I'm stupid and its faster

    for _ in 0..operations.len() {
        for (in_a, op_code, in_b, output) in &operations {
            // try to do the operation
            if !registers.contains_key(*in_a) || !registers.contains_key(*in_b) {
                continue;
            }

            registers.insert(String::from(*output), if *op_code == "AND" {
                registers[*in_a] && registers[*in_b]
            } else if *op_code == "OR" {
                registers[*in_a] || registers[*in_b]
            } else {
                registers[*in_a] != registers[*in_b]
            });
        }
    }


    let mut reg_values = Vec::<(String, bool)>::new();
    for (k,v) in registers {
        if k.chars().nth(0).unwrap() == 'z' {
            reg_values.push((k,v));
        }
    }

    reg_values.sort_by_key(|(k,_)| k[1..].parse::<usize>().unwrap());
    reg_values.reverse();

    let mut binary_num_str = String::new();
    for (k,v) in reg_values {
        if k.chars().nth(0).unwrap() == 'z' {
            binary_num_str += if v {"1"} else {"0"};
        }
    }

    usize::from_str_radix(&binary_num_str, 2).unwrap()
}

fn main() {
    let str_input = std::fs::read_to_string("input.txt").unwrap();
    println!("Part 1: {}", part_1(&str_input));
}