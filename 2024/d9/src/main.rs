fn main() {
    let path = "test_input";
    let input_str = std::fs::read_to_string(path).unwrap();
    let blocks: Vec::<u32> = input_str.chars().map(|e| e.to_digit(10).unwrap()).collect();

    let mut file_vec: Vec::<i32> = vec![];
    let mut is_empty = false;
    let mut current_id = 0;

    for block_c in &blocks {
        for _ in 0..*block_c {
            if is_empty {
                file_vec.push(-1);
            } else {
                file_vec.push(current_id);
            }
        }
        current_id += !is_empty as i32;
        is_empty = !is_empty;
    }

    // move files
    let mut upper: isize = (file_vec.len()-1) as isize;
    while upper >= 0 {
        // go to the next non empty block
        while file_vec[upper as usize] == -1 {
            upper -= 1;
        }

        // calculate its size
        let mut block_size = 0;
        let block_id = file_vec[upper as usize];
        while file_vec[(upper - block_size) as usize] != -1 {
            block_size += 1
        }

        // look for a block with a greater size
        let mut bottom_id = 0;
        let mut current_size = 0;
        let mut start_id = 0;
        while bottom_id < upper {
            if file_vec[bottom_id as usize] == -1 {
                current_size += 1;
            }

            else {
                // if we found enough space
                if current_size >= block_size {
                    // copy into the space
                    for k in 0..block_size {
                        file_vec[(start_id + k) as usize] = block_id;
                        file_vec[upper as usize] = -1;
                        upper -= 1;
                    }
                    // out of the while loop
                    break;
                }
                current_size = 0;
                start_id = bottom_id;
            }

            bottom_id += 1;
        }
    }



    // calculate checksum
    for i in file_vec {
        print!("{} ", i);
    }

}