'''Reading and writing to file'''

db_path = "fibonaccis.txt"
Fibonaccis = []
db_file = open(db_path,'r')
Fibonaccis = [int(line) for line in db_file.readlines()]
db_file.close()

print(Fibonaccis)

db_path = "writing_data.txt"
db_file = open(db_path,'w+')
db_file.writelines([str(number) + "\n" for number in Fibonaccis])

