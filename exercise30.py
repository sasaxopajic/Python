employee_number = 0
employees = []
salaries = []
while employee_number >= 0:
    name = input("Employee name: ")
    employees.append(name)
    salary = int(input("Salary: "))
    salaries.append(salary)
    m = input("Do you want to continue? (yes/no) ")
    if m == "no":
        break
max_salary = salaries[0]
for i in range(1, len(salaries)):
    if salaries[i] > max_salary:
        max_salary = salaries[i]
        print("Max salary:", employees[i], "-", max_salary)
    else:
        print("Max salary:", employees[0], "-", salaries[0])