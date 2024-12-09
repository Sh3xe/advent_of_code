fn main() {
    let path = "test_input";
    let input_str = std::fs::read_to_string(path).unwrap();
    let blocks: Vec::<u64> = input_str.chars().map(|c| c.to_digit(10).unwrap() as u64).collect();

    let size: u64 = blocks.iter().sum();
    let mut checksum: u64 = 0;

    let mut real_lower = 0;
    let mut relative_upper = (blocks.last().unwrap() - 1) as i32;
    let mut block_lower = 0 as u64;

    let mut real_upper = size-1;
    let mut block_upper = (blocks.len()-1) as u64;

    while real_lower < real_upper {
        // block is full
        if block_lower % 2 == 0 {
            if block_lower == block_upper {
                break;
            }
            for _ in 0..blocks[block_lower as usize] {
                checksum += real_lower * (block_lower / 2);
                real_lower += 1;
            }
        } else {
            let mut k = 0;
            while k < blocks[block_lower as usize] {
                if blocks[block_upper as usize] == 0 {
                    block_upper -= 1;
                    relative_upper = blocks[block_upper as usize] as i32 - 1;
                    continue;
                }

                if block_upper % 2 == 1{
                    real_upper -= blocks[block_upper as usize];
                    block_upper -= 1;
                    relative_upper = blocks[block_upper as usize] as i32 - 1;
                    continue;
                }
                
                checksum += real_lower * (block_upper/2);
                real_upper -= 1;
                relative_upper -= 1;
                real_lower += 1;
                k += 1;

                if relative_upper == -1 {
                    block_upper -= 1;
                    relative_upper = blocks[block_upper as usize] as i32 - 1;
                }
            }
        }
        block_lower += 1;
    }

    if block_lower == block_lower {
        for _ in 0..relative_upper+1 {
            checksum += real_lower * (block_upper / 2);
            real_lower += 1;
        }
    }
    
    println!("{checksum}");
}

// 6451113111501
// 6448989155953