__author__ = 'veradocs-web'


squares = []
for x in range(10):
    squares.append(x**2)

print(squares)

print([x**2 for x in range(10)])

print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])

matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
 ]

print([[row[i] for row in matrix] for i in range(4)])

zip(*matrix)


