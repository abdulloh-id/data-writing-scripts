# Writing data to a file with the DictWriter class: An alternative method

import csv

# Data stored in lists
cars = ['porsche', 'audi', 'bmw', 'nissan']
gadgets = ['phone', 'pc', 'tablet', 'smartwatch']
movies = ['scream', 'stab', 'final destination', 'harry potter']

# Create/Open a file using the 'with' context manager
with open('my_file.csv', 'w', encoding='utf-8', newline='') as file:
	
	# Set the header names and their order
	headers = ['Gadgets', 'Movies', 'Cars']
	
	# Declare a DictWriter object
	my_writer = csv.DictWriter(file, fieldnames = headers)

	# Assign the headers
	my_writer.writeheader() # writes headers as the initial line

	# Use for-loop to write the data
	for car, movie, gadget in zip(cars, movies, gadgets):
		my_writer.writerow({
							'Cars': car,
							'Gadgets': gadget,
							'Movies': movie
							})
