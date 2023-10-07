### IF, ELIF AND ELSE FUNCTIONS IN PYTHON ###

      
  

x=(input("enter a name:"))


if len(x)<3:
    
    print("name can't be less than 3 characters!")


elif len(x)>50:
    
    print("name should be of maximum fifty characters!")

else:
    
    print("name looks good!")


y=int(input("enter your weight:"))

z=(input("lbs or kg:"))

if z in "lbs":
    
    print(f"Your converted weight: {y*0.45}")

elif z in "kg":
    
    print(f" Your converterd weight: {y/0.45}")
    
else:
    
    print("error!")
