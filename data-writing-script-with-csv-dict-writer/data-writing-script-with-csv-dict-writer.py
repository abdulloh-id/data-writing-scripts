# Writing data to a file using the DictWriter class

import csv

# Data stored in lists
cars = ['porsche', 'audi', 'bmw', 'nissan']
gadgets = ['phone', 'pc', 'tablet', 'smartwatch']
movies = ['scream', 'stab', 'final destination', 'harry potter']

# Create a file
file = open('my_file.csv', 'w', encoding='utf-8', newline='')

# Set the header names and their order
headers = ['Movies', 'Cars', 'Gadgets']

# Declare a DictWriter object
my_writer = csv.DictWriter(file, fieldnames = headers)

# Assign the headers 
my_writer.writeheader() # Writes the headers as the initial line

# Use for-loop to write the data
for car, gadget, movie in zip(cars, gadgets, movies):
  my_writer.writerow({
                      'Cars': car,
						          'Gadgets': gadget,
						          'Movies': movie
						          })
  
# Close the file
file.close()
