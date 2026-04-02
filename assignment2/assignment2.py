import csv
import os
import traceback
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(SCRIPT_DIR)
CSV_PATH = os.path.join(PARENT_DIR, 'csv', 'employees.csv')


# Task 2: Read a CSV File
def read_employees():
    info = {}
    rows = []

    try:
        with open(CSV_PATH, 'r') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    info['fields'] = row
                else:
                    rows.append(row)
            info['rows'] = rows
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name: {trace[2]}, Message : {trace[3]}')
        print(f'Exception type: {type(e).__name__}')
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f'Stack trace: {stack_trace}')
    
    return info

employees = read_employees()
print('Task 1 result:')
print(employees)
print()

# Task 3: Find the Column Index
def column_index(idx: str) -> int:
    return employees['fields'].index(idx)

employee_id_column = column_index('employee_id')
print('Task 3 result:')
print(f'Employee_id column number: {employee_id_column}')
print()

# Task 4: Find the Employee First Name
def first_name(row_num: int) -> str:
    idx = column_index('first_name')
    return employees['rows'][row_num][idx]

#Task 5: Find the Employee: a Function in a Function
def employee_find(employee_id: int):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches = list(filter(employee_match, employees['rows']))
    return matches

# Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches

# Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    idx = column_index('last_name')
    employees['rows'].sort(key=lambda x: x[idx])
    return employees['rows']

sort_by_last_name()
print('Task 6 result: ')
print('Sorted dict:')
print(employees)
print()

# Task 8: Create a dict for an Employee
def employee_dict(row: list) -> dict:
    return dict(zip(employees['fields'][1:], row[1:]))

print('Task 8 result:')
print('Dictionary by first row')
print(employee_dict(employees['rows'][1]))
print()

# Task 9: A dict of dicts, for All Employees
