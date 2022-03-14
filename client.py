import random

#no duplicate digits
unique = True 

print("[guess 'q' to exit]")
print("[guess 'ans' for answer]")
print(f"[unique is {unique}]")

#Get number of digits
while True:
    try:
        digits = int(input("How many digits: "))
        if digits > 8 or digits < 1:
            print("improper digit amount")
            continue
        break
    except:
        print("Enter an integer value")


lower_bound = 10**(digits-1)
upper_bound = (10**digits)-1

#randomly generate computer's number (the one being guessed)
if not unique:
    comp_num = str(random.randint(lower_bound, upper_bound))
else:
    while True:
        comp_num = str(random.randint(lower_bound, (10**digits)-1))
        if len(comp_num) == len(set(comp_num)):
            break

#prints to stdout and logs to file
def printl(string):
    print(string)
    log.write(string+"\n")

log = open("bic_log.txt", "a+")

tries = 0

while True:
    while True:
        guess = input("Guess: ")
        try:
            guess = int(guess)
        except:
            if "q" in guess:
                printl("bye")
                log.close()
                exit()
            if guess == "ans":
                print("Wow you sold out ... tsktsktsk")
                printl(f"Answer was {comp_num}")
                log.close()
                exit()
            printl("Guess an integer")
            continue
        
        if not(lower_bound > guess or guess > upper_bound):
            guess = str(guess)
            break
        else:
            printl(f"Guess a number between {lower_bound} and {upper_bound}")
    
    tries += 1

    c_count = 0
    b_count = 0

    for g in guess:
        if g in comp_num:
            c_count += 1

    for g, r in zip(guess, comp_num):
        if g == r:
            b_count += 1
            c_count -= 1

    printl(f"C: {c_count} | B: {b_count}")
    if b_count == digits:
        printl("----You win!----")
        break

log.close()
