from collections import deque, defaultdict
# Problem 1: Celebrity Collaborations
# collaborations = defaultdict(list)
# collaborations["Chadwick Boseman"].append(("Lupita Nyong'o", 2))
# collaborations["Chadwick Boseman"].append(("Robert Downey Jr.", 3))
# collaborations["Chadwick Boseman"].append(("Mark Ruffalo", 2))
# collaborations["Lupita Nyong'o"].append(("Mark Ruffalo", 1))
# collaborations["Lupita Nyong'o"].append(("Chadwick Boseman", 2))
# collaborations["Mark Ruffalo"].append(("Lupita Nyong'o", 1))
# collaborations["Mark Ruffalo"].append(("Chadwick Boseman", 2))
# collaborations["Mark Ruffalo"].append(("Robert Downey Jr.", 5))
# collaborations["Mark Ruffalo"].append(("Rosario Dawson", 2))
# collaborations["Robert Downey Jr."].append(("Chadwick Boseman", 3))
# collaborations["Robert Downey Jr."].append(("Mark Ruffalo", 5))
# collaborations["Rosario Dawson"].append(("Mark Ruffalo", 2))

# print(collaborations["Lupita Nyong'o"])
# print(collaborations["Mark Ruffalo"])
# print(collaborations["Rosario Dawson"])
# print(collaborations["Robert Downey Jr."])
# print(collaborations["Chadwick Boseman"])


# Problem 2: Cast vs Crew
# DFS METHOD

# - Main function
#     def dfs(self, start_node):
#         - Create empty list to store nodes that have been visited
#         - Pass list of visited nodes and `start_node` into `dfs_helper`
#         - Return list of visited nodes

# - Helper function
#     def dfs_helper(self, start_node, visited)
#         - If `start_node` is not in list of visited nodes
#             - Append `start_node` to list of visited nodes
#             - Loop through `start_node`'s neighbors
#                 - Call dfs_helper passing in list of visited nodes and the neighbor
#                   as the new start node
# ------------------------------------------------------------------------------------------------------
# def dfs_helper(cast_and_crew, start_node, component, visited):
#     if start_node not in visited:
#         component.add(start_node)
#         visited.add(start_node)
#         for i in cast_and_crew[start_node]:
#             dfs_helper(cast_and_crew, i, component, visited)

# def get_groups(cast_and_crew):
#     components = []
#     visited = set()
#     for k, v in cast_and_crew.items():
#         if k not in visited:
#             component = set()
#             dfs_helper(cast_and_crew, k, component, visited)
#             components.append(list(component))
#     return components



# cast_and_crew = {
#     "Daniel Kaluuya": ["Allison Williams"],
#     "Allison Williams": ["Daniel Kaluuya", "Catherine Keener", "Bradley Whitford"],
#     "Bradley Whitford": ["Allison Williams", "Catherine Keener"],
#     "Catherine Keener": ["Allison Williams", "Bradley Whitford"],
#     "Jordan Peele": ["Jason Blum", "Gregory Plotkin", "Toby Oliver"],
#     "Toby Oliver": ["Jordan Peele", "Gregory Plotkin"],
#     "Gregory Plotkin": ["Jason Blum", "Toby Oliver", "Jordan Peele"],
#     "Jason Blum": ["Jordan Peele", "Gregory Plotkin"]
# }

# print(get_groups(cast_and_crew))



# Problem 3:
# def bacon_number(bacon_network, celeb):
#     if celeb == "Kevin Bacon":
#        return 0 
#     queue = deque()
#     visited = set()

#     queue.append((celeb, 0))
#     visited.add(celeb)

#     while queue:
#         current, curr_num = queue.popleft()
#         for i in bacon_network[current]:
#             if i == "Kevin Bacon":
#                 return curr_num + 1
#             if i not in visited:
#                 queue.append((i, curr_num + 1))
#                 visited.add(i)


#     return -1


# bacon_network = {
#     "Kevin Bacon": ["Kyra Sedgewick", "Forest Whitaker", "Julia Roberts", "Tom Cruise"],
#     "Kyra Sedgewick": ["Kevin Bacon"],
#     "Tom Cruise": ["Kevin Bacon", "Kyra Sedgewick"],
#     "Forest Whitaker": ["Kevin Bacon", "Denzel Washington"],
#     "Denzel Washington": ["Forest Whitaker", "Julia Roberts"],
#     "Julia Roberts": ["Denzel Washington", "Kevin Bacon", "George Clooney"],
#     "George Clooney": ["Julia Roberts", "Vera Farmiga"],
#     "Vera Farmiga": ["George Clooney", "Max Theriot"],
#     "Max Theriot": ["Vera Farmiga", "Jennifer Lawrence"],
#     "Jennifer Lawrence": ["Max Theriot"]
# }

# # Test 1: Kevin Bacon himself
# assert bacon_number(bacon_network, "Kevin Bacon") == 0  # Expected Output: 0

# # Test 2: Kyra Sedgewick, directly connected to Kevin Bacon
# assert bacon_number(bacon_network, "Kyra Sedgewick") == 1  # Expected Output: 1

# # Test 3: Julia Roberts, directly connected to Kevin Bacon
# assert bacon_number(bacon_network, "Julia Roberts") == 1  # Expected Output: 1

# # Test 4: Max Theriot, 4 steps away from Kevin Bacon
# assert bacon_number(bacon_network, "Max Theriot") == 4  # Expected Output: 4

# # Test 5: Actor1, no path to Kevin Bacon
# bacon_network_no_path = {
#     "Actor1": ["Actor2"],
#     "Actor2": ["Actor3"],
#     "Actor3": ["Actor4"],
#     "Actor4": ["Actor5"],
#     "Actor5": []
# }
# assert bacon_number(bacon_network_no_path, "Actor1") == -1  # Expected Output: -1 (No path to Kevin Bacon)

# # Test 6: George Clooney, no path to Kevin Bacon
# assert bacon_number(bacon_network, "George Clooney") == 2  # Expected Output: -1 (No direct or indirect path to Kevin Bacon)

# # Test 7: Forest Whitaker, directly connected to Kevin Bacon
# assert bacon_number(bacon_network, "Forest Whitaker") == 1  # Expected Output: 1

# # Test 8: Jennifer Lawrence, 5 steps away from Kevin Bacon
# assert bacon_number(bacon_network, "Jennifer Lawrence") == 5  # Expected Output: 5

# print("ALL TESTS PASSED!")


# Problem 4: Press Junket Navigation

# Optimize this using parent pointers. aka a map. do it after 5

# def find_path(venue_map, target):
#     if target == 0:
#         return [0]
#     visited = set()
#     queue = deque()
#     possible_paths = set()

#     visited.add(0)
#     possible_paths.add((0,0))
#     queue.append((0, 0))
#     targetFound = False
#     path = []
#     while queue:
#         parent, current = queue.popleft()
#         for i in venue_map[current]:
#             if i not in visited:
#                 queue.append((current, i))
#                 possible_paths.add((current, i))
#                 visited.add(i)
#             if i == target:
#                 targetFound = True
#                 break
#         if targetFound:
#             break

#     new_target = target
#     while new_target != 0:
#         for current in possible_paths:
#             if current[1] == new_target:
#                 path.append(current[1])
#                 new_target = current[0]
#                 break
    
#     path.append(0)
#     path.reverse()
#     return path



# venue_map = [
#     [1, 2],        # Node 0 is connected to 1 and 2
#     [0, 3],        # Node 1 is connected to 0 and 3
#     [0, 4],        # Node 2 is connected to 0 and 4
#     [1, 5],        # Node 3 is connected to 1 and 5
#     [2],           # Node 4 is connected to 2
#     [3]            # Node 5 is connected to 3
# ]

# # Test cases
# print(find_path(venue_map, 5))  # Expected output: [0, 1, 3, 5]
# print(find_path(venue_map, 2))  # Expected output: [0, 2]
# print(find_path(venue_map, 4))  # Expected output: [0, 2, 4]
# print(find_path(venue_map, 0))  # Expected output: [0]
# print(find_path(venue_map, 3))  # Expected output: [0, 1, 3]



# Problem 5: WEIRD
# def dfs_helper(connections, connection_dict, start_node, visited, curr_num):
#     if start_node not in visited:
#         curr_num[0] += 1
#         visited.add(start_node)
#         print("Before: Curr Val", start_node)
#         print("Before: Num", curr_num)
#         print("---------------------")
#         tuple_list = (curr_num[0], -1)
#         connection_dict[start_node] = tuple_list
        
#         for i in connections[start_node]:
#             dfs_helper(connections, connection_dict, i, visited, curr_num)
#             curr_num[0] += 1 
        
#         if len(connections[start_node]) == 0:
#             curr_num[0] += 1
#             tuple_list = connection_dict[start_node][0], curr_num[0]
#             connection_dict[start_node] = tuple_list
#         else:
#             # print("After: Curr Val", start_node)
#             # print("After: Num", curr_num)
#             # print("---------------------")
#             tuple_list = connection_dict[start_node][0], curr_num[0]
#             connection_dict[start_node] = tuple_list

        


# def rumor_spread_times(connections, n, start):
#     connection_dict = defaultdict(tuple)
#     connections_adj_list = defaultdict(list)
#     for i in connections:
#         connections_adj_list[i[0]].append(i[1])
#     for i in connections:
#         connection_dict[i[0]] = (-1,-1)
#         connection_dict[i[1]] = (-1,-1)
#     visited = set()
#     curr_num = [0]
#     print(connections_adj_list)
#     print('-------------------------------')
#     dfs_helper(connections_adj_list, connection_dict, start, visited, curr_num)
#     return connection_dict 

    


# connections = [
#     ["Amber Gill", "Greg O'Shea"],
#     ["Amber Gill", "Molly-Mae Hague"],
#     ["Greg O'Shea", "Molly-Mae Hague"],
#     ["Greg O'Shea", "Tommy Fury"],
#     ["Molly-Mae Hague", "Tommy Fury"],
#     ["Tommy Fury", "Ovie Soko"],
#     ["Curtis Pritchard", "Maura Higgins"]
# ]

# print(rumor_spread_times(connections, 7, "Amber Gill"))

# Problem 6: Network Strength

# def is_strongly_connected(celebrities):
#     for k, v in celebrities.items():
#         if len(v) != len(celebrities) - 1:
#             return False
#     return True


# Example Test Cases with Assertions

# def test_is_strongly_connected():
#     # Test Case 1: Fully connected graph
#     celebrities1 = {
#         "Dev Patel": ["Meryl Streep", "Viola Davis"],
#         "Meryl Streep": ["Dev Patel", "Viola Davis"],
#         "Viola Davis": ["Meryl Streep", "Dev Patel"]
#     }
#     assert is_strongly_connected(celebrities1) == True, "Test Case 1 Failed"
    
#     # Test Case 2: Missing connections (not everyone likes everyone else)
#     celebrities2 = {
#         "John Cho": ["Rami Malek", "Zoe Saldana", "Meryl Streep"],
#         "Rami Malek": ["John Cho", "Zoe Saldana", "Meryl Streep"],
#         "Zoe Saldana": ["Rami Malek", "John Cho", "Meryl Streep"],
#         "Meryl Streep": []  # Missing connections
#     }
#     assert is_strongly_connected(celebrities2) == False, "Test Case 2 Failed"

#     # Test Case 3: Empty graph (no celebrities)
#     celebrities3 = {}
#     assert is_strongly_connected(celebrities3) == True, "Test Case 3 Failed"

#     # Test Case 4: Single celebrity (trivial case)
#     celebrities4 = {
#         "Tom Hanks": []
#     }
#     assert is_strongly_connected(celebrities4) == True, "Test Case 4 Failed"

#     # Test Case 5: Partially connected graph
#     celebrities5 = {
#         "A": ["B", "C"],
#         "B": ["A", "C"],
#         "C": ["A"]  # Missing connection to B
#     }
#     assert is_strongly_connected(celebrities5) == False, "Test Case 5 Failed"

#     # Test Case 6: Fully connected with a larger group
#     celebrities6 = {
#         "A": ["B", "C", "D"],
#         "B": ["A", "C", "D"],
#         "C": ["A", "B", "D"],
#         "D": ["A", "B", "C"]
#     }
#     assert is_strongly_connected(celebrities6) == True, "Test Case 6 Failed"

#     print("All test cases passed!")

# # Run tests
# test_is_strongly_connected()


# Problem 7: Max Star Power

# def find_max_star_power(collaboration_map, costar_a, costar_b):
#     visited = set()
#     max_num = [float('-inf')]

#     def dfs_helper(start_node, visited, curr_num, max_num, costar_b):
#         if start_node not in visited:
#             visited.add(start_node)
#             for i in collaboration_map[start_node]:
#                 if i[0] not in visited:
#                     curr_num += i[1]
#                     if i[0] == costar_b:
#                         if curr_num > max_num[0]:
#                             max_num[0] = curr_num
#                     dfs_helper(i[0], visited, curr_num, max_num, costar_b)
#         if max_num[0] == float('-inf'):
#             return 0
#         return max_num[0]

#     return dfs_helper(costar_a, visited, 0, max_num, costar_b)

# def test_find_max_star_power():
#     # Test case 1
#     collaboration_map_1 = {
#         "Leonardo DiCaprio": [("Brad Pitt", 40), ("Robert De Niro", 30)],
#         "Brad Pitt": [("Leonardo DiCaprio", 40), ("Scarlett Johansson", 20)],
#         "Robert De Niro": [("Leonardo DiCaprio", 30), ("Chris Hemsworth", 50)],
#         "Scarlett Johansson": [("Brad Pitt", 20), ("Chris Hemsworth", 30)],
#         "Chris Hemsworth": [("Robert De Niro", 50), ("Scarlett Johansson", 30)]
#     }
#     # Path with max star power: Leonardo DiCaprio -> Brad Pitt -> Scarlett Johansson -> Chris Hemsworth (40 + 20 + 30 = 90)
#     assert find_max_star_power(collaboration_map_1, "Leonardo DiCaprio", "Chris Hemsworth") == 90

#     # Test case 2 (simple graph)
#     collaboration_map_2 = {
#         "A": [("B", 10)],
#         "B": [("A", 10), ("C", 20)],
#         "C": [("B", 20)]
#     }
#     # Path with max star power: A -> B -> C (10 + 20 = 30)
#     assert find_max_star_power(collaboration_map_2, "A", "C") == 30

#     # Test case 3 (direct connection between a and b)
#     collaboration_map_3 = {
#         "A": [("B", 50)],
#         "B": [("A", 50)]
#     }
#     # Direct connection A -> B with star power 50
#     assert find_max_star_power(collaboration_map_3, "A", "B") == 50

#     # Test case 4 (disconnected graph)
#     collaboration_map_4 = {
#         "A": [("B", 15)],
#         "B": [("A", 15)],
#         "C": [("D", 25)],
#         "D": [("C", 25)]
#     }
#     # No valid path between A and D, so result should be 0 (or a default value, depending on your implementation)
#     assert find_max_star_power(collaboration_map_4, "A", "D") == 0

#     # Test case 5 (graph with multiple paths)
#     collaboration_map_5 = {
#         "A": [("B", 10), ("C", 5)],
#         "B": [("A", 10), ("C", 20)],
#         "C": [("A", 5), ("B", 20)]
#     }
#     # Path with max star power: A -> B -> C (10 + 20 = 30)
#     assert find_max_star_power(collaboration_map_5, "A", "C") == 30

#     print("All test cases passed.")

# # Assuming the function find_max_star_power is defined, we can call the test function
# test_find_max_star_power()


# Problem 8: Celebrity Feuds

# def can_split(n, dislikes):
#     queue = deque()
#     visited = set()
#     color1 = 0
#     colors = []
#     for i in range(n):
#         colors.append(-1)
#     adj_list = defaultdict(list)
#     for i in dislikes:
#         adj_list[i[0]].append(i[1])
#     colors[0] = color1
#     visited.add(1)
#     queue.append(1)
#     while queue:
#         current = queue.popleft()
#         for i in adj_list[current]:
#             if colors[i-1] == -1:
#                 colors[i-1] = 1 - colors[current-1]
#             elif colors[i-1] == colors[current-1]:
#                 return False
#             if i not in visited:
#                 visited.add(i)
#                 queue.append(i)
#     return True
    
# def test_can_split():
#     # Test case 1
#     dislikes_1 = [[1, 2], [1, 3], [2, 4]]
#     assert can_split(4, dislikes_1) == True, "Test case 1 failed"

#     # Test case 2
#     dislikes_2 = [[1, 2], [1, 3], [2, 3]]
#     assert can_split(3, dislikes_2) == False, "Test case 2 failed"

#     # Test case 3 (No dislikes, should be able to split any group)
#     dislikes_3 = []
#     assert can_split(5, dislikes_3) == True, "Test case 3 failed"

#     # Test case 4 (Single celebrity, no dislikes)
#     dislikes_4 = []
#     assert can_split(1, dislikes_4) == True, "Test case 4 failed"

#     # Test case 5 (Two celebrities, no dislikes)
#     dislikes_5 = []
#     assert can_split(2, dislikes_5) == True, "Test case 5 failed"

#     # Test case 6 (Two celebrities, one dislike)
#     dislikes_6 = [[1, 2]]
#     assert can_split(2, dislikes_6) == True, "Test case 6 failed"

#     # Test case 7 (Cycle in dislikes, should return False)
#     dislikes_7 = [[1, 2], [2, 3], [3, 1]]
#     assert can_split(3, dislikes_7) == False, "Test case 7 failed"

#     # Test case 8 (Dislikes in larger group, should return False)
#     dislikes_8 = [[1, 2], [2, 3], [3, 4], [4, 1]]
#     assert can_split(4, dislikes_8) == True, "Test case 8 failed"

#     print("All test cases passed.")

# test_can_split()
