import csv
import sigdigit_cal
print(float(4.8))
file_name = input('file name : ')

f = open(file_name + ".csv", 'r', encoding='utf-8')

csv_index = csv.reader(f)

table = []
table_name = []

file_index = []

for line in csv_index:
    file_index.append(line)



for index in file_index[0]:
    table.append([])
    table_name.append(index)

n = 0

while n != len(file_index) - 2:
    for num, index in enumerate(file_index[n+1]):
        table[num].append(str(index))
    n += 1

fomular_syntax = file_index[-1][0]

table_width = len(table_name)
table_length = len(table[0])

n = 0


while n < table_length:
    
    symbol = {}
    
    for n2 in range(table_width):
        symbol[table_name[n2]] = table[n2][n]
        
    sigdigit_cal.calculate(fomular_syntax, symbol)
    
    n = 4
