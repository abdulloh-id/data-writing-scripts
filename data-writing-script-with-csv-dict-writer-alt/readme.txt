How to write data to a file using the DictWrite class: An alternative method 

1. First of all, you need to import the CSV library. It is a built-in Python library.

2. Make sure that you have your data stored in lists.

3. Create/Open a file using the 'with' context manager. It will be responsible for the opening and closing of the file.
    1) 'w' parameter stands for writing.
    2) You can set encoding too, as (encoding='utf-8').
    3) You should add (newline='') to write data properly. Otherwise, it will write data to every other row.

4. You can create header names as a simple list of strings.
   In order to manipulate the order of the columns, you just need to change the order of the headers.

5. Declare a new DictWrite object and pass which file you are writing and header names as fieldnames as parameters.
   This object will be responsible for writing data to the file.

6. Assign the headers with .writeheader() method. If you don't do this, headers won't be written.

7. Use a for-loop to iterate through lists and write data.
    1) zip() can be used while iterating through multiple lists at once.
    2) .writerow() method is used to write data to the file, but it cannot affect the order of columns.
