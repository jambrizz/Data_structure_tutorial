"""
In this example problem, we will be using sets to add, remove, check for membership, size of set.
You can copy and paste the code below to test out the code in your own environment.
"""

company_employees = set(["Mike", "Corey"])

# Create an add employee method to add employees to an existing set
def add_employee(set, employee):
    set.add(employee)

# Create a remove employee method to remove employees from an existing set
def remove_employee(set, employee):
    set.remove(employee)
    
# Create a method to check if an employee is in the set and return True if they are, False if they are not
def found_employee(set, employee):
    if employee in set:
        return True
    else:
        return False
    
# Create a method to return the size of the set
def size_of_set(set):
    return len(set)
    
print(company_employees)
add_employee(company_employees, "John")
print(company_employees)
remove_employee(company_employees, "Mike")
print(company_employees)
print(found_employee(company_employees, "Corey"))
print(found_employee(company_employees, "Joseph"))
print(size_of_set(company_employees))

"""
This part of the code is to show how to perform unions, intersections and differences.
You can copy and paste the code below to test out the code in your own environment.
"""

# Create a method to perform a union between two sets
def union(set1, set2):
    newSet = set()
    for x in set1:
        newSet.add(x)
    for x in set2:
        newSet.add(x)
    return newSet

# Create a method to perform an intersection between two sets
def intersection(set1, set2):
    newSet = set()
    for x in set1:
        if x in set2:
            newSet.add(x)
    return newSet

# Create a method to perform a difference between two sets
def difference(set1, set2):
    newSet = set()
    for x in set1:
        if x not in set2:
            newSet.add(x)
    for x in set2:
        if x not in set1:
            newSet.add(x)
    return newSet

employees_site_1 = set(["Mike", "Corey", "John", "Matt"])
employees_site_2 = set(["Matt", "Luis", "John", "Corey"])

print(union(employees_site_1, employees_site_2))
print(intersection(employees_site_1, employees_site_2))
print(difference(employees_site_1, employees_site_2))