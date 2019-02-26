while True:
	print("Choose Any Options :")
	print("1.Type add for addition")
	print("2.Type sub for substraction")
	print("3.Type mult for multlipication")
	print("4.Type div for division")
	print("5.Type quit for exiting")
	user_ip=input("enter corresponding numbers or options: ")
	if user_ip=="quit" or user_ip=="5":
		break
	elif user_ip=="add" or user_ip=="1":
		n1=float(input("another number : "))
		n2=float(input("another number : "))
		print(n1+n2)
	elif user_ip=="sub" or user_ip=="2":
		n1=float(input("Enter the number to be substracted : "))
		n2=float(input("Enter the number to be substracted from : "))
		print(n1-n2)
	elif user_ip=="mult" or user_ip=="3":
		n1=float(input("Enter a number : "))
		n2=float(input("Enter another number : "))
		print(n1*n2)
	elif user_ip=="div" or user_ip=="4":
		n1=float(input("enter the dividend : "))
		n2=float(input("enter the divisor : "))
		print(n1/n2)
print("Program exited")