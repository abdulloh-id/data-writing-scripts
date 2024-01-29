How to write data to a file with a regular csv-writer

1. First of all, you need to import the CSV library. It's a built-in Python library for working with CSV files.

2. Make sure that you have your data stored in lists.

3. Create a new file for writing.
   1) 'w' stands for writing.
   2) You can set encoding too, as (encoding='utf-8').
   3) You should add (newline='') to write data properly. Otherwise, it will write data to every other row.

4. You can create header names. But changing the order of headers doesn't change the order in which the data is written.

5. Use a for-loop to iterate through lists and write data.
   1) zip() can be used while iterating through multiple lists at once.
   2) .writerow() method is the main character here. With it, you can manipulate which data should go under which header. In other words, you can set the order of writing data to columns.

6. Finally, close the file with the .close() method. This will save it too.
