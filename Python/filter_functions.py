import sys #System tools

def get_dimensions(): #Take the code in the def function
	try: #Variables with validation
		columns = int(input("Enter the number of columns:"))

		rows = int(input("Enter the number of rows:"))

	except ValueError: #Error checking
		print("incorrect input, only numbers can be entered")
		sys.exit() #Emergency completion

	if columns <= 0 or rows <= 0: #Checking for the correct number
		print("incorrect input, incorrect number entered")
		sys.exit() #Emergency completion

	return columns, rows #Function completion

def filter_even_numbers(columns, rows):
	numbers = [] #List numbers
	even_numbers = [] #List even numbers

	for i in range(0, columns * rows): #Cycle of adding numbers to a table and a range of numbers
		numbers.append(i) #Add the number i to the list
		if i % 2 == 0:
			even_numbers.append(i) #Add the even number i to the list

	return numbers, even_numbers

def print_statistics(numbers, even_numbers):
	percentage_even_numbers = len(even_numbers) / len(numbers) * 100  #The number of even numbers as a percentage
	average = sum(even_numbers) / len(even_numbers) #The arithmetic mean
	print(f"\n --- Statistics for Even Numbers ---\nCount of even numbers: {len(even_numbers)}\nPercentage of even numbers: {percentage_even_numbers:.2f}%\nSum of even numbers: {sum(even_numbers)}\nAverage of even numbers: {average}")

columns, rows = get_dimensions() #Function call
numbers, even_numbers = filter_even_numbers(columns, rows) #Function call

print(f"You entered: {columns} and {rows}")
print(f"All: {numbers}")
print(f"Evens: {even_numbers}")

print_statistics(numbers, even_numbers) #Function call