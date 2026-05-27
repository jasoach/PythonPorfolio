import random

x = random.randint(1,1000000000000)
print(f"The secret number is {x}")

def linear_search():
    global x
    c=0
    for guess in range (1,100000000000):
        c = c+1
        if guess == x:
            print(f"guess is {guess} it took {c} attempts")

def binary_search():
    global x
    low = 1
    high = 1000000000000
    found = False
    m=0
    while found == False:
        mid = (low+high)//2
        if mid == x:
            print(f"count is {mid} it took {m} tries")
            found = True
        else:
            if mid > x:
                high = mid - 1
                m=m+1
            else:
                low = mid +1
                m=m+1


binary_search()
