###### August 25, 2022
###### Foundations of Programming: Python
###### Assignment 07
###### (repo)[https://github.com/kbev12/IntroToProg-Python-Mod07]

# To Do Script

## Introduction

	For assignment 07 for the class Foundations of Programming: Python I worked on a python script that pickles a file, loads and prints the unpickled file, and ends the program.
Creating the Script

## Pickling
	The script begins with importing the pickle module and declaring the variables (Figure 1). 
 ![pickle](https://user-images.githubusercontent.com/110877101/186582331-e6d3a40a-7a43-4c4d-970c-2ddced25b463.JPG)
Figure 1. Importing pickle module and declaring the program variables

	I started creating the script (Figure 2) by taking a string input for a task, int input for the priority, and assigning them to a dictionary.  I created a function to append to ‘to_do.txt in binary. Using pickle.dump the to_do object is serialized to obj_file. The function loadData unpickles todo.txt by opening the file in read binary and loading the file to the variable obj_file_data.
![pickle](https://user-images.githubusercontent.com/110877101/186581619-81ab7843-4b92-482a-88a2-ad7a83febe2c.JPG)
Figure 2. Pickling and unpickling todo.txt
## Exceptions
	To enhance the script I updated the loadData function to printData function to add in a try/except (Figure 3). The function still opens todo.txt in read binary but now it loads each line and prints it to the terminal. Except once it receives an End of File error it prints ‘End of File’ and then closes the file.
  ![trycatch](https://user-images.githubusercontent.com/110877101/186581886-ab204ced-f3dd-4f9b-9453-2d2ceadc1ba9.JPG)
  Figure 3. Try/catch for printing rows of data
## End of Script
The script ends by asking the user to press enter to end the program. (Figure 4) Each of the functions are called in order. 
![eof](https://user-images.githubusercontent.com/110877101/186582246-b28ea1d1-08b3-4ff7-9e36-8bcaa248778a.jpg) 
Figure 4 Program ends with user’s input
## Testing the Script	
	I tested the program in both PyCharm and in the command prompt and it successfully completed using both (Figure 5).
 ![test](https://user-images.githubusercontent.com/110877101/186582365-b82edf15-d30e-4301-8678-dce90b9df793.JPG)
Figure 5. Testing the program

The script successfully ran and updated the text file todo.txt (Figure 6).
 ![binary](https://user-images.githubusercontent.com/110877101/186582395-af356e27-aab4-4fb6-b8ab-0f40199441be.JPG)

Figure 6. Updated todo.txt


## Summary

	For Foundations of Programming: Python seventh assignment I worked on a python script that pickles a file, loads and prints the unpickled file, and ends the program.
