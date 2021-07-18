import random 
print("#---------------#\n|GUESS THE NUMBER|\n#---------------#\n")
print("Range of random numbers.\n")
start = int(input("start no:"))
end = int(input("end no:"))
n = random.randint(start,end)
print("\n")
while True:
    g = int(input("no:"))
    if g>n:
        print("try a lower no. ")
    elif g<n:
        print("go a little higher ")
    else:
        print("right on! well done!")
