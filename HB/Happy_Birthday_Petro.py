#If you have problem with cyrillics: set LC_ALL running sudo update-locale LC_ALL=ru_UA.UTF-8
from datetime import date
debug = False

def Happy_Birthday_en(BD,name,congratulators_name):
    ''' Shows as many "Happy Birthdays" in English as person's age,
        if today is BD. Arguments:
        BD - date of Birthday;
        name - person's name;
        congratulators_name - name of person who congratulates.
    '''
    current_date = date.today()
    if current_date.month == BD.month and current_date.day == BD.day:
        how_many_HB = age = current_date.year - BD.year
        for i in range(0,how_many_HB):
            print ("Happy Birthday " + name + "!\t#%d" % (i+1) )
        print ("\nHappy " + str(age) + " years " + name + "!")
        print ("\t\t\t ", congratulators_name, "\n\t\t\t",current_date)
    else:
        print ("Today is not your Birthday " + name + ", calm down.")

def Happy_Birthday_uk(BD,name,congratulators_name):
    ''' Shows as many "Happy Birthdays" in Ukrainian as person's age,
        if today is BD. Arguments:
        BD - date of Birthday;
        name - person's name. Note that vocative case should be used.
        congratulators_name - name of person who congratulates. Nominative.
    '''
    current_date = date.today()
    if current_date.month == BD.month and current_date.day == BD.day:
        how_many_HB = age = current_date.year - BD.year
        for i in range(0,how_many_HB):
            print ("З Днем Народження, " + name + "!\t#%d" % (i+1) )
        print ("\nЗ " + str(age) + "-літтям, " + name + "!")
        print ("\t\t\t", congratulators_name, "\n\t\t\t",current_date)
    else:
        print ("Сьогодні не твій День Народження, " + name + ", дайся на спокій.")

def Happy_Birthday_ru(BD,name,congratulators_name):
    ''' Shows as many "Happy Birthdays" in Russian as person's age,
        if today is BD. Arguments:
        BD - date of Birthday;
        name - person's name;
        congratulators_name - name of person who congratulates.
    '''
    current_date = date.today()
    if current_date.month == BD.month and current_date.day == BD.day:
        how_many_HB = age = current_date.year - BD.year
        for i in range(0,how_many_HB):
            print ("С Днём Рождения, " + name + "!\t#%d" % (i+1) )
        print ("\nС " + str(age) + "-летием, " + name + "!")
        print ("\t\t\t", congratulators_name, "\n\t\t\t",current_date)
    else:
        print ("Спокойно, " + name + ", сегодня не твой День Рождения.")

if debug:
    Petro_BD = date(1988, date.today().month, date.today().day)
else:
    Petro_BD = date(1988, 8, 5)

lang = input("Choose language (en, uk, ru): ")
while lang not in ['en', 'uk', 'ru', 'EN', 'UK', 'RU']:
    lang = input("Incorrect input. Please enter en, uk, or ru: ")

if lang == "en":
    Happy_Birthday_en(Petro_BD,"Petro","Yevhen")
elif lang == "uk":
    Happy_Birthday_uk(Petro_BD,"Петре","Євген")
else:
    Happy_Birthday_ru(Petro_BD,"Петро","Женя")
