import random

# Establish blank player objects.
playerObject1 = [0, 0]
playerObject2 = [0, 0]
playerObject3 = [0, 0]
playerObject4 = [0, 0]
playerObject5 = [0, 0]

# Randomise computer objects 1 and 2.
computerObject1 = [random.randint(1, 5), random.randint(1, 5)]
computerObject2 = [random.randint(1, 5), random.randint(1, 5)]

# Error check for objects being equal to each other.
while computerObject2 == computerObject1:
    computerObject2 = [random.randint(1, 5), random.randint(1, 5)]

# Randomise computer object 3.
computerObject3 = [random.randint(1, 5), random.randint(1, 5)]

# Error check for objects being equal to each other.
while computerObject3 == computerObject2 or computerObject3 == computerObject1:
    computerObject3 = [random.randint(1, 5), random.randint(1, 5)]

# Randomise computer object 4.
computerObject4 = [random.randint(1, 5), random.randint(1, 5)]

# Error check for objects being equal to each other.
while computerObject4 == computerObject3 or computerObject4 == computerObject2 or computerObject4 == computerObject1:
    computerObject4 = [random.randint(1, 5), random.randint(1, 5)]

# Randomise computer object 5.
computerObject5 = [random.randint(1, 5), random.randint(1, 5)]

# Error check for objects being equal to each other.
while computerObject5 == computerObject4 or computerObject5 == computerObject3 or computerObject5 == computerObject2 or computerObject5 == computerObject1:
    computerObject5 = [random.randint(1, 5), random.randint(1, 5)]

# Ask for first player object's coordinates.
playerObject1[0] = int(input("Please enter the first object's x-coordinate.\n"))
playerObject1[1] = int(input("Please enter the first object's y-coordinate.\n"))

# Error check for correct coordinates.
while playerObject1[0] > 5 or playerObject1[1] > 5 or playerObject1[0] < 1 or playerObject1[1] < 1:
    print("Error. Object coordinates must be between 1 and 5.\n")
    playerObject1[0] = int(input("Please enter the first object's x-coordinate.\n"))
    playerObject1[1] = int(input("Please enter the first object's y-coordinate.\n"))
    
# Ask for second player object's coordinates.
playerObject2[0] = int(input("Please enter the second object's x-coordinate.\n"))
playerObject2[1] = int(input("Please enter the second object's y-coordinate.\n"))

# Error check for objects being equal to each other.
while playerObject2 == playerObject1:
    print("Error. Objects can't be equal to each other.\n")
    playerObject2[0] = int(input("Please enter the second object's x-coordinate.\n"))
    playerObject2[1] = int(input("Please enter the second object's y-coordinate.\n"))

# Error check for correct coordinates.
while playerObject2[0] > 5 or playerObject2[1] > 5 or playerObject2[0] < 1 or playerObject2[1] < 1:
    print("Error. Object coordinates must be between 1 and 5.\n")
    playerObject2[0] = int(input("Please enter the first object's x-coordinate.\n"))
    playerObject2[1] = int(input("Please enter the first object's y-coordinate.\n"))

# Ask for third player object's coordinates.
playerObject3[0] = int(input("Please enter the third object's x-coordinate.\n"))
playerObject3[1] = int(input("Please enter the third object's y-coordinate.\n"))

# Error check for objects being equal to each other.
while playerObject3 == playerObject2 or playerObject3 == playerObject1:
    print("Error. Objects can't be equal to each other.\n")
    playerObject3[0] = int(input("Please enter the third object's x-coordinate.\n"))
    playerObject3[1] = int(input("Please enter the third object's y-coordinate.\n"))

# Error check for correct coordinates.
while playerObject3[0] > 5 or playerObject3[1] > 5 or playerObject3[0] < 1 or playerObject3[1] < 1:
    print("Error. Object coordinates must be between 1 and 5.\n")
    playerObject3[0] = int(input("Please enter the first object's x-coordinate.\n"))
    playerObject3[1] = int(input("Please enter the first object's y-coordinate.\n"))

# Ask for fourth player object's coordinates.
playerObject4[0] = int(input("Please enter the fourth object's x-coordinate.\n"))
playerObject4[1] = int(input("Please enter the fourth object's y-coordinate.\n"))

# Error check for objects being equal to each other.
while playerObject4 == playerObject3 or playerObject4 == playerObject2 or playerObject4 == playerObject1:
    print("Error. Objects can't be equal to each other.\n")
    playerObject4[0] = int(input("Please enter the fourth object's x-coordinate.\n"))
    playerObject4[1] = int(input("Please enter the fourth object's y-coordinate.\n"))

# Error check for correct coordinates.
while playerObject4[0] > 5 or playerObject4[1] > 5 or playerObject4[0] < 1 or playerObject4[1] < 1:
    print("Error. Object coordinates must be between 1 and 5.\n")
    playerObject4[0] = int(input("Please enter the first object's x-coordinate.\n"))
    playerObject4[1] = int(input("Please enter the first object's y-coordinate.\n"))

# Ask for fifth player object's coordinates.
playerObject5[0] = int(input("Please enter the fifth object's x-coordinate.\n"))
playerObject5[1] = int(input("Please enter the fifth object's y-coordinate.\n"))

# Error check for objects being equal to each other.
while playerObject5 == playerObject4 or playerObject5 == playerObject3 or playerObject5 == playerObject2 or playerObject5 == playerObject1:
    print("Error. Objects can't be equal to each other.\n")
    playerObject4[0] = int(input("Please enter the fifth object's x-coordinate.\n"))
    playerObject4[1] = int(input("Please enter the fifth object's y-coordinate.\n"))

# Error check for correct coordinates.
while playerObject5[0] > 5 or playerObject5[1] > 5 or playerObject5[0] < 1 or playerObject5[1] < 1:
    print("Error. Object coordinates must be between 1 and 5.\n")
    playerObject5[0] = int(input("Please enter the first object's x-coordinate.\n"))
    playerObject5[1] = int(input("Please enter the first object's y-coordinate.\n"))

# Establish player throw.
playerThrow = [0, 0]

# Check if player throw matches computer objects.
if playerThrow == computerObject1:
    print("Object 1 hit.")
elif playerThrow == computerObject2:
    print("Object 2 hit.")
elif playerThrow == computerObject3:
    print("Object 3 hit.")
elif playerThrow == computerObject4:
    print("Object 4 hit.")
elif playerThrow == computerObject5:
    print("Object 5 hit.")
else:
    print("Miss.")
