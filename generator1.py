'''
def generator_function():
    for i in range(10):
        yield i

for item in generator_function():
    print(item)
'''

'''
def csv_reader(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    return result
'''

def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row
        
csv_gen = csv_reader("dataset.txt")
row_count = 0

for row in csv_gen:
    row_count += 1

print(f"Row count is {row_count}")

