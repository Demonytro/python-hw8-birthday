# python - home work 8 - select birthday

from datetime import datetime, timedelta

users = [
    {'name_user': 'Dmytro', 'birthday': datetime(1979, 10, 22)},
    {'name_user': 'Nataliya', 'birthday': datetime(1984, 2, 2)},
    {'name_user': 'Veronika', 'birthday': datetime(2009, 3, 23)},
    {'name_user': 'Bill', 'birthday': datetime(2007, 12, 17)},
    {'name_user': 'Kim', 'birthday': datetime(2007, 12, 15)},
    {"name_user": "Tanya", "birthday": datetime(year=1992, month=9, day=23)},
    {"name_user": "Kostya", "birthday": datetime(year=1992, month=3, day=8)},
    {"name_user": "Serhiy", "birthday": datetime(year=1992, month=3, day=8)},
    {"name_user": "Sasha", "birthday": datetime(year=1994, month=11, day=3)},
    {"name_user": "Nastya", "birthday": datetime(year=1989, month=12, day=24)},
    {"name_user": "Vasya", "birthday": datetime(year=1986, month=12, day=24)},
    {"name_user": "Pasha", "birthday": datetime(year=1986, month=12, day=21)},
    {"name_user": "Olia", "birthday": datetime(year=1995, month=12, day=21)}
]

# dict_birthday = [
#     {'key': 0, 'weekday': 'Monday: ', 'user': ''},
#     {'key': 1, 'weekday': 'Tuesday: ', 'user': ''},
#     {'key': 2, 'weekday': 'Wednesday: ', 'user': ''},
#     {'key': 3, 'weekday': 'Thursday: ', 'user': ''},
#     {'key': 4, 'weekday': 'Friday: ', 'user': ''},
#     {'key': 6, 'weekday': 'next Monday: ', 'user': ''}
# ]


# def get_birthdays_per_week(users):






def main(users, n=7):
    # count = 0

    # dict_with_present_year = {}                #
    # prepare_list_birthdays = []                #

    present_day = datetime.now()
    # present_day = datetime.now().date()
    # weekdays_today = present_day.weekday()
    # period_date_birth = present_day + timedelta(days=n)
    # n = datetime.timedelta()
    # print(type(n))

    for count_n in range(n+1):
        period_date_birth = present_day + timedelta(days=count_n)
        # print(period_date_birth)

        join_user = ''
        
        for user in users:
            # user_date = datetime.strptime(user['birthday'], '%y, %m, %d')
            # print(user)                   #
            current_year = user['birthday'].replace(year=present_day.year)
            # left_days = current_year - period_date_birth

            # if left_days.days < 0:
            #     current_year = user['birthday'].replace(year=present_day.year + 1)
            #     left_days = current_year - period_date_birth

            # print(left_days.days)            #

            # if left_days.days <= n:
            if current_year.date() == period_date_birth.date():
                # print(current_year.date(), period_date_birth.date())

                current_year_weekday = current_year.weekday()
                if current_year_weekday == 5:
                    current_year = period_date_birth + timedelta(days=2)
                if current_year_weekday == 6:
                    current_year = period_date_birth + timedelta(days=1)
                if join_user == '':
                    a = current_year.strftime('%A')
                    # print(a, type(a))
                    # print(user['name_user'])
                    join_user = join_user + a + ': ' + user['name_user']
                    # join_user = (f'{strftime(current_year, '%A')}: {user['name_user']}')
                else:
                    join_user = join_user + ', ' + user['name_user']

        
        
        if join_user != '':
            # prepare_list_birthdays[count] = join_user
            # count +=1
            print(join_user)
        # else:
        #     print('next day')

            

 

# # -------------------------------------------------------------------------------------


if __name__ == '__main__':

    main(users)



