out "Input^the^1st^term^:"
in a

out "Input^the^2nd^term^:"
in b

out "Input^the^number^of^terms^:"
in n

# wrong input...
if<= n 0 A1 A2

block A1
out "Number^of^terms^should^be^bigger^than^zero!"
exit

block A2
if n 1 B1 B2

block B1
out a
exit

block B2
if n 2 C1 C2

block C1
out a
out b
exit

block C2
out a
out b
let i 2

block loop
add i i 1
let temp b
add b a b
let a temp
out b
if i n final loop

block final
exit
