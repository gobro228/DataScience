import re

text = '''
Имя: Иван, Группа: A123, Средний балл: 4.75
Имя: Петр, Группа: B456, Средний балл: 3.92
Имя: Елена, Группа: A123, Средний балл: 4.89
Имя: Анна, Группа: C789, Средний балл: 4.12
Имя: Михаил, Группа: B456, Средний балл: 5.01
Имя: Алиса, Группа: A123, Средний балл: 4.98
'''.strip()

with open('./content/data.txt', 'w', encoding='utf-8') as f:
    f.write(text)


def read_student_data(file_path):
    students = []

    pattern = re.compile(r"Имя: (?P<Имя>[а-яА-Яa-zA-Z]+), Группа: (?P<Группа>\w+), Средний балл: (?P<Средний_балл>\d+\.\d+)")

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            match = pattern.match(line.strip())
            if match:
                student_info = {
                    "Имя": match.group("Имя"),
                    "Группа": match.group("Группа"),
                    "Средний балл": float(match.group("Средний_балл"))
                }
                students.append(student_info)
            else:
                print(f"Строка не соответствует шаблону: {line.strip()}")

    return students

file_path = "./content/data.txt"

student_data = read_student_data(file_path)

for student in student_data:
  print(f"Имя: {student['Имя']}, Группа: {student['Группа']}, Средний балл: {student['Средний балл']}")

