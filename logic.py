playerObject1 = [0, 0]
playerObject2 = [0, 0]
playerObject3 = [0, 0]
playerObject4 = [0, 0]
playerObject5 = [0, 0]

computerObject1 = [0, 0]
computerObject2 = [0, 0]
computerObject3 = [0, 0]
computerObject4 = [0, 0]
computerObject5 = [0, 0]

playerObject1[0] = int(input("Please enter the first object's x-coordinate.\n"))
playerObject1[1] = int(input("Please enter the first object's y-coordinate.\n"))

while playerObject1[0] > 5 or playerObject1[1] > 5:
    print("Error. Object coordinates can't be greater than 5.\n")
    playerObject1[0] = int(input("Please enter the first object's x-coordinate.\n"))
    playerObject1[1] = int(input("Please enter the first object's y-coordinate.\n"))
    
playerObject2[0] = int(input("Please enter the second object's x-coordinate.\n"))
playerObject2[1] = int(input("Please enter the second object's y-coordinate.\n"))

while playerObject2 == playerObject1:
    print("Error. Objects can't be equal to each other.\n")
    playerObject2[0] = int(input("Please enter the second object's x-coordinate.\n"))
    playerObject2[1] = int(input("Please enter the second object's y-coordinate.\n"))

while playerObject2[0] > 5 or playerObject2[1] > 5:
    print("Error. Object coordinates can't be greater than 5.\n")
    playerObject2[0] = int(input("Please enter the first object's x-coordinate.\n"))
    playerObject2[1] = int(input("Please enter the first object's y-coordinate.\n"))

playerObject3[0] = int(input("Please enter the third object's x-coordinate.\n"))
playerObject3[1] = int(input("Please enter the third object's y-coordinate.\n"))

while playerObject3 == playerObject2 or playerObject3 == playerObject1:
    print("Error. Objects can't be equal to each other.\n")
    playerObject3[0] = int(input("Please enter the third object's x-coordinate.\n"))
    playerObject3[1] = int(input("Please enter the third object's y-coordinate.\n"))

while playerObject3[0] > 5 or playerObject3[1] > 5:
    print("Error. Object coordinates can't be greater than 5.\n")
    playerObject3[0] = int(input("Please enter the first object's x-coordinate.\n"))
    playerObject3[1] = int(input("Please enter the first object's y-coordinate.\n"))

playerObject4[0] = int(input("Please enter the fourth object's x-coordinate.\n"))
playerObject4[1] = int(input("Please enter the fourth object's y-coordinate.\n"))

while playerObject4 == playerObject3 or playerObject4 == playerObject2 or playerObject4 == playerObject1:
    print("Error. Objects can't be equal to each other.\n")
    playerObject4[0] = int(input("Please enter the fourth object's x-coordinate.\n"))
    playerObject4[1] = int(input("Please enter the fourth object's y-coordinate.\n"))

while playerObject4[0] > 5 or playerObject4[1] > 5:
    print("Error. Object coordinates can't be greater than 5.\n")
    playerObject4[0] = int(input("Please enter the first object's x-coordinate.\n"))
    playerObject4[1] = int(input("Please enter the first object's y-coordinate.\n"))

playerObject5[0] = int(input("Please enter the fifth object's x-coordinate.\n"))
playerObject5[1] = int(input("Please enter the fifth object's y-coordinate.\n"))

while playerObject5 == playerObject4 or playerObject5 == playerObject3 or playerObject5 == playerObject2 or playerObject5 == playerObject1:
    print("Error. Objects can't be equal to each other.\n")
    playerObject4[0] = int(input("Please enter the fifth object's x-coordinate.\n"))
    playerObject4[1] = int(input("Please enter the fifth object's y-coordinate.\n"))

while playerObject5[0] > 5 or playerObject5[1] > 5:
    print("Error. Object coordinates can't be greater than 5.\n")
    playerObject5[0] = int(input("Please enter the first object's x-coordinate.\n"))
    playerObject5[1] = int(input("Please enter the first object's y-coordinate.\n"))

playerThrow = [0, 0]

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
