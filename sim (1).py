import random

#initial conditions
finish_line = 50  #Finish Line
tortoise_pos = 0  #Starting Position
hare_pos = 0		 #Starting Position
is_hare_asleep = False #Hare starts Awake
count1=0
count2=0
count3 = 0

#simulations loop
for i in range(100000):
    while tortoise_pos < finish_line and hare_pos < finish_line:
        tortoise_pos = tortoise_pos+random.randint(1,3)
        x = random.randint(1,9)
        if x <=5:
            is_hare_asleep = True
        else:
            is_hare_asleep = False
        if is_hare_asleep == False:
            hare_pos = hare_pos + random.randint(1,5)
        if tortoise_pos >= 50 or hare_pos >=50:
            if tortoise_pos == hare_pos:
                count3 = count3+1
            elif tortoise_pos > hare_pos:
                count1 = count1+1
            elif hare_pos > tortoise_pos:
                count2 = count2+1
    tortoise_pos = 0
    hare_pos = 0
    is_hare_asleep = False

print(f"tortoise won {count1} times ")
print(f"hare won {count2} times ")
print(f"tie {count3} times")
