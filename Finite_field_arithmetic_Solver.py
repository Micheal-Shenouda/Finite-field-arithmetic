#!/bin/python3
import binascii

###########################################################################
# Mechanism: 1)Read a finite-polynomial-field file                        #
#            2)Filter string "poly" to array "index" with x indexes       #
#            3)Convert all strings in "index" into int                    #
#            4)Check if the last term was constant, Then reassign it as 0 #
#            5)Convert "index" into binary code in "bin" string           #
#            6)Convert binary code  into ascii characters                 #
###########################################################################


# 1)Read a finite-polynomial-field file 
file = open('data.txt', 'r')
poly = file.read()


# 2)Filter string "poly" to array "index" with x indexes
poly = poly[4:] 
poly = poly.replace('x^', '')
index = poly.split(" + ")


# 3)Convert all strings in "index" into int
index = [eval(i) for i in index]


# 4)Check if the last term was constant, Then reassign it as 0
                    ##################
                    # DO IT MANUALLY #
                    ##################  
index[-1] = 0


# 5)Convert "index" into binary code in "bin" string
bin = ""
i = iter(index)
current_iterator = next(i)

for num in range(index[0], 0, -1):
    if current_iterator == num:
        bin += "1"
        current_iterator = next(i)  # Get the next iterator
        continue

    bin += "0"

#################
#    CAUTION    #
#################
# If the last term wasn't constant, you must remove the next line
bin += "1" 


# 6)Convert binary code  into ascii characters
bin = int(bin, 2)
print(binascii.unhexlify('%x' % bin).decode())
