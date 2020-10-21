import random
import time
print("welcome to the guessing game")
print("you have to guess a no. between 1-10")
print("you have 3 chance to guess correct no.")
secret_number= random.randint(1,10)
guess_count  = 0
guess_limit  = 5

while guess_count < guess_limit:
    guess = int(input("guess: "))
    guess_count+=1
    if guess == secret_number:
        print("You won!!")
        break
    print("try again")
else:
    print(" you lost ;( \n coreect no. is:")
    print(secret_number)
    print("bye \ngame would be closed in 5 second")
    time.sleep(5)