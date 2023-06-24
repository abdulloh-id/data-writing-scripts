# Writing data to a file with a regular csv-writer

import csv

# Data stored in lists
cars = ['porsche', 'audi', 'bmw', 'mustang']
gadgets = ['phone', 'pc', 'tablet', 'smartwatch']
movies = ['scream', 'stab', 'final destination', 'harry potter']

# Create a file
file = open('my_file.csv', 'w', encoding='utf-8', newline='')

writer = csv.writer(file)

# Header names
writer.writerow(['Cars', 'Gadgets', 'Movies'])

# Use for-loop to write the data
for gadget, car, movie in zip(gadgets, cars, movies):
	writer.writerow([car, gadget, movie])

# Close the file
file.close()