import heapq

# ==========================================
# Intelligent Campus Navigation Assistant
# ==========================================

# -------------------------------------------------
# CO1 : Problem Formulation & Graph Representation
# Campus Map using Graph
# Nodes = Locations
# Edges = Roads
# Values = (Distance, Time)
# -------------------------------------------------

campus = {

    "Library": {
        "Cafeteria": (2, 5),
        "Computer Lab": (4, 8)
    },

    "Cafeteria": {
        "Library": (2, 5),
        "Admin Office": (3, 4),
        "Parking Area": (6, 10)
    },

    "Computer Lab": {
        "Library": (4, 8),
        "Admin Office": (5, 7),
        "Classroom Block": (3, 4)
    },

    "Admin Office": {
        "Cafeteria": (3, 4),
        "Computer Lab": (5, 7),
        "Auditorium": (4, 5)
    },

    "Parking Area": {
        "Cafeteria": (6, 10),
        "Auditorium": (3, 4)
    },

    "Classroom Block": {
        "Computer Lab": (3, 4),
        "Auditorium": (2, 2)
    },

    "Auditorium": {
        "Admin Office": (4, 5),
        "Parking Area": (3, 4),
        "Classroom Block": (2, 2)
    }
}

# -------------------------------------------------
# CO3 : Constraint Satisfaction Problem (CSP)
# Blocked / Restricted Paths
# -------------------------------------------------

blocked_paths = [
    ("Parking Area", "Auditorium")
]

# -------------------------------------------------
# CO5 : Probabilistic Reasoning
# Crowd Probability
# Higher value = More crowded
# -------------------------------------------------

traffic_probability = {

    "Library": 0.2,
    "Cafeteria": 0.9,
    "Computer Lab": 0.4,
    "Admin Office": 0.3,
    "Parking Area": 0.7,
    "Classroom Block": 0.2,
    "Auditorium": 0.1
}

# -------------------------------------------------
# Function to Fix Case Sensitivity
# Removes spaces and converts correctly
# -------------------------------------------------

def normalize_location(user_input):

    return user_input.strip().title()

# -------------------------------------------------
# CO2 : Search Algorithm
# Dijkstra Based Intelligent Navigation
# -------------------------------------------------

def intelligent_navigation(graph, start, end, mode):

    queue = [(0, start, [])]

    visited = set()

    while queue:

        cost, node, path = heapq.heappop(queue)

        if node in visited:
            continue

        visited.add(node)

        path = path + [node]

        if node == end:
            return cost, path

        for neighbor, values in graph[node].items():

            # -------------------------------------------------
            # CO3 Covered Here
            # Constraint Checking
            # -------------------------------------------------

            if ((node, neighbor) in blocked_paths or
                (neighbor, node) in blocked_paths):

                continue

            distance = values[0]
            time = values[1]

            # -------------------------------------------------
            # CO4 : Intelligent Decision Making
            # -------------------------------------------------

            if mode == "shortest":

                new_cost = cost + distance

            elif mode == "fastest":

                new_cost = cost + time

            elif mode == "safest":

                safety_penalty = (
                    traffic_probability[neighbor] * 10
                )

                new_cost = (
                    cost +
                    distance +
                    safety_penalty
                )

            heapq.heappush(
                queue,
                (new_cost, neighbor, path)
            )

    return float("inf"), []

# -------------------------------------------------
# Main Program
# -------------------------------------------------

print("==========================================")
print(" Intelligent Campus Navigation Assistant ")
print("==========================================")

print("\nAvailable Locations:\n")

for place in campus:
    print("-", place)

# -------------------------------------------------
# User Input
# -------------------------------------------------

source = normalize_location(
    input("\nEnter Starting Location: ")
)

destination = normalize_location(
    input("Enter Destination Location: ")
)

# -------------------------------------------------
# Invalid Location Checking
# -------------------------------------------------

if source not in campus:

    print("\nInvalid Starting Location")
    exit()

if destination not in campus:

    print("\nInvalid Destination Location")
    exit()

# -------------------------------------------------
# CO4 : User Decision Making
# -------------------------------------------------

print("\nSelect Route Preference")
print("1. Shortest Route")
print("2. Fastest Route")
print("3. Safest Route")

choice = input("\nEnter Your Choice: ").strip()

# -------------------------------------------------
# Choice Processing
# -------------------------------------------------

if choice == "1":

    mode = "shortest"

elif choice == "2":

    mode = "fastest"

elif choice == "3":

    mode = "safest"

else:

    print("\nInvalid Choice")
    exit()

# -------------------------------------------------
# CO6 : Integrated AI Pipeline
# User Input -> Graph -> Constraints
# -> Search -> Decision -> Final Route
# -------------------------------------------------

cost, route = intelligent_navigation(
    campus,
    source,
    destination,
    mode
)

# -------------------------------------------------
# Final Output
# -------------------------------------------------

print("\n===================================")
print("        Navigation Result")
print("===================================")

if cost == float("inf"):

    print("\nNo Route Found")

else:

    print("\nSelected Mode :", mode.upper())

    print("\nBest Route :")

    print(" -> ".join(route))

    if mode == "shortest":

        print("\nTotal Distance :", cost)

    elif mode == "fastest":

        print("\nTotal Time :", cost, "minutes")

    elif mode == "safest":

        print("\nSafety Score :", round(cost, 2))

# -------------------------------------------------
# CO Mapping Summary
# -------------------------------------------------
#
# CO1 -> Graph Representation
# CO2 -> Search Algorithm
# CO3 -> Constraint Satisfaction Problem
# CO4 -> Intelligent Decision Making
# CO5 -> Probabilistic Reasoning
# CO6 -> Integrated AI Pipeline
#
# -------------------------------------------------