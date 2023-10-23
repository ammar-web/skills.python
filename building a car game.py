### BUILDING A CAR GAME USING PYTHON ###

for i in range(2):
 
    info=input(">")

 
    if info=="help":
        
        print('''Start- To start the car
Stop- To stop a car
Quit-To exit''')

        break

    elif info!="help":
        
        print("I don't undestand that...")
        
        break

for j in range(3):

    command = input(">")

    if command=="start":
        
        print("car started to move...")
        
        break

    elif command=="stop":
        
        print("car has stopped moving...")
        
        break

    elif command=="quit":
        
        print("you are returned to the main menu...")
     
        break
