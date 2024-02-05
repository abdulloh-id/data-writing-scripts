How to write data to a file with a regular csv-writer: an alternative method

1. First of all, you need to import the CSV library. It is a built-in Python library.

2. Make sure that you have your data stored in lists.

3. Open a file using the 'with' keyword.
	1) Other lines in this writing block should be under this block. So you should indentate them inside the block.
	2) 'w' stands for writing.   
	3) You can set encoding too, as (encoding='utf-8').   
	4) You should add (newline='') to write data properly. Otherwise, it will write data to every other row.

4. You can create header names. But changing their order doesn't change the order in which the data is written.

5. Use a for-loop to iterate through lists and write data.   
	1) zip() can be used while iterating through multiple lists at once.   
	2) .writerow() method is the main character here. With it, you can manipulate which data should go under which header. In other words, you can set the order of writing data to columns.

6. Finally, you don't need to close the file with this method. Because the 'with' context manager automatically closes the file after writing the data.

