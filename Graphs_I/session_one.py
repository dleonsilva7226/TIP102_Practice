from collections import defaultdict, deque
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



# Problem 5: Secret Celebrity
# def identify_celebrity(trust, n):
#     if n == 1:
#         return -1
#     trustedIndividuals = set()
#     for i in trust:
#         trustedIndividuals.add(i[1])
#     if len(trustedIndividuals) == 1:
#         return trustedIndividuals.pop()
#     return -1


# # Test Case 1: Minimum input size, no celebrity
# trust1 = []
# n1 = 1
# expected1 = -1

# # Test Case 2: Celebrity exists with only two people
# trust2 = [[1, 2]]
# n2 = 2
# expected2 = 2

# # Test Case 3: No celebrity due to mutual trust
# trust3 = [[1, 2], [2, 1]]
# n3 = 2
# expected3 = -1

# # Test Case 4: Celebrity exists with multiple people
# trust4 = [[1, 3], [2, 3]]
# n4 = 3
# expected4 = 3

# # Test Case 5: No celebrity due to a lack of universal trust
# trust5 = [[1, 3], [2, 3], [3, 1]]
# n5 = 3
# expected5 = -1

# # Test Case 6: Larger group with a celebrity
# trust6 = [[1, 4], [2, 4], [3, 4]]
# n6 = 4
# expected6 = 4

# # Test Case 7: Larger group with no celebrity
# trust7 = [[1, 2], [2, 3], [3, 1]]
# n7 = 3
# expected7 = -1

# # Test Case 8: Everyone trusts everyone (no celebrity)
# trust8 = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]]
# n8 = 4
# expected8 = -1

# # List of test cases for easier iteration
# test_cases = [
#     (trust1, n1, expected1),
#     (trust2, n2, expected2),
#     (trust3, n3, expected3),
#     (trust4, n4, expected4),
#     (trust5, n5, expected5),
#     (trust6, n6, expected6),
#     (trust7, n7, expected7),
#     (trust8, n8, expected8),
# ]

# # Example test execution
# for i, (trust, n, expected) in enumerate(test_cases, 1):
#     result = identify_celebrity(trust, n)
#     print(f"Test Case {i}: {'Passed' if result == expected else 'Failed'}")


# Problem 6: Casting Call Search

# def have_connection(celebs, start_celeb, target_celeb):
    # BFS Algorithm
    # - Initialize an empty list of visited nodes
    # - Initialize an empty queue 
    # - Add the node we would like to start our traversal from to the queue 
    # - Add the node we would like to start our traversal from to visited
    # - While the queue is not empty:
    #     - Remove an element from the queue and store it in a variable, `current`
    #     - Loop through each of the current node's neighbors:
    #         - If the neighbor has not yet been visited:
    #             - Add the neighbor to the queue
    #             - Add the neighbor to the list of visited nodes
    # - Return the list of visited nodes
#     if start_celeb == target_celeb:
#         return True
#     visited = set()
#     queue = deque()
#     queue.append(start_celeb)
#     visited.add(start_celeb)


#     while queue:
#         current = queue.popleft()
#         for i in range(len(celebs[current])):
#             current_element = celebs[current][i]
#             if current_element == 1 and i == target_celeb:
#                 return True
#             if current_element == 1 and i not in visited:
#                 visited.add(i)
#                 queue.append(i)

#     return False
#     # pass






# Problem 7: Casting Call Search II

# def dfs_helper(celebs, start_node, target_node, visited):
#     # - Helper function
#     #     def dfs_helper(self, start_node, visited)
#     #         - If `start_node` is not in list of visited nodes
#     #             - Append `start_node` to list of visited nodes
#     #             - Loop through `start_node`'s neighbors
#     #                 - Call dfs_helper passing in list of visited nodes and the neighbor
#     #                 as the new start node
#     if start_node not in visited:
#         visited.add(start_node)
#         for i in range(len(celebs[start_node])):
#             current_element = celebs[start_node][i]
#             if current_element == 1:
#                 if i == target_node:
#                     return True
#                 elif dfs_helper(celebs, i, target_node, visited):
#                     return True
#     return False
# def have_connection(celebs, start_celeb, target_celeb):
#     # - Main function
#     # def dfs(self, start_node):
#     #     - Create empty list to store nodes that have been visited
#     #     - Pass list of visited nodes and `start_node` into `dfs_helper`
#     #     - Return list of visited nodes
#     if start_celeb == target_celeb:
#         return True
#     visited = set()
#     return dfs_helper(celebs, start_celeb, target_celeb, visited)


# def test_have_connection():
#     celebs = [
#         [0, 1, 0, 0, 0, 0, 0, 0],  # Celeb 0
#         [0, 1, 1, 0, 0, 0, 0, 0],  # Celeb 1
#         [0, 0, 0, 1, 0, 1, 0, 0],  # Celeb 2
#         [0, 0, 0, 0, 1, 0, 1, 0],  # Celeb 3
#         [0, 0, 0, 1, 0, 0, 0, 1],  # Celeb 4
#         [0, 1, 0, 0, 0, 0, 0, 0],  # Celeb 5
#         [0, 0, 0, 1, 0, 0, 0, 1],  # Celeb 6
#         [0, 0, 0, 0, 1, 0, 1, 0],  # Celeb 7
#     ]

#     # Test case 1: Direct connection exists
#     assert have_connection(celebs, 0, 6) == True, "Test case 1 failed"

#     # Test case 2: No connection exists
#     assert have_connection(celebs, 3, 5) == False, "Test case 2 failed"

#     # Test case 3: Self-loop (should always return True if start_celeb == target_celeb)
#     assert have_connection(celebs, 2, 2) == True, "Test case 3 failed"

#     # Test case 4: Multiple paths to target
#     assert have_connection(celebs, 1, 4) == True, "Test case 4 failed"

#     # Test case 5: No possible path
#     assert have_connection(celebs, 7, 0) == False, "Test case 5 failed"

#     # Test case 6: Target is unreachable from start
#     assert have_connection(celebs, 0, 7) == True, "Test case 6 failed"

#     print("All test cases passed!")


# test_have_connection()

# Problem 8: Copying Seating Arrangements


