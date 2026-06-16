import heapq

# ==========================================
# Intelligent Campus Navigation Assistant
# A* Search + IDS + Bayes Rule
# ==========================================

campus = {

    "Library": {
        "Cafeteria": (2, 5),
        "Computer Lab": (4, 8)
    },

    "Cafeteria": {
        "Library": (2, 5),
        "Admin Office": (3, 4)
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

    "Classroom Block": {
        "Computer Lab": (3, 4),
        "Auditorium": (2, 2)
    },

    "Auditorium": {
        "Admin Office": (4, 5),
        "Classroom Block": (2, 2)
    }
}

# ==========================================
# A* Heuristic
# ==========================================

heuristic = {

    "Library": 8,
    "Cafeteria": 6,
    "Computer Lab": 4,
    "Admin Office": 3,
    "Classroom Block": 2,
    "Auditorium": 0
}

# ==========================================
# Prior Crowd Probabilities
# ==========================================

crowd_probability = {

    "Library": 0.2,
    "Cafeteria": 0.9,
    "Computer Lab": 0.4,
    "Admin Office": 0.3,
    "Classroom Block": 0.2,
    "Auditorium": 0.1
}

# ==========================================
# Normalize Input
# ==========================================

def normalize_location(user_input):

    return " ".join(
        word.capitalize()
        for word in user_input.strip().split()
    )

# ==========================================
# Bayes Rule
# ==========================================

def posterior_probability(location):

    prior = crowd_probability[location]

    p_noise_given_crowded = 0.8
    p_noise_given_not_crowded = 0.2

    p_noise = (
        p_noise_given_crowded * prior
        +
        p_noise_given_not_crowded * (1 - prior)
    )

    posterior = (
        p_noise_given_crowded * prior
    ) / p_noise

    return posterior

# ==========================================
# A* Search
# ==========================================

def a_star(start, goal, mode):

    pq = []

    heapq.heappush(
        pq,
        (0, 0, start, [start])
    )

    visited = set()

    while pq:

        f, g, node, path = heapq.heappop(pq)

        if node == goal:
            return g, path

        if node in visited:
            continue

        visited.add(node)

        for neighbor, values in campus[node].items():

            distance = values[0]
            time = values[1]

            if mode == "shortest":

                edge_cost = distance

            elif mode == "fastest":

                edge_cost = time

            else:

                edge_cost = posterior_probability(
                    neighbor
                )

            new_g = g + edge_cost

            new_f = (
                new_g +
                heuristic[neighbor]
            )

            heapq.heappush(
                pq,
                (
                    new_f,
                    new_g,
                    neighbor,
                    path + [neighbor]
                )
            )

    return None, None

# ==========================================
# Depth Limited Search
# ==========================================

def dls(node, goal, limit, path):

    if node == goal:
        return path

    if limit <= 0:
        return None

    for neighbor in campus[node]:

        if neighbor not in path:

            result = dls(
                neighbor,
                goal,
                limit - 1,
                path + [neighbor]
            )

            if result:
                return result

    return None

# ==========================================
# Iterative Deepening Search
# ==========================================

def ids(start, goal):

    for depth in range(len(campus) + 1):

        result = dls(
            start,
            goal,
            depth,
            [start]
        )

        if result:
            return result

    return None

# ==========================================
# Main Program
# ==========================================

print("=" * 42)
print(" Intelligent Campus Navigation Assistant ")
print("=" * 42)

print("\nAvailable Locations:\n")

for place in campus:
    print("-", place)

source = normalize_location(
    input("\nEnter Starting Location: ")
)

destination = normalize_location(
    input("Enter Destination Location: ")
)

if source not in campus:

    print("\nInvalid Starting Location")
    exit()

if destination not in campus:

    print("\nInvalid Destination Location")
    exit()

print("\nSelect Route Preference")
print("1. Shortest Route")
print("2. Fastest Route")
print("3. Safest Route")

choice = input("\nEnter Choice: ")

if choice == "1":

    mode = "shortest"

elif choice == "2":

    mode = "fastest"

elif choice == "3":

    mode = "safest"

else:

    print("\nInvalid Choice")
    exit()

# ==========================================
# A* Result
# ==========================================

cost, route = a_star(
    source,
    destination,
    mode
)

print("\n===================================")
print("Navigation Result")
print("===================================")

print("\nSelected Mode :", mode.upper())

print("\nSearch Algorithm Used : A* Search")

print("\nBest Route :")
print(" -> ".join(route))

if mode == "shortest":

    print("\nTotal Distance :", round(cost, 2))

elif mode == "fastest":

    print("\nTotal Time :", round(cost, 2), "minutes")

else:

    print("\nSafety Score :", round(cost, 3))

# ==========================================
# Bayesian Probabilities (FOR ALL MODES)
# ==========================================

print("\n===================================")
print("Bayesian Crowd Diagnosis")
print("===================================\n")

total = 0

for location in route:

    p = posterior_probability(location)

    total += p

    print(
        f"{location} -> P(Crowded|Noise) = {p:.3f}"
    )

average = total / len(route)

print(
    f"\nAverage Posterior Probability = {average:.3f}"
)

# ==========================================
# IDS Result
# ==========================================

ids_route = ids(
    source,
    destination
)

print("\n===================================")
print("Iterative Deepening Search Result")
print("===================================\n")

print(" -> ".join(ids_route))

print("\nSearch Algorithm Used : IDS")

# ==========================================
# CO Mapping
# ==========================================

print("\n===================================")
print("AI Concepts Demonstrated")
print("===================================\n")

print("CO1 -> Graph Representation")
print("CO2 -> A* Search")
print("CO3 -> Iterative Deepening Search")
print("CO4 -> Intelligent Decision Making")
print("CO5 -> Bayes Rule Inference")
print("CO6 -> Integrated AI Navigation Pipeline")
