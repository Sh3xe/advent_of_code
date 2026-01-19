let load_inputs_1 file_path = 
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

let load_inputs_2 file_path = 
  let file = open_in file_path in

  (* Read all lines *)
  let mat = ref [] in
  try
    while true do
      let line = input_line file in
      let mat_line = Array.of_seq (String.to_seq line) in
      mat := mat_line::!mat;
    done;
  with End_of_file -> ();
  close_in file;
  Array.of_list !mat
in

let is_num c =
  (Char.code c) >= Char.code '0' && (Char.code c) <= Char.code '9'
in

let part_2 matrix =
  let res = ref 0 in
  let cur_nums = ref [] in
  let buf = ref "" in

  for j = Array.length matrix.(0)-1 downto 0  do
    for i = Array.length matrix - 1 downto 0 do
      let c = matrix.(i).(j) in
      if is_num c then
        buf := String.concat "" [!buf; String.make 1 c]
      else if !buf <> "" then begin
        cur_nums := (int_of_string !buf) :: !cur_nums;
        buf := "";
      end;

      if c = '+' then begin
        res := !res + List.fold_left ( + ) 0 !cur_nums;
        cur_nums := []
      end else if c = '*' then begin
        res := !res + List.fold_left ( * ) 1 !cur_nums;
        cur_nums := []
      end
    done
  done;

  !res
in

let filename = "./inputs/6.txt" in
let numbers, ops = load_inputs_1 filename in
let matrix = load_inputs_2 filename in
let key_1 = part_1 numbers ops in
let key_2 = part_2 matrix in
Printf.printf "Part 1: %d\nPart 2: %d\n" key_1 key_2