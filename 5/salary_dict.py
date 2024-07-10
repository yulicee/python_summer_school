# Initialize a dictionary with at least 5 employees and their salaries
employee_salaries = {
    'Alice': 30000,
    'Bob': 70000,
    'Jane': 120000,
    'John': 50000,
    'Caroline': 40000
}

# Print the initial dictionary
print("Initial employee data: ")
for employee, salary in employee_salaries.items():
    print(f"{employee}: ${salary}")

# Prompt user to add a new employee and their salary to the dictionary
new_employee = input("\nEnter the name of the new employee: ")
new_salary = int(input(f"Enter the salary for {new_employee}: "))
employee_salaries[new_employee] = new_salary

# Print the updated dictionary of employee data
print("\nUpdated employee information: ")
for employee, salary in employee_salaries.items():
    print(f"{employee}: ${salary}")

# Prompt user to update the salary for an existing employee
update_employee = input("\nEnter the name of the employee whose salary will be updated: ")
if update_employee in employee_salaries:
    updated_salary = int(input(f"Enter the new salary for {update_employee}: "))
    employee_salaries[update_employee] = updated_salary
else:
    print(f"{update_employee} not found in the employee list.")

# Prompt user to remove an employee from the list
remove_employee = input("\nEnter the name of the employee you want to remove: ")
if remove_employee in employee_salaries:
    del employee_salaries[remove_employee]
else:
    print(f"{remove_employee} not found in the employee list.")

# Calculate and print average salary of the employees
average_salary = sum(employee_salaries.values()) / len(employee_salaries)
print(f"\nThe average salary of the employees is: ${average_salary:.2f}")

# Find and print the employee(s) with the highest and lowest salaries
highest_salary = max(employee_salaries.values())
lowest_salary = min(employee_salaries.values())

highest_salary_employees = [employee for employee, salary in employee_salaries.items() if salary == highest_salary]
lowest_salary_employees = [employee for employee, salary in employee_salaries.items() if salary == lowest_salary]

print("\nEmployee(s) with the highest salary: ")
for employee in highest_salary_employees:
    print(f"{employee}: ${highest_salary}")

print("\nEmployee(s) with the lowest salary: ")
for employee in lowest_salary_employees:
    print(f"{employee}: ${lowest_salary}")

# Print the dictionary in a well-formatted manner
print("\nFinal employee data: ")
for employee, salary in employee_salaries.items():
    print(f"{employee}: ${salary}")