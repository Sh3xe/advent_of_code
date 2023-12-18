
let rec convert_line line = 
  List.map int_of_string (String.split_on_char ' ' line)
in

let parse_input (path: string) =
  let file = open_in path in 
  let lines = ref [] in
  let _ = try
    while true do
      let line = input_line file in
      lines := line :: !lines;
    done
  with e -> begin
    close_in file
  end in
  List.map convert_line !lines
in

let lst = parse_input "input2" in 
List.iter (fun x -> List.iter (fun y -> Printf.printf "%d " y) x) lst