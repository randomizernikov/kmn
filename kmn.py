print ('камень - 1 \nножницы - 2 \nбумага - 3')
timur = int(input('тимур, выбери знак: '))
ruslan = int(input('руслан, выбери знак: '))


if timur >= 4 or timur < 1 or ruslan >= 4 or ruslan < 1:
    print ('была введена неверная цифра')
elif timur ==1 and ruslan == 2:
    print ('тимур победил')
elif timur ==2 and ruslan == 3:
    print ('тимур победил')
elif timur ==3 and ruslan == 1:
    print ('тимур победил')
elif timur == ruslan:
    print ('ничья')
else:
    print ('победил руслан')