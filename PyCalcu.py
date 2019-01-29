# ================ PyCalcu by Flipp3rrr ================

# Basic information and help
print("Starting PyCalcu...")
print("Done!")
print()
print("For basic syntax help, type \"Functions\".")
print("For a list of commands, type \"Advanced functions\".")
print("Type the wanted function")

# Main loop
while True:

	# Main variable
	input_var = input("> ")

	# Function help
	if input_var == "Functions":
		print("The basic functions of this program are:")
		print("1. Add")
		print("2. Substract")
		print("3. Multiply")
		print("4. Divide")
		print()
		print("To use a function you can either use the number or name.")

	# Advanced functions help
	else if input_var == "Advanced functions":
		print("For more advanced function you got the following possibilities:")
		print("5. None")
		print("6. None")
		print("7. None")

	# Add function
	else if input_var == "Add" or input_var == "1":
		num1 = int(input("First number > "))
		num2 = int(input("Second number > "))
		print(num1, "+", num2, "=", add(num1,num2))
