# If you have problem with cyrillics: set LC_ALL running
# sudo update-locale LC_ALL=ru_UA.UTF-8

from datetime import date


class Person_to_congratulate:
    '''A person that should be congratulated.
    Attributes:
    1. First Name
    2. First Name in Vocative case (if not Ukrainian, then should be same as
    First Name)
    3. DOB
    4. Native language code: "en", "uk", or "ru"
    '''
    def __init__(self, first_name_Nominative, first_name_Vocative, DOB,
                 nativ_lang):
        self.__native_language = nativ_lang  # en, uk, ru
        self.__BD = DOB
        self.__age = date.today().year - self.__BD.year
        self.__name = first_name_Vocative
        self.__name_Nominative = first_name_Nominative

    def __str__(self):
        if self.__native_language == "uk":
            return f"""Person's name is {self.__name_Nominative}
                       Vocative case of name is {self.__name}
                       Born {self.__BD}
                       Navive language is {self.__native_language}"""
        else:
            return f"""Person's name is {self.__name_Nominative}
                       Born {self.__BD}
                       Navive language is {self.__native_language}"""

#   def __concatenate_DOBs(DOB1,DOB2):
#      '''Makes new DOB so age is age1 + age2'''
        pass

    def __add__(self, second_person):
        return Person_to_congratulate(self.__name_Nominative + ", and " +
                                      second_person.__name_Nominative,
                                      self.__name +
                                      ", and" +
                                      second_person.__name, self.__BD, "en")

    def Happy_Birthday_en(self, congratulators_name, how_many_HB):
        ''' Shows as many "Happy Birthdays" in native language as person's age,
            if today is BD. Arguments:
            BD - date of Birthday;
            name - person's name;
            congratulators_name - name of person who congratulates.
        '''
        current_date = date.today()
        if (current_date.month == self.__BD.month and
           current_date.day == self.__BD.day):
            for i in range(0, how_many_HB):
                print ("Happy Birthday " + self.__name + "!\t#%d" % (i+1))
            print ("\nHappy " + str(self.__age) + " years " + self.__name +
                   "!")
            print ("\t\t\t ", congratulators_name, "\n\t\t\t", current_date)
        else:
            print ("Today is not your Birthday " + self.__name +
                   ", calm down.")

    def Happy_Birthday_uk(self, congratulators_name, how_many_HB):
        ''' Shows as many "Happy Birthdays" in Ukrainian as person's age,
            if today is BD. Arguments:
            BD - date of Birthday;
            name - person's name. Note that vocative case should be used.
            congratulators_name - name of person who congratulates. Nominative.
        '''
        current_date = date.today()
        if (current_date.month == self.__BD.month and
           current_date.day == self.__BD.day):
            for i in range(0, how_many_HB):
                print ("З Днем Народження, " + self.__name + "!\t#%d" % (i+1))
            print ("\nЗ " + str(self.__age) + "-літтям, " + self.__name + "!")
            print ("\t\t\t", congratulators_name, "\n\t\t\t", current_date)
        else:
            print ("Сьогодні не твій День Народження, " + self.__name +
                   ", дайся на спокій.")

    def Happy_Birthday_ru(self, congratulators_name, how_many_HB):
        ''' Shows as many "Happy Birthdays" in Russian as person's age,
            if today is BD. Arguments:
            BD - date of Birthday;
            name - person's name;
            congratulators_name - name of person who congratulates.
        '''
        current_date = date.today()
        if (current_date.month == self.__BD.month and
           current_date.day == self.__BD.day):
            for i in range(0, how_many_HB):
                print ("С Днём Рождения, " + self.__name + "!\t#%d" % (i+1))
            print ("\nС " + str(self.__age) + "-летием, " + self.__name + "!")
            print ("\t\t\t", congratulators_name, "\n\t\t\t", current_date)
        else:
            print ("Спокойно, " + self.__name +
                   ", сегодня не твой День Рождения.")

    def Happy_Birthday(self, who_congratulates, how_many_times_congratulate):
        '''Congratulates the person with his/her Birtday
        '''
        if self.__native_language == "en":
            self.Happy_Birthday_en(who_congratulates,
                                   how_many_times_congratulate)
        elif self.__native_language == "uk":
            self.Happy_Birthday_uk(who_congratulates,
                                   how_many_times_congratulate)
        else:
            self.Happy_Birthday_ru(who_congratulates,
                                   how_many_times_congratulate)
