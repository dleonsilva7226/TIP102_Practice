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
# Problem 4:





# Problem 5: 


# Problem 6:


# Problem 7:


# Problem 8:
