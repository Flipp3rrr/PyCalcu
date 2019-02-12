# ================ PyCalcu by Flipp3rrr ================

# Basic information and help
print("Welcome to PyCalcu. Type \"Help\" or \"1\" to get started.")

# Main loop
while True:

	# Main variable
	input_var = input("> ")

	# Function help
	if input_var == "Help" or input_var == "1":
		print("The basic functions of this program are:")
		print("1. Help")
		print("2. Advanced help")
		print("3. Add")
		print("4. Subtract")
		print("5. Multiply")
		print("6. Divide")
		print("")
		print("To use a function you can either use the number or name.")

	# Advanced functions help
	elif input_var == "Advanced help" or input_var == "2":
		print("For more advanced function you got the following possibilities:")
		print("7. Percents")
		print("8. None")
		print("9. None")

	# Add function
	elif input_var == "Add" or input_var == "3":
		num1 = int(input("Starting number > "))
		num2 = int(input("How many do you want to add to ", num1, "? > "))
		print(num1, "+", num2, "=", num1 + num2)

	# Subtract function
	elif input_var == "Subtract" or input_var == "4":
		num1 = int(input("Starting number > "))
		num2 = int(input("How many do you want to subtract from ",num1, "? > "))
		print(num1, "-", num2, "=", num1 - num2)

	# Multiply function
	elif input_var == "Multiply" or input_var == "5":
		num1 = int(input("Starting number > "))
		num2 = int(input("By how many do you want to multiply ", num1, "? > "))
		print(num1, "-", num2, "=", num1 * num2)

	# Divide function
	elif input_var == "Divide" or input_var == "6":
		num1 = int(input("Starting number > "))
		num2 = int(input("By how many do you want to divide ", num1, "? > "))
		print(num1, "-", num2, "=", num1 / num2)

	# Invalid function reporter
	else:
		print("Error! ", input_var, " isn't a valid function!")
