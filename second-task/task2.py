import os

os.chdir('./content')
os.makedirs("my_folder", exist_ok=True)
os.chdir(path="./my_folder")

for num in range(1, 11):
    file = open(f'file_{num}.txt', 'w+')
    file.write(f'Это файл номер {num}')
    file.close()
    print(f'Файл номер {num} создан и записан')

os.chdir("../")