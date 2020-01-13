#DAY1 TASKS
from __future__ import division

users = [
    {'id': 0, 'name': 'Hero'},
    {'id': 1, 'name': 'Dunn'},
    {'id': 2, 'name': 'Sue'},
    {'id': 3, 'name': 'Chi'},
    {'id': 4, 'name': 'Thor'},
    {'id': 5, 'name': 'Clive'},
    {'id': 6, 'name': 'Hicks'},
    {'id': 7, 'name': 'Devin'},
    {'id': 8, 'name': 'Kate'},
    {'id': 9, 'name': 'Klein'},
]

#ДРУЖЕСКИЕ СВЯЗИ НА РАБОТЕ

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

for user in users:
    user['friends'] = []
    for i, j in friendships:
        users[i]['friends'].append(users[j]) # j friends for i
        users[j]['friends'].append(users[i]) # i friends for j

#СУММА ДРУЗЕЙ

def number_of_friends(user):
    return len(user['friends']) #length lists id friends
total_connections = sum(number_of_friends(user) for user in users)
num_users = len(users)
avg_connections = total_connections / num_users #average numbers

num_friends_by_id = [(user['id'], number_of_friends(user)) for user in users]
sorted(num_friends_by_id, key = lambda (user_id, num_friends):num_friends, reverse = True) #Упорядочить в убывающем порядке

#ЗАРПЛАТЫ И СТАЖ

salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (83000, 8.7), (88000, 8.1),
                        (83000, 8.7), (88000, 8.1),
                        (83000, 8.7), (88000, 8.1),
                        (83000, 8.7), (88000, 8.1)]
salary_by_tenure = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

#СРЕДНЯЯ ЗАРПЛАТА В ЗАВИСИМОСТИ ОТ СТАЖА

average_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}

# СТАЖНАЯ ГРУППА

def tenure_bucket(tenure):
    if tenure < 2:
        return 'Менее 2'
    elif tenure < 5:
        return 'Между 2 и 5'
    else:
        return 'Более 5'

salary_by_tenure_bucket - defaultdict(list)
for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

average_salary_by_bucket = {
    tenure_bucket: sum(salaries) / len(salaries)
    for tenure_bucket, salaries in salary_by_tenure_bucket.iteritems()
}