# test for timing the loop

out "Input^an^integer^:"
in a

let b 0

block loop
add b b 1
if b a final loop

block final
out b
exit
