
### IMAGE FILES IN PYTHON ###
  
  
f=open("300A7659.JPG","rb") 

f1=open("legend.JPG","wb")

for i in f:
    f1.write(i)
