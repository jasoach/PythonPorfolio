#slots
# creates a slot machine

import random

m=0
slots = ["7", "♢" , "♡", "♣"]
rolled = []
def spin():
    global m
    x=random.choices(slots, weights = [5,30,30,35], k=3)
    print(x)
    rolled.append(x)
    if x == ["7","7","7"]:
        print("Holy lucky jackpot, you won big, 500 big nolans")
        m = m + 500
        rolled.clear()
    elif x == ["♢","♢","♢"] or x == ["♡","♡","♡"] or x == ["♣","♣","♣"]:
        print("good match, +100 nolans")
        m = m + 100
        rolled.clear()
    else:
        print("womp")
        rolled.clear()
def cont():
    global m
    while True:
        nolan = input("What would you like to do next? Deposit, View_Funds, Spin, Cashout: ").lower()
        if nolan == "spin":
            if m>= 10:
                m=m-10
                print("good choice")
                spin()
            if m < 10:
                print("insufficient funds, please insert credits")
        elif nolan == "deposit":
            dep = input("how much would you like to deposit? 20, 50, 100: ")
            if dep == "20" or dep == "50" or dep == "100":
                m = m+int(dep)
                print(f"You have {m} nolan coins")
            else:
                print("not a valid amount, please try again")
        elif nolan == "view_funds":
            print(f"You have {m} nolan coins")
        elif nolan == "cashout":
            print(f"you have cashed out {m} nolan coins")
            break
        else:
            print("not a valid choice, please try again.")

def simulation():
    global m
    for i in range(1000):
        spin()
        m=m-10
    print(f" you are left with {m} nolan coins...")

simulation()


