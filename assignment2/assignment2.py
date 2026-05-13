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
def all_employees_dict():
    return{row[employee_id_column]: employee_dict(row) for row in employees['rows']}

print('Task 9 result:')
print('All Employees Dictionary:')
print(all_employees_dict())
print()

# Task 10: Use the os Module
def get_this_value():
    return os.getenv('THISVALUE')
print('Task 10 result:')
print(f'THISVALUE: {get_this_value()}')
print()

# Task 11: Creating Your Own Module
import custom_module

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret('Open Sesame!')
print('Task 11 result:')
print(f'New secret: {custom_module.secret}')
print()

# Task 12: Read minutes1.csv and minutes2.csv
def read_minutes():
    minutes1_path = os.path.join(PARENT_DIR, 'csv', 'minutes1.csv')
    minutes2_path = os.path.join(PARENT_DIR, 'csv', 'minutes2.csv')
    minutes1 = {}
    minutes2 = {}
    try:
        rows = []
        with open(minutes1_path, 'r') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    minutes1['fields'] = row
                else:
                    rows.append(tuple(row))
            minutes1['rows'] = rows
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

    try:
        rows = []
        with open(minutes2_path, 'r') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    minutes2['fields'] = row
                else:
                    rows.append(tuple(row))
            minutes2['rows'] = rows
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

    return minutes1, minutes2

minutes1, minutes2 = read_minutes()
print('Task 12 result:')
print('minutes1: ')
print(minutes1)
print('minutes2: ')
print(minutes2)
print()

# Task 13: Create minutes_set
def create_minutes_set():
    set1 = set(minutes1['rows'])
    set2 = set(minutes2['rows'])
    res_set = set1.union(set2)
    return res_set

minutes_set = create_minutes_set()
print('Task 13 result:')
print('minutes_set:')
print(minutes_set)
print()

# Task 14: Convert to datetime
from datetime import datetime

def create_minutes_list():
    minutes_list = list(minutes_set)
    minutes_list = list(map(lambda x: (x[0], datetime.strptime(x[1], '%B %d, %Y')), minutes_list))
    return minutes_list

minutes_list = create_minutes_list()
print('Task 14 result:')
print('minutes_list:')
print(minutes_list)
print()

# Task 15: Write Out Sorted List
def write_sorted_list():
    sorted_list = sorted(minutes_list, key=lambda x: x[1])
    sorted_list = list(map(lambda x: (x[0], datetime.strftime(x[1], '%B %d, %Y')), sorted_list))
    try:
        rows = []
        with open('minutes.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(minutes1['fields'])
            writer.writerows(sorted_list)
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
    return sorted_list

write_sorted_list()