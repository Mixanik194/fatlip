# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности
# duration в секундах: до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.


seconds = int(input('Введите секунды: '))
sec = seconds % 60
min = (seconds // 60) % 60
hour = (seconds // 3600) % 24
day = (seconds // 86400)

if seconds < 60:
    print(sec)
elif 60 <= seconds < 3600:
    print(min, sec)
elif 3600 <= seconds < 86400:
    print(hour, min, sec)
elif seconds >= 86400:
    print(day, 'дн', hour, 'час', min, 'мин', sec,  'сек')


