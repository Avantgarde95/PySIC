# start
out "Input^a^number^:"
in N
out "Primes^(in^[1,^n])^:"

let n 1

# main loop
block main
if< n N call quit

block call
add n n 1
goto is_prime

block quit
exit

# --------------------------
# function
block is_prime

# base case (n < 2)
block case_1
if< n 2 fail case_2

# another base case (n = 2)
block case_2
if n 2 success general

# general case (n > 2)
block general
let d 2
goto loop

block loop
if d n success continue
block continue
div q n d
mul n_cmp q d
add d d 1
if n n_cmp fail loop

block success
out n
goto main

block fail
goto main
# --------------------------
