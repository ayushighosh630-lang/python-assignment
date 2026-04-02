import csv

file_name = "data.csv"

with open(file_name, 'r') as file:
    reader = csv.reader(file)
    row_count = 0
    # The loop MUST be indented inside the 'with' block
    for row in reader:
        row_count += 1

print("Total no of rows in csv:", row_count)