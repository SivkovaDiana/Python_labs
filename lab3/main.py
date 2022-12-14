import csv
import copy
from func import Filter
from func import Map
from func import Reduce

# Файл StudentsData.csv содержит информацию
# о количестве учеников/студентов различной квалификации(attained level 1-5) для каждого региона Великобритании.
# Требуется Найти отношение количества учеников первой группы к третьей, для регионов, чей код не содержит цифры 3

with open("StudentsData.csv", mode='r', encoding='UTF-8') as file:

    csv_reader = csv.reader(file)

    next(csv_reader)

    filtered = Filter(lambda x : '3' not in x[0], csv_reader)

    m1 = Map(lambda x : [int(x[4]),int(x[6])],filtered)

    def sum_two_values(accumulator,lst):
        accumulator[0] += lst[0]
        accumulator[1] += lst[1]
        return accumulator

    result = Reduce(m1,[0,0],sum_two_values)

with open("result.txt",mode='w',encoding='UTF-8') as file:
    file.write(str(result[0]/result[1]))