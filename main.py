
#Задание 1
#Пользователь вводит НОМЕР ДНЯ НЕДЕЛИ, программа выводит название этого дня

intDay = abs(int(input("\n Enter number day of week:\t")))

if intDay > 7 or intDay == 0:
    print("\tEntered number is uncorrect")
elif intDay == 1 :
    print(" Day number", intDay, "is Monday")
elif intDay == 2 :
    print(" Day number", intDay, "is Thuesday")
elif intDay == 3 :
    print(" Day number", intDay, "is Wensday")
elif intDay == 4 :
    print(" Day number", intDay, "is Thursday")
elif intDay == 5 :
    print(" Day number", intDay, "is Friday")
elif intDay == 6 :
    print(" Day number", intDay, "is Saturday")
elif intDay == 7 :
    print(" Day number", intDay, "is Sunday")