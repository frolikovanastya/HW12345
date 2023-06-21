import os
files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.txt')]
file_data = []
for f in files:
    with open(f, 'r', encoding="utf-8") as file:
        file_lines = file.readlines()
        file_data.append((f, len(file_lines), file_lines))
file_data.sort(key=lambda x: x[1])
with open('result.txt', 'w', encoding="utf-8") as file:
    for data in file_data:
        file.write(data[0] + '\n')
        file.write(str(data[1]) + '\n')
        file.writelines(data[2])
