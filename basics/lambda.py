scifi_authors = ["Isaac Asimov", "Ray Bradbury", "Douglas Adams"]

scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())
print(scifi_authors)
