# Lau Ming Hong 22079217D
# VS Code is used

import hashlib
import random
import os
# import string

global X, Y
global finalX, finalY
global attempts
finalX = ""
finalY = ""
X = ""
Y = ""
attempts = 0

def genRanString():
    length = random.randint(15, 25)
    return os.urandom(length).hex()

def find_collision():

    global X, Y, finalX, finalY, attempts

    full_name = "LauMingHong"
    student_id = "22079217d"

    flag = True
    attempts = 0

    # Generate X string with random string
    ran1 = genRanString()
    X = full_name + ran1

    # Generate Y string with random string
    ran2 = genRanString()
    Y = student_id + ran2

    hashX_values = {}
    hashY_values = {}

    # hashX = hashlib.sha256(X.encode()).hexdigest()
    
    while (flag == True):

        hashX = hashlib.sha256(X.encode()).hexdigest() 
        hashY = hashlib.sha256(Y.encode()).hexdigest() 

        hashX_Prefix = hashX[:11]
        hashY_Prefix = hashY[:11]

        hashX_values.update({hashX_Prefix: hashX})
        hashY_values.update({hashY_Prefix: hashY})

        attempts += 1
        print("Current attempt: ", attempts)
        # print("Current hash_X: ", hash_X)
        # print("Current hash_Y: ", hash_Y, "\n")

        if hashX_Prefix in hashX_values:
            if hashY_Prefix in hashY_values:
                if hashX_Prefix in hashY_values.keys():
                    finalX = hashX
                    finalY = hashY_values[hashX_Prefix]
                    print("Collision found in case 2.")
                    print("Name with random string: \t", X)
                    print("ID with random string: \t\t", Y)
                    return X, Y
                if hashX_Prefix == hashY_Prefix:
                    finalX = hashX
                    finalY = hashY
                    print("Collision found in case 1.")
                    print("Name with random string: \t", X)
                    print("ID with random string: \t\t", Y)
                    return X, Y
                if hashY_Prefix in hashX_values.keys():
                    finalY = hashY
                    finalX = hashX_values[hashY_Prefix]
                    print("Collision found in case 3.")
                    print("Name with random string: \t", X)
                    print("ID with random string: \t\t", Y)
                    return X, Y

        ran1 = genRanString()
        X = full_name + ran1

        ran2 = genRanString()
        Y = student_id + ran2
        
    ''' print("No collision found within the iterations.")
    return None '''

# Main program
collision_result = find_collision()
if collision_result is not None:
    print("hash_X:", finalX)
    print("hash_Y:", finalY)
    print("Final attempts: ", attempts)
''' else:
    print("No collision found.")'''