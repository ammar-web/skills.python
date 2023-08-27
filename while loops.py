### WHILE LOOPS IN PYTHON ###


secret_number=14

guess_count=0

guess_limit=3

while guess_count < guess_limit:
    guess=int(input("guess:"))
    guess_count+=1

if guess==secret_number:
        print("you won")

else:print("you loose")
