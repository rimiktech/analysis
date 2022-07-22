#Write the program to Creating BMI Calculator?[BMI-Body Mass Index]
H=float(input("enter the your H in cm: "))
W=float(input("enter the your W in kg: "))
H=H/100
BMI=W/(H*H)
print("your Body Mass Index is : ",BMI)
if(BMI>0):
    if(BMI<=16):
        print("you are severely underweight")
    elif(BMI<=18):
        print("you are underweight")
    elif(BMI<=25):
        print("you are healthy")
    elif(BMI<=30.5):
        print("you nare overweight")
    else: print("you are severly overweight")
else:("enter valid details")                    

