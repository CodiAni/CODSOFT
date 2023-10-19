print( "    WELCOME TO CALCULATOR    ")
a=int(input(" Number1 -> "))
b=input(" Operation -> ")
c=int(input(" Number2 -> "))
print(a,b,c)
if b== "+":
	print("Addition =",a+c)
elif b=="-":
	print("Substraction =",a-c)
elif b=="//":
	print("=",a//c)
elif b=="x":
	print("=",a*c)
elif b=="%":
    print("=",a%c)
else:
	print(" INVALID CHOICE : PLEASE enter operations like +,-,//,×,%")