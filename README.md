# python-hw8-birthday
a function for displaying a list of colleagues who need to be congratulated on their birthday during the week

Задание

Вам нужно реализовать полезную функцию для вывода списка коллег, которых надо поздравить с днём рождения на неделе.

У вас есть список словарей users, каждый словарь в нём обязательно имеет ключи name и birthday. Такая структура представляет модель списка пользователей с их именами и днями рождения. name — это строка с именем пользователя, а birthday — это datetime объект, в котором записан день рождения.

Ваша задача написать функцию get_birthdays_per_week, которая получает на вход список users и выводит в консоль (при помощи print) список пользователей, которых надо поздравить по дням.
Условия приёмки
get_birthdays_per_week выводит именинников в формате:

Monday: Bill, Jill
Friday: Kim, Jan

Пользователей, у которых день рождения был на выходных, надо поздравить в понедельник.
Для отладки удобно создать тестовый список users и заполнить его самостоятельно.
Функция выводит пользователей с днями рождения на неделю вперед от текущего дня.
Неделя начинается с понедельника.
