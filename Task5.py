#print("Hello world!")

d = int(input ("Пожалуйста введите размер выручки компании, тыс. руб: "))
r = int(input ("Пожалуйста введите размер издержек компании, тыс. руб: "))
if d > r:
    pr = d - r
    print("Поздравляю, Ваша компания работает с прибылью, тыс.руб. ", pr)
    rent = (d - r) / d
    print("Рентабельность Вашего бизнеса составляет", rent)
    n = int(input("Пожалуйста введите количество сотрудников компании: "))
    pr_empl = (d - r) / n
    print("Прибыль компании из расчета на 1 сотрудника составляет, тыс.руб.", pr_empl)
else:
    mi = r - d
    print("Ваша компания работате с убытком, тыс.руб.", mi)