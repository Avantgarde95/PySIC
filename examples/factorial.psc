out "Input^an^integer^:"
in n

if< n 0 case_1 case_2

block case_1
out "Input^a^non-negative^number!"
exit

block case_2
if n 0 case_3 case_4

block case_3
out 1
exit

block case_4
let f 1
let d 1
block loop
mul f f d
add d d 1
if> d n final loop

block final
out f
exit
