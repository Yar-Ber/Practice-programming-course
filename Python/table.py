import sys #System tools

try: #Variables with validation
	columns = int(input("Enter the number of columns:"))

	rows = int(input("Enter the number of rows:"))

except ValueError: #Error checking
	print("incorrect input, only numbers can be entered")
	sys.exit() #Emergency completion

if columns <= 0 or rows <= 0: #Checking for the correct number
	print("incorrect input, incorrect number entered")
	sys.exit() #Emergency completion

total_sum = 0

for i in range(0, columns * rows): #Cycle of adding numbers to a table and a range of numbers
	print(f"{i : 5}", end="")
	if ((i + 1) % columns == 0): #Checking for moving to a new row
		print()
	total_sum += i #Calculating the total sum of the numbers

average = total_sum/(columns * rows) #Calculating the arithmetic mean
print(f"The arithmetic mean: {average}")