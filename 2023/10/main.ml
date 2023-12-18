let parse_input (path: string): (char array array) =
  let file = open_in path in 
  let lines = In_channel.input_lines file in 
  let li = (List.length lines) in 
  let lj = (match lines with a::_ -> String.length a | [] -> 0) in
  let matrix = Array.make_matrix li lj ' ' in 
  List.iteri (fun i str ->
    for j = 0 to lj -1 do 
      matrix.(i).(j) <- str.[j]
    done
  ) lines;
  matrix
in

(* affiche le plateau *)
let print_matrix (mat: char array array): unit =
  Array.iter (fun a -> begin
    Array.iter ( Printf.printf "%c" ) a;
    Printf.printf "\n"
  end) mat
in

let matrix_size (mat: char array array): int*int =
  assert (Array.length mat > 0);
  Array.length mat, Array.length mat.(0)
in

(* localise le charactère 'S' *)
let locate_begin (mat: char array array): int*int =
  let li, lj = ref 0, ref 0 in 
  Array.iteri (fun i arr -> 
    Array.iteri (fun j c ->
      if c = 'S' then begin
        li := i; lj := j 
      end) arr
   ) mat;
  !li, !lj
in

let neighbours (mat: char array array) (i: int) (j: int): (int*int) list =
  let connection_exists ni nj =
    match (ni, nj) with
    | (-1, 0) -> Array.exists (fun c -> c = mat.(ni+i).(nj+j)) [|'|'; '7'; 'S'; 'F'|]
    | (1, 0) -> Array.exists (fun c -> c = mat.(ni+i).(nj+j)) [|'|'; 'J'; 'S'; 'L'|]
    | (0, -1) -> Array.exists (fun c -> c = mat.(ni+i).(nj+j)) [|'-'; 'L'; 'S'; 'F'|]
    | (0, 1) -> Array.exists (fun c -> c = mat.(ni+i).(nj+j)) [|'-'; '7'; 'S'; 'J'|]
    | _ -> failwith "4rn0: bad delta"
  in
  let possible_neighbours c =
    match c with
    | '.' -> []
    | 'L' -> [(i-1, j); (i, j+1)]
    | 'J' -> [(i-1, j); (i, j-1)]
    | 'F' -> [(i, j+1); (i+1, j)]
    | '7' -> [(i, j-1); (i+1, j)]
    | '-' -> [(i, j+1); (i, j-1)]
    | '|' -> [(i-1, j); (i+1, j)]
    | 'S' -> [(i, j+1); (i-1, j); (i, j-1); (i+1, j)]
    | _ -> failwith "4rn0: char not supported"
  in
  let li, lj = matrix_size mat in 
  List.filter ( fun (ni, nj) ->
    (0 <= ni && ni < li && 0 <= nj && nj < lj) && (connection_exists (ni-i) (nj-j))
  ) (possible_neighbours mat.(i).(j))
in

let get_loop_dist (mat: char array array): (int*int*int) list =
  let (si, sj) = locate_begin mat in
  let (li, lj) = matrix_size mat in 
  let distances = Array.make_matrix li lj (-1) in
  let queue = Queue.create () in
  let loop = ref [] in 
  Queue.add (si, sj, 0) queue;
  (* parcours de la loop *)
  while not (Queue.is_empty queue) do 
    let i, j, d = Queue.pop queue in
    if distances.(i).(j) == -1 then begin
      loop := (i, j, d) :: !loop;
      distances.(i).(j) <- d;
      List.iter (fun (ni,nj) ->
        if distances.(ni).(nj) == -1 then 
          Queue.add (ni, nj, d+1) queue
      ) (neighbours mat i j)
    end
  done;
  !loop
in

let matrix = parse_input "input" in 
let loop = get_loop_dist matrix in 
let maxi = ref 0 in
List.iter (fun (i,j,d) ->
  maxi := max (!maxi) d
) loop;
Printf.printf "%d\n" !maxi