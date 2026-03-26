# Task 1: Hello
def hello():
    return "Hello!"

# Task 2: Greet with a Formatted String
def greet(name: str) -> str:
    return f'Hello, {name}!'

# Task 3: Calculator
def calc(a, b, operation='multiply') -> int | float:
    match operation:
        case "add":
            try:
                return a + b
            except TypeError:
                return "You can't add those values!"
        case "subtract":
            try:
                return a - b
            except TypeError:
                return "You can't subtract those values!"
        case "multiply":
            try:
                return a * b
            except TypeError:
                return "You can't multiply those values!"
        case "divide":
            try:
                return a / b
            except TypeError:
                return "You can't divide those values!"
            except ZeroDivisionError:
                return "You can't divide by 0!"
        case "modulo":
            try:
                return a % b
            except TypeError:
                return "You can't modulo those values!"
            except ZeroDivisionError:
                return "You can't divide by 0!"
        case "int_divide":
            try:
                return a // b
            except TypeError:
                return "You can't divide those values!"
            except ZeroDivisionError:
                return "You can't divide by 0!"
        case _:
            raise ValueError("Operation must be from ['add', 'subtract', 'multiply', 'divide', 'modulo', 'int_divide']")
    return
'''
Remark: 
According to the task requirement, these are the error to be caught. 
However, this "calc" function doesn't really make sense if the input are strings and list etc.,
but the program can still function properly due to native support of operators in Python.
'''

# Task 4: Data Type Conversion
def data_type_conversion(value, type: str):
    err_msg = f"You can't convert {value} into a {type}."
    match type:
        case 'float':
            try:
                return float(value)
            except ValueError as e:
                return err_msg
        case 'str':
            try:
                return str(value)
            except ValueError as e:
                return err_msg
        case 'int':
            try:
                return int(value)
            except ValueError as e:
                return err_msg
        case _:
            raise ValueError(f"{type} is not a supported type.")

# Task 5: Grading System, Using *args
def grade(*args):
    try:
        avg = sum(args) / len(args)
    except ZeroDivisionError:
        print("Input cannot be empty")
        return "Invalid data was provided."
    except TypeError:
        return "Invalid data was provided."
    grades = ['F', 'D', 'C', 'B', 'A']
    return grades[int(max(0, avg // 10 - 5))]

# Task 6: Use a For Loop with a Range
def repeat(old_str: str, cnt: int) -> str:
    new_str = ''
    for i in range(cnt):
        new_str += old_str
    return new_str

# Task 7: Student Scores, Using **kwargs
def student_scores(method: str, **kwargs) -> float:
    if method == 'best':
        best_score = float('-inf')
        for key, value in kwargs.items():
            if value > best_score:
                best_student = key
                best_score = value
        return best_student
    elif method == 'mean':
        return sum(kwargs.values()) / len(kwargs.values())
    
# Task 8: Titleize, with String and List Operations
def titleize(title: str) -> str:
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    title_split = title.split(' ')
    for i in range(len(title_split)):
        if i == 0 or i == len(title_split) - 1 or title_split[i] not in little_words:
            title_split[i] = title_split[i].capitalize()
    return ' '.join(title_split)

# Task 9: Hangman, with more String Operations
def hangman(secret: str, guess: str) -> str:
    guesses = set(guess)
    print(guesses)
    return ''.join([c if c in guesses else '_' for c in secret])

# Task 10: Pig Latin, Another String Manipulation Exercise
def pig_single(word: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(word)):
        if word[i] in vowels:
            if i == 0:
                return word + 'ay'
            elif word[i] == 'u' and word[i - 1] == 'q':
                return word[i + 1:] + word[:i + 1] + 'ay'
            else:
                return word[i:] + word[:i] + 'ay'

def pig_latin(original: str) -> str:
    original_list = original.split(' ')
    return ' '.join([pig_single(word) for word in original_list])