from pyparsing import *
import numpy as np


# составляем массив узлов, слагающих элементы
elements = np.zeros((1, 3))
line_num = 0
with open('1.fpn', 'r') as f:
    for line in f:
        if 'TRIA' in line:
            int_num = Suppress(Word(alphas)) + ZeroOrMore(Suppress(',') + Word(nums))
            result = int_num.parseString(line).asList()
            result = result[2:]
            for id_n, node in enumerate(result):
                elements[line_num, id_n] = int(node)
            line_num += 1
            elements = np.append(elements, np.zeros((1, 3)), axis=0)
elements = elements[:-1, :]
print(elements)

# составляем массив координат x, y узлов
nodes = np.zeros((1, 2))
line_num = 0
with open('1.fpn', 'r') as f:
    for line in f:
        if 'NODE' in line:
            int_num = Suppress(Word(alphas)) + ZeroOrMore(Suppress(',') + Word(nums + '.'+ '-'))
            result = int_num.parseString(line).asList()
            result = result[1:3]

            for id_n, coord in enumerate(result):
                nodes[line_num, id_n] = float(coord)
            line_num += 1
            nodes = np.append(nodes, np.zeros((1, 2)), axis=0)
nodes = nodes[:-1, :]
print(nodes)
