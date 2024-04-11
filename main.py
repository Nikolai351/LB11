import random

def ant_colony_algorithm(cities, iterations, evaporation_rate, pheromone_update):
    # Инициализация феромона
    pheromone = {(i, j): 1 for i in range(len(cities)) for j in range(i)}

    # Инициализация расстояния между городами
    distances = {(i, j): abs(cities[i][0] - cities[j][0]) + abs(cities[i][1] - cities[j][1]) for i in range(len(cities)) for j in range(i)}

    # Инициализация пути
    path = []

    for _ in range(iterations):
        # Создание случайного пути
        new_path = [random.choice(cities)]
        current_city = new_path[0]
        for _ in range(len(cities) - 1):
            possible_cities = [city for city in cities if city != current_city]
            min_distance = float('inf')
            for next_city in possible_cities:
                distance = distances[(current_city, next_city)]
                if distance < min_distance:
                    min_distance = distance
                    next_city = next_city
            new_path.append(next_city)
            current_city = next_city
        new_path.append(new_path[0])  # Замыкание пути

        # Обновление феромона
        for i in range(len(new_path) - 1):
            pheromone[(new_path[i], new_path[i + 1])] *= (1 - evaporation_rate) + evaporation_rate * pheromone_update

        # Обновление расстояния между городами
        for i in range(len(new_path) - 1):
            distances[(new_path[i], new_path[i + 1])] = abs(cities[new_path[i]][0] - cities[new_path[i + 1]][0]) + abs(cities[new_path[i]][1] - cities[new_path[i + 1]][1])

        # Обновление пути
        path = new_path

    return path

# Пример использования функции
cities = [(0, 0), (5, 10), (10, 5), (15, 10), (20, 0)]
path = ant_colony_algorithm(cities, 1000, 0.1, 1.0)
print(path)
