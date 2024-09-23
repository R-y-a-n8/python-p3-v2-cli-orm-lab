from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.all()  
    for employee in employees:
        print(employee)  

def find_employee_by_name():
    name = input("Enter the employee's name: ")
    employee = Employee.find_by_name(name)
    if employee:
        print(employee)
    else:
        print(f"Employee {name} not found")


def find_employee_by_id():
    emp_id = input("Enter the employee's id: ")
    employee = Employee.find_by_id(emp_id)
    if employee:
        print(employee)
    else:
        print(f"Employee {emp_id} not found")


def create_employee():
    try:
        name = input("Enter the employee's name: ")
        job_title = input("Enter the employee's job title: ")
        department_id = int(input("Enter the employee's department id: "))
        department = Department.find_by_id(department_id)

        if not department:
            raise ValueError("Department ID must reference an existing department.")

        employee = Employee.create(name=name, job_title=job_title, department_id=department_id)
        print(f"Success: {employee}")
    except Exception as e:
        print(f"Error creating employee: {str(e)}")


def update_employee():
    try:
        emp_id = input("Enter the employee's id: ")
        employee = Employee.find_by_id(emp_id)
        if not employee:
            print(f"Employee {emp_id} not found")
            return

        name = input(f"Enter the employee's new name (current: {employee.name}): ")
        job_title = input(f"Enter the employee's new job title (current: {employee.job_title}): ")
        department_id = int(input(f"Enter the employee's new department id (current: {employee.department_id}): "))
        department = Department.find_by_id(department_id)

        if not department:
            raise ValueError("Department ID must reference an existing department.")

        employee.update(name=name, job_title=job_title, department_id=department_id)
        print(f"Success: {employee}")
    except Exception as e:
        print(f"Error updating employee: {str(e)}")


def delete_employee():
    emp_id = input("Enter the employee's id: ")
    employee = Employee.find_by_id(emp_id)
    if employee:
        employee.delete()
        print(f"Employee {emp_id} deleted")
    else:
        print(f"Employee {emp_id} not found")


def list_department_employees():
    department_id = int(input("Enter the department's id: "))
    department = Department.find_by_id(department_id)
    if department:
        employees = department.employees()  
        for employee in employees:
            print(employee)
    else:
        print(f"Department {department_id} not found")
