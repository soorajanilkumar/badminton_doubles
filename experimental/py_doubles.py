#! /bin/env python3
from itertools import combinations

players = {
    'Alice': 8,
    'Bob': 10,
    'Charlie': 10,
    'Diana': 6,
    'Eve': 6,
    'Frank': 3,
    'Grace': 7,
    'Heidi': 6
}

# make list of all combinations of players
player_combinations = list(combinations(players.keys(), 2))

# get the total skill level for each combination
skill_levels = {
    pair: players[pair[0]] + players[pair[1]]
    for pair in player_combinations
}

# List the pairs sorted by skill level
sorted_pairs = sorted(skill_levels.items(), key=lambda item: item[1], reverse=True)

# Print the pairs and their skill levels in a tabular format
print(f"{'Pair':<20} {'Skill Level':<12}")
print('-' * 32)
for pair, skill in sorted_pairs:
    print(f"{pair[0]:<15} {pair[1]:<15} {skill:<12}")
print('-' * 32)
print(f"Total pairs: {len(sorted_pairs)}")

