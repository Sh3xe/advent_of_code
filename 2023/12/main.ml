
let parse_input path = 
  let parse_line line =
    let split = String.split_on_char ' ' line in 
    match split with
    | spring::rest::[] ->
      (spring, List.map int_of_string (String.split_on_char ',' rest))
    | _ -> failwith "invalid input"
  in
  let file = open_in path in 
  let lines = In_channel.input_lines file in 
  close_in file;
  List.map parse_line lines
in 

let unfold_spring spring_data =
  let spring, nums = spring_data in 
  let str = String.concat "?" [spring] in
  (* code de débile *)
  let unfolded_str = String.concat spring [str; str; str; str] in 
  let unfolded_nums = List.concat [nums; nums; nums; nums; nums] in 
  (* fin de: code de débile *)
  (unfolded_str, unfolded_nums)
in

let springs_data = List.map unfold_spring (parse_input "test_input") in 
();;