from datetime import datetime

def CharInput(inname,inage):
    CurrentYear = datetime.now()
    HundredYear = str(CurrentYear.year - inage + 100)
    
    return str(inname + " you'll be a hundred years old in " + HundredYear)

print(CharInput("Petro",31))