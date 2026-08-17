# Number Pyramid & Analysis Program

rows = int(input("Enter the number of rows: "))

total_numbers = 0
total_sum = 0

print("\nNumber Pyramid:")

for i in range(1, rows + 1):
    for j in range(1, i + 1):

        # Skip numbers greater than 9
        if j > 9:
            continue

        # Stop the row if the number is 10
        if j == 10:
            break

        print(j, end=" ")
        total_numbers += 1
        total_sum += j

    print()

print("\nAnalysis:")
print("Total numbers:", total_numbers)
print("Sum of numbers:", total_sum)
