import json
# Напишите функцию read_entire_file , которая целиком считает текст из файла и напечатает его
file_1 = 'exercise_1\sample.txt'
file_2 = 'exercise_1\sample.json'


def read_entire_file(path_file):
    with open(path_file, 'r') as f:
        text = f.read()
        print(text)

# read_entire_file('exercise_1\sample.txt')


# функция которая принимает на вход путь к текстовому файлу и число n и возвращает первые n строк
def read_first_n_lines(path2file, n):
    # чтение файла построчно и вывод каждой строки из первых n
    with open(path2file, 'r') as f:
        for i in range(0, n):
            print(f.readline().strip())


# read_first_n_lines(file_1, 3)
string = 'read_entire_file(file_1'
# функция которая принимает на вход путь к текстовому файлу и дописывает последней строкой


def add_end_to_file(path2file, string):
    with open(path2file, 'a', encoding='utf-8') as this_file:
        # дополните функцию write необходимым аргументом
        this_file.write('\n' + string)


# add_end_to_file(file_1, string)

new_file = 'digit_marks.json'

# get_names_from_json
def get_names_from_json(path2file):
    with open(path2file, 'r') as file:  # откройте файл в режиме чтения
        data = json.load(file)
        grade = {
            'A': 5,
            'B': 4,
            'C': 3,
            'D': 2
        }
        grades = {}
        names = []
        
        for name, value in data.items():
            names.append(name)
            grades[name] = grade[value]
            
            with open("exercise_1\digit_marks.json","w") as file: 
                json.dump(grades, file, indent=4, ensure_ascii=False)




print(get_names_from_json(file_2))
