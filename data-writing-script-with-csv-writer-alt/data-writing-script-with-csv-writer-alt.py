# Writing data to a file with a regular csv-writer: Alternative method

import csv

# Data stored in lists
cars = ['porsche', 'audi', 'bmw', 'nissan']
gadgets = ['phone', 'pc', 'tablet', 'smartwatch']
movies = ['scream', 'stab', 'final destination', 'harry potter']

# The 'with' context manager is used to handle opening and closing the file
with open('my_file.csv', 'w', encoding='utf-8', newline='') as file:

	# Declare a writer
	writer = csv.writer(file)

	# Header names
	writer.writerow(['Cars', 'Gadgets', 'Movies'])

	# Use for-loop to write the data
	for gadget, car, movie in zip(gadgets, cars, movies):
		writer.writerow([car, gadget, movie])
