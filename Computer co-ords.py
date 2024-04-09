import random

# Establish blank player objects.
playerObject1 = [0, 0]
playerObject2 = [0, 0]
playerObject3 = [0, 0]
playerObject4 = [0, 0]
playerObject5 = [0, 0]

# Randomise computer objects 1 and 2.
computerX1 = random.randint(1, 5)
computerY1 = random.randint(1, 5)

computerX2 = random.randint(1, 5)
computerY2 = random.randint(1, 5)

# Error check for objects being equal to each other.
while computerX1 == computerX2 and computerY1 == computerY2:
    computerY2 = random.randint(1, 5)

# Randomise computer object 3.
computerX3 = random.randint(1, 5)
computerY3 = random.randint(1, 5)

# Error check for objects being equal to each other.
if computerX3 == computerX1:
    while computerY3 == computerY1:
        computerY3 = random.randint(1, 5)
if computerX3 == computerX2:
    while computerY3 == computerY2:
        computerY3 = random.randint(1, 5)
    
# Randomise computer object 4.
computerX4 = random.randint(1, 5)
computerY4 = random.randint(1, 5)

# Error check for objects being equal to each other.
if computerX4 == computerX1:
    while computerY4 == computerY1:
        computerY4 = random.randint(1, 5)
if computerX4 == computerX2:
    while computerY4 == computerY2:
        computerY4 = random.randint(1, 5)
if computerX4 == computerX3:
    while computerY4== computerY3:
        computerY4 = random.randint(1, 5)

# Randomise computer object 5.
computerX5 = random.randint(1, 5)
computerY5 = random.randint(1, 5)

# Error check for objects being equal to each other.
if computerX5 == computerX1:
    while computerY5 == computerY1:
        computerY5 = random.randint(1, 5)
if computerX5 == computerX2:
    while computerY5 == computerY2:
        computerY5 = random.randint(1, 5)
if computerX5== computerX3:
    while computerY5== computerY3:
        computerY5 = random.randint(1, 5)
if computerX5 == computerX4:
    while computerY5 == computerY4:
        computerY5 = random.randint(1, 5)
        
print(computerX1, computerY1)

print(computerX2, computerY2)

print(computerX3, computerY3)

print(computerX4, computerY4)

print(computerX5, computerY5)