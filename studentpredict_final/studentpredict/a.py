import datetime
import pandas
file = pandas.read_excel('portuguese_data.xlsx')
f = open('sql_port.txt', 'w')
perform = file['category']

f.write('insert into performance values')
for roll in range(647):
    f.write('(%d, 1828410%03d, \'%s\'),\n' % (roll + 1, roll, perform[roll]))
roll = 648
f.write('(%d, 1828410%03d, \'%s\');\n' % (roll + 1, roll, perform[roll]))