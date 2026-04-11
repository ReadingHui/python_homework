# Task 3: List Comprehensions Practice
import csv
CSV_PATH = 'csv/employees.csv'

def read_file():

    try:
        with open(CSV_PATH, 'r') as f:
            reader = csv.reader(f)
            result = [row[1] + ' ' + row[2] for i, row in enumerate(reader) if i > 0]
            print(result)
            e_result = [name for name in result if 'e' in name]
            print(e_result)
    except FileNotFoundError:
        print('File not found.')

def main():
    read_file()

if __name__ == '__main__':
    main()