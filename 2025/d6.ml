let load_inputs file_path = 
  let file = open_in file_path in

  (* Read all lines *)
  let mat = ref [] in
  try
    while true do
      let line = input_line file in
      let elements = List.map String.trim (String.split_on_char ' ' line)
      |> List.filter (fun x -> x <> "") in
      mat := elements::!mat;
    done;
  with End_of_file -> ();
  close_in file;

  (* Convert to int all but the last one *)
  match !mat with
  | [] -> [[]],[||]
  | op::tail -> List.map (fun el -> List.map int_of_string el) tail, (Array.of_list op) 
in

let part_1 numbers ops =
  let acc = Array.make (Array.length ops) 0 in
  Array.iteri (fun i x -> if x = "*" then acc.(i) <- 1 ) ops;
  List.iter (fun x -> List.iteri (fun i x ->
    if ops.(i) = "+" then
      acc.(i) <- acc.(i) + x
    else 
      acc.(i) <- acc.(i) * x
  ) x) numbers;
  Array.fold_left (+) 0 acc
in

let part_2 numbers ops =
  0
in

let filename = "./inputs/6.txt" in
let numbers, ops = load_inputs filename in
let key_1 = part_1 numbers ops in
let key_2 = part_2 numbers ops in
Printf.printf "Part 1: %d\nPart 2: %d\n" key_1 key_2