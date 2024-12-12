import random

# Convert all transfer amounts to floats
transfers = [float(x.replace(',', '')) for x in [
    "-2.76", '-131.9', '-732522.06', '-12', '-245.25', '-13000', '-860.58', '-41955.65', '-317.8', '-66.2', '-55.63', '-2000', '-20', '-583.94', '-478162.44', '-8.23', '-17501.62', '-14377.94', '-3926.63', '-14.38', '-3164.01', '-260.76', '-182.83', '-856.44', '-783.31', '-1476.06', '-28.8', '-2420.98', '-9999', '-275.94', '-423.66', '-1146.92', '-14460', '-57.1', '-50.18', '-5', '-50213.63', '-64.29', '-24920.27', '-287.02', '-2.77', '-2', '-151.73', '-144.91', '-61.2', '-68.65', '-24721.5', '-725094', '-1057.09', '-283.96', '-50', '-1418.12', '-108.33', '-85.05', '-2809.91', '-132.7', '-2003', '-275.31', '-100', '-9238.41', '-1872.07', '-2.9', '-26334.9', '-1176.35', '-2.9', '-1121265.52', '-2725.77', '-997.93', '-44.33', '-770829.18', '-723.61', '-1246031.19', '-26146.07', '-1066505.7', '-1232218.55', '-724.11', '-10.44', '-200317.6', '-57.98', '-180.58', '-222.85', '-329.93', '-100', '-1222.3', '-580.33', '-3219.29', '-2.9', '-1259843.82', '-286.28', '-16852.56', '-34740.7', '-1657.85', '-1824.23', '-59.65', '-2731149', '-64503', '-110878.51', '-149663', '-10074.58', '-107410.6', '-2.9', '-20', '-1378.98', '-569', '-400.38', '-70.73', '-17.23', '-2.06', '-2958.77', '-185.6',
    "-536429.02", "-8.23", "-17501.62", "-14377.94", "-3926.63", "-51.22", "-6", "-3385.33", "-96.52", "-278.87", "-566.79", "-567", "-17201.51", "-14.33", "-829.19", "-228.26", "-224", "-1084.72", "-99", "-3279.91", "-236.21", "-2.79", "-178.18", "-917.63", "-534.72", "-857.2", "-277.55", "-4.24", "-150.65", "-12.34", "-20", "-114.61", "-1037063.93", "-1032.48", "-2.78", "-200", "-29.08", "-591.39", "-2998.79", "-1317.75", "-109", "-2.32", "-359.47", "-2214.07", "-76996", "-20713.08", "-339.26", "-889.15", "-3.41", "-5601.16", "-129.61", "-18843", "-138.25", "-55.01", "-75.57", "-254.24", "-20.87", "-225.65", "-12.83", "-150", "-1000", "-56.6", "-171.25", "-3", "-152.85"
]]

def fitness(combination, target_range):
    """Improved fitness function with less harsh penalties for near-misses."""
    total = sum(combination)
    if target_range[0] <= total <= target_range[1]:
        return 0  # Best fitness
    return min(abs(total - target_range[0]), abs(total - target_range[1]))  # Lesser penalty for being close

# def fitness(combination, target_range):
#     """Fitness function: prioritizes combinations within the target range, heavily penalizes others."""
#     total = sum(combination)
#     if target_range[0] <= total <= target_range[1]:
#         return 0  # Optimal fitness
#     else:
#         # This returns a high penalty if outside the range
#         return abs(min(abs(total - target_range[0]), abs(total - target_range[1]))) + 100000


def create_individual(transfers, size):
    """Allow dynamic individual size."""
    return random.sample(transfers, size)

def create_population(transfers, pop_size, min_size, max_size):
    """Create population with varying individual sizes."""
    return [create_individual(transfers, random.randint(min_size, max_size)) for _ in range(pop_size)]

def select(population, target_range, num_parents):
    """Select the best performing individuals to continue to next gen."""
    population.sort(key=lambda x: fitness(x, target_range))
    return population[:num_parents]

def crossover(parent1, parent2):
    """Perform a more sophisticated crossover."""
    split = random.randint(1, min(len(parent1), len(parent2)) - 1)
    return parent1[:split] + parent2[split:]

def mutate(individual, transfers, mutation_rate):
    """Mutate an individual by changing some of its genes."""
    return [random.choice(transfers) if random.random() < mutation_rate else gene for gene in individual]

def genetic_algorithm(transfers, target_range, pop_size, num_generations, mutation_rate, min_size, max_size):
    population = create_population(transfers, pop_size, min_size, max_size)
    for generation in range(num_generations):
        print(f"Generation {generation}: Best fitness = {fitness(population[0], target_range)}")
        population = select(population, target_range, len(population) // 2)
        next_generation = []
        while len(next_generation) < pop_size:
            parent1, parent2 = random.sample(population, 2)
            child = crossover(parent1, parent2)
            child = mutate(child, transfers, mutation_rate)
            next_generation.append(child)
        population = next_generation
    best_individual = select(population, target_range, 1)[0]
    return best_individual, sum(best_individual)

# Define the target range
target_range = (-148130.00, -148139.00)

# Run the genetic algorithm
best_combination, best_sum = genetic_algorithm(transfers, target_range, pop_size=50, num_generations=200, mutation_rate=0.05, min_size=2, max_size=5)
print(f"Best combination: {best_combination}, Sum: {best_sum}")
