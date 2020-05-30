countries = ["", "Argentina", "", "Brasil", 0]

print("Raw list:", countries, "\nFiltered list:", list(filter(None, countries)),"\n")

import statistics
random_data = [1.3, 2.7, 0.8, -0.1]

avg = statistics.mean(random_data)

print("Full list:", random_data, "\nAverage:", avg, "\nAbove average:",list(filter(lambda x: x > avg, random_data)))
