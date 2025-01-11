from collections import defaultdict
# Standard Problem Set Version 2


# Problem 1: Hollywood Stars
# hollywood_stars = defaultdict(list)
# hollywood_stars['Kevin Bacon'] = ['Laverne Cox', 'Sofia Vergara']
# hollywood_stars['Meryl Streep'] = ['Idris Elba', 'Sofia Vergara']
# hollywood_stars['Idris Elba'] = ['Meryl Streep', 'Laverne Cox']
# hollywood_stars['Laverne Cox'] = ['Kevin Bacon', 'Idris Elba']
# hollywood_stars['Sofia Vergara'] = ['Kevin Bacon', 'Meryl Streep']


# print(list(hollywood_stars.keys()))
# print(list(hollywood_stars.values()))
# print(hollywood_stars["Kevin Bacon"])

# Problem 2: The Feeling is Mutual

# def is_mutual(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr[i])):
#             if i != j and arr[i][j] != arr[j][i] and arr[i][j] == 1:
#                 return False
#     return True

# celebrities1 = [
#                 [0, 1, 1, 0],
#                 [1, 0, 1, 0],
#                 [1, 1, 0, 1],
#                 [0, 0, 1, 0]]

# celebrities2 = [
#                 [0, 1, 1, 0],
#                 [1, 0, 0, 0],
#                 [1, 1, 0, 1],
#                 [0, 0, 0, 0]]

# print(is_mutual(celebrities1))
# print(is_mutual(celebrities2))

# Problem 3: Closest Friends

# def get_close_friends(contacts, celeb):
#     adjList = defaultdict(list)

#     for i in range(len(contacts)):
#         adjList[contacts[i][0]].append(contacts[i][1])
#         adjList[contacts[i][1]].append(contacts[i][0])
#     return adjList[celeb]

# contacts = [["Lupita Nyong'o", "Jordan Peele"], ["Meryl Streep", "Jordan Peele"], ["Meryl Streep", "Lupita Nyong'o"], 
# ["Greta Gergwig", "Meryl Streep"], ["Ali Wong", "Greta Gergwig"]]

# print(get_close_friends(contacts, "Lupita Nyong'o"))
# print(get_close_friends(contacts, "Greta Gergwig"))

# Problem 4: Network Lookup
# def get_adj_matrix(clients):
#     celebs = set()
#     for i in range(len(clients)):
#         celebs.add(clients[i][0])
#         celebs.add(clients[i][1])


#     idx = 0
#     celebMap = {}
#     for i in celebs:
#         celebMap[i] = idx
#         idx += 1
    
#     # idMatrix = [[0] * len(celebs)] * len(celebs)
#     idMatrix = []
#     for i in range(len(celebs)):
#         idMatrix.append([0] * len(celebs))    

#     for i, j in clients:
#         idMatrix[celebMap[i]][celebMap[j]] = 1
#         idMatrix[celebMap[j]][celebMap[i]] = 1
#     return celebMap, idMatrix


# clients = [
#             ["Yalitza Aparicio", "Julio Torres"], 
#             ["Julio Torres", "Fred Armisen"], 
#             ["Bowen Yang", "Julio Torres"],
#             ["Bowen Yang", "Margaret Cho"],
#             ["Margaret Cho", "Ali Wong"],
#             ["Ali Wong", "Fred Armisen"], 
#             ["Ali Wong", "Bowen Yang"]]

# id_map, adj_matrix = get_adj_matrix(clients)
# print(id_map)
# print(adj_matrix)



# Problem 5

# Problem 6

# Problem 7

# Problem 8
