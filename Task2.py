#print ("Hello world!")

seconds = int(input("Пожалуйста, введите время в секундах: "))
hour = seconds // 3600
minute = seconds % 3600 /60
secund = seconds % 3600 % 60 /60
print("h {} m {} s {}" .format(hour, minute, secund))