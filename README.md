Finite field arithmetic is a kind of cryptography, This script decode the crypto within few steps:

1)Read a finite-polynomial-field file
2)Filter string "poly" to array "index" with x indexes
3)Convert all strings in "index" into int
4)Check if the last term was constant, Then reassign it as 0
5)Convert "index" into binary code in "bin" string
6)Convert binary code into ascii characters

example of Finite field arithmetic: polycrypto from CTFlearn.com
