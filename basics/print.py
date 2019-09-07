import os

print(f"Hello {os.getlogin()}")
print(f"Env. variables: {os.environ}")
print(f"This dir: {os.listdir()}")