from functools import reduce

data = [7, 3, 15, 4, 5, 15]
print(reduce(lambda x, y: x*y, data))

product = 1
for x in data:
	product *= x

print(product)

# иными словами, редьюс реализует вычисление _индуктивной функции_ — той, у которой достаточно знать предыдущее значение и значение нового элемента последовательности входов
# другие индуктивные ф-ции: количество, сумма, произведение (выше), хотя бы один, все, максимум, частотный анализ

number = 0
for x in data:
	number += 1

def num_for_reduce(calculated_number, next_input):
	return calculated_number + 1

print("Number =", number, "\nNumber reduce=", reduce(lambda x, y: x+1, data), " - doesn't work with reduce! Need to have initial value 1, not data[0]")

print("Sum =", reduce(lambda x, y: x + y, data))

print("At least one is more than 6:", reduce(lambda x, y: x or y if y > 6 else None, data))
print("At least one is 7:", reduce(lambda x, y: x or y if y == 7 else None, data), "SHOULD RETURN 7")

print("Max =", reduce(lambda x, y: x if x >= y else y, data))

