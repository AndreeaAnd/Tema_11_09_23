# 1.Realizati un program care sa gaseasca al doilea cel mai mic numar din lista. - OK

# list_1 = [-8, 1, 2, -2, 0]
# print(list_1)
# list_1.sort()
# print(list_1)
# print('Al doilea cel mai mic numar din lista este:', sorted(list_1)[1])

# list_2 = [1, 1, 0, 0, 2, -2, -2]
# print(list_2)
# list_2.sort()
# print(list_2)
# print('Al doilea cel mai mic numar din lista este:', sorted(list_2)[2:3])

# list_3 = [1, -1, 0, -9, 4, -5]
# print(list_3)
# list_3.sort()
# print(list_3)
# print('Al doilea cel mai mic numar din lista este:', sorted(list_3)[1])

# list_4 = [1, 4, 0, 23, 6, 34]
# print(list_4)
# list_4.sort()
# print(list_4)
# print('Al doilea cel mai mic numar din lista este:', sorted(list_4)[1])

# 2.Realizati un program care sa creeze o lista, concatenand o lista data, cu nr. de la 1 la n
#exemplu:
#list-var = ['p', 's']
# n = 5
# result = ['p1', 's1', 'p2', 's2', 'p3', 's3', 'p4', 's4', 'p5', 's5']

# list1 = ['a', 'b']
# list2 = [1, 2, 3, 4]
# new_list1=[]
# n = 4
# for i in list1:
#     print('')
#     for j in list2:
#         new_list1.append(i+str(j+1))
# print(list(new_list1))

# for i in range(1, n+1):
#     for element in new_list:

# list1 = ['a', 'b']
# newlist = [x for x in list1 if 'a' in x]
# print(newlist)

# 4. Realizati un program care sa sorteze o lista de dictionare folosind functia Lambda.
# models = [{'make':'Huawei', 'model':2, 'color':'Black'}, {'make':'Apple', 'model':'14', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
# models_sorted = sorted(models, key=lambda x: x['make'])
# print(models_sorted)

# Top Filme
# Utilizatorul cu cele mai multe filme vizionate
# utilizatori = [
#     {'nume': 'George', 'filme': ['Shrek', 'Bond', 'Fight Club']},
#     {'nume': 'Cristian', 'filme': ['Fight Club', 'The Nun', 'Dracula', 'Bond']},
#     {'nume': 'Stefan', 'filme': ['Fight Club', 'Slumdog Millionaire']}
# ]
# utilizator_max_filme = None
# max_numar_filme = 0
# for utilizator in utilizatori:
#     numar_filme = len(utilizator['filme'])
#     if numar_filme > max_numar_filme:
#         max_numar_filme = numar_filme
#         utilizator_max_filme = utilizator['nume']
# print('Utilizatorul cu cele mai multe filme vizionate:', utilizator_max_filme)


# Top utilizatori cu cele mai multe filme vizionate
# users = [
#     {'name': 'George', 'movies': ['Shrek', 'Bond', 'Fight Club']},
#     {'name': 'Cristian', 'movies': ['Fight Club', 'The Nun', 'Dracula', 'Bond']},
#     {'name': 'Stefan', 'movies': ['Fight Club', 'Slumdog Millionaire']}
#     ]
# sorted_users = sorted(users, key=lambda x: len(x['movies']), reverse=True)
# print('Top users with most viewed movies:')
# for user in sorted_users:
#     print(user['name'])

# Top filme după vizionări
# utilizatori = [
#     {'nume': 'George', 'filme': ['Shrek', 'Bond', 'Fight Club']},
#     {'nume': 'Cristian', 'filme': ['Fight Club', 'The Nun', 'Dracula', 'Bond']},
#     {'nume': 'Stefan', 'filme': ['Fight Club', 'Slumdog Millionaire']}
# ]
# numar_vizionari={'Shrek':100, 'Bond':110, 'Fight Club':150,'The Nun':90,'Dracula':105,'Slumdog Millionaire':85}
# top_filme = sorted(numar_vizionari.keys(), key=lambda x: numar_vizionari[x], reverse=True)
# print('Top filme după vizionări:', top_filme)
# for film in top_filme:
#     print(film)

# Cel mai vizionat film - Fight Club in cazul de mai sus
# most_watched_movie = []
# movie_counts = {'Shrek':1, 'Bond':1, 'Fight Club':3,'The Nun':1,'Dracula':1,'Bond':1,'Slumdog Millionaire':1}
# max_views = 0
# for movie, views in movie_counts.items():
#     if views > max_views:
#         most_watched_movie = movie
#         max_views = views
# print("Cel mai vizionat film:", most_watched_movie)

# Avand doua liste, afisati o lista a elementelor comune ambelor liste
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# Rezultat
# [1,2,3,5,8,13]

# Tema elemente comune
# elemente_comune = []
# for element in a:
#     if element in b and element not in elemente_comune:
#         elemente_comune.append(element)
# print("Elemente comune din ambele liste:", elemente_comune)







