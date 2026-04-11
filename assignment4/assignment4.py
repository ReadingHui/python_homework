# Task 1: Introduction to Pandas - Creating and Manipulating DataFrames
import pandas as pd

def print_df(df, message: str):
    print(message)
    print(df)
    print()

data_dict = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

task1_data_frame = pd.DataFrame(data_dict)
print_df(task1_data_frame, 'task1_data_frame: ')


task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
print_df(task1_with_salary, 'task1_with_salary: ')

task1_older = task1_with_salary.copy()
task1_older['Age'] += 1
print_df(task1_older, 'task1_older: ')

task1_older.to_csv('employees.csv', index=False)

# Task 2: Loading Data from CSV and JSON
task2_employees = pd.read_csv('employees.csv')
print_df(task2_employees, 'task2_employees: ')

json_employees = pd.read_json('additional_employees.json')
print_df(json_employees, 'json_employees: ')

more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print_df(more_employees, 'more_employees: ')

# Task 3: Data Inspection - Using Head, Tail, and Info Methods
first_three = more_employees.head(3)
print(first_three, 'first_three: ')

last_two = more_employees.tail(2)
print(last_two, 'last_two: ')

employee_shape = more_employees.shape
print(employee_shape, 'employee_shape: ')

print('more_employees info: ')
print(more_employees.info())
print()

# Task 4: Data Cleaning
dirty_data = pd.read_csv('assignment4/dirty_data.csv')
print_df(dirty_data, 'dirty_data: ')
clean_data = dirty_data.copy()

clean_data.drop_duplicates(inplace=True)
print_df(clean_data, 'clean_data after dropping duplicates: ')

clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')
print_df(clean_data, 'clean_data after converting Age to numeric: ')

clean_data['Salary'] = clean_data['Salary'].replace(['unknown', 'n/a'], pd.NA)
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')
print_df(clean_data, 'clean_data after standardizing NaNs and converting Salary to numeric: ')

clean_data['Age'] = clean_data['Age'].fillna(clean_data['Age'].mean())
clean_data['Salary'] = clean_data['Salary'].fillna(clean_data['Salary'].median())
print_df(clean_data, 'clean_data after filling NaN values with mean on Age and median on Salary: ')

clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], format='mixed', errors='coerce')
print_df(clean_data, 'clean_data after converting Hier Date to datetime: ')

clean_data['Name'] = clean_data['Name'].str.strip().str.upper()
clean_data['Department'] = clean_data['Department'].str.strip().str.upper()
print_df(clean_data, 'clean_data after stripping extra whitespace and standardizing Name and Department as uppercase: ')