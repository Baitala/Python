def add_Celsius(temp_tuple):
	return (temp_tuple[0], temp_tuple[1], "Celsius")

temps = [("Berlin", 15), ("Lviv", 20)]

c_to_f = lambda data: (data[0], (9/5)*data[1] + 32, "Fahrenheit")

print(list(map(c_to_f, temps)))
print(list(map(add_Celsius, temps)))
