#обмен двух переменных через две доп. переменные
a=2
b=5
##tmp1=b
##tmp2=a
##a=tmp1
##b=tmp2

#это же через множественное присваивание
#tmp1, tmp2 = b, a
#a, b = tmp1, tmp2

#а вот и короткий вариант
a, b = b, a
#обмен через временный кортеж — неименованные «скрытые» tmp1, tmp2
