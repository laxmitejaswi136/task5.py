# 1. Create a Python script that generates a tuple containing the names of 5 different cities
cities_tuple = ("Hyderabad", "Mumbai", "Bangalore", "Delhi", "Chennai")
print("1. Original Cities Tuple:", cities_tuple)
print("-" * 50)


# 2. Write a function that takes a tuple as an argument and returns the first and last elements of the tuple
def get_first_and_last(my_tuple):
    # Index 0 is the first element, index -1 is the last element
    return my_tuple, my_tuple[-1]

# Testing the function
first, last = get_first_and_last(cities_tuple)
print(f"2. First element: '{first}', Last element: '{last}'")
print("-" * 50)


# 3. Create a tuple of tuples, where each inner tuple contains a student's name and their corresponding grade
student_grades = (("John", 85), ("Alice", 92), ("Charlie", 78), ("Bob", 95))
print("3. Tuple of Tuples (Students & Grades):", student_grades)
print("-" * 50)


# 4. Implement a function that takes the tuple of tuples from the previous task 
# and returns a new tuple with the students' names sorted in alphabetical order
def get_sorted_student_names(students_tuple):
    names = []
    # Loop through the tuple of tuples to extract just the names
    for student in students_tuple:
        names.append(student)  # student contains the name
    
    # Sort the names alphabetically
    names.sort()
    
    # Convert the sorted list back into a tuple as requested
    return tuple(names)

# Testing the function
sorted_names = get_sorted_student_names(student_grades)
print("4. Sorted Student Names Tuple:", sorted_names)
print("-" * 50)


# 5. Practice tuple unpacking by writing a function that takes a tuple of 3 elements 
# and assigns each element to a separate variable, then prints out the values of these variables
def unpack_three_elements(three_elem_tuple):
    # Unpacking the tuple into three individual variables
    var1, var2, var3 = three_elem_tuple
    
    print("5. Inside unpacking function:")
    print("   Variable 1:", var1)
    print("   Variable 2:", var2)
    print("   Variable 3:", var3)

# Testing the unpacking function with a 3-element sample tuple
sample_tuple = ("Python", 2026, "Tuple Assignment")
unpack_three_elements(sample_tuple)