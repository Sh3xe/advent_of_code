use std::rc::Rc;
use std::thread;

enum LL<T> {
    Node(T, Rc::<LL::<T>>),
    Empty
}

impl<T> LL<T> {
    #[allow(unused)]
    fn new() -> Self {
        LL::Empty
    }

    #[allow(unused)]
    fn len(&self) -> usize {
        match self {
            LL::Empty => 0,
            LL::Node(_, l) => 1 + l.len()
        }
    }

    #[allow(unused)]
    fn from_it<I>(it: &mut I) -> Self
    where I: std::iter::Iterator<Item=T> {
        match it.next() {
            None => LL::Empty,
            Some(value) => LL::Node(value, Rc::new(Self::from_it(it)))
        }
    }

    #[allow(unused)]
    fn iterate<F>(&self, f: F)
    where F: Fn(&T){
        match self {
            LL::Empty => (),
            LL::Node(el, l) => {
                f(&el);
                l.iterate(f);
            }
        }
    }
}

fn transform_stone(stone: &String) -> (String, Option<String>) {
    if stone == "0" {
        return (String::from("1"), None);
    }
    else if stone.len() % 2 == 0 {
        return (
            String::from(&stone[0..stone.len()/2]), 
            Some(String::from(&stone[stone.len()/2..]).parse::<usize>().unwrap().to_string())
        );
    }
    else {
        return ((stone.parse::<usize>().unwrap() * 2024).to_string(), None);
    }
}

fn transform_stones(stones: &LL::<String>) -> LL::<String> {
    match stones {
        LL::Empty => LL::Empty,
        LL::Node(stone, rest) => {
            let (right, left) = transform_stone(stone);
            match left {
                None => LL::Node(right, Rc::new(transform_stones(rest))),
                Some(value) => LL::Node(right, Rc::new(LL::Node(value, Rc::new(transform_stones(rest)))))
            }
        }
    }
}

#[allow(unused)]
fn part_1(nums: &str, num_iters: usize) -> usize {
    let mut num_lst  = LL::from_it(&mut nums.split(" ").map(|s| String::from(s)));

    for _ in 0..num_iters {
        num_lst = transform_stones(&mut num_lst);
        // num_lst.iterate(|s| print!("{s} "));
        // println!("");
    }

    num_lst.len()
}

fn other_main() {
    #[allow(unused)]
    let input = "27 10647 103 9 0 5524 4594227 902936";
    #[allow(unused)]
    let test_input = "0 1 10 99 999";

    let stone_count = part_1(input,25);

    println!("Number of stones: {stone_count}");
}

fn main() {
    // Spawn thread with explicit stack size
    let child = thread::Builder::new()
        .stack_size(1024 * 1024 * 1024)
        .spawn(other_main)
        .unwrap();

    // Wait for thread to join
    child.join().unwrap();
}
