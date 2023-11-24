import itertools

def read_actions(filename):
    actions = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            name, cost, profit = parts[0], int(parts[1]), float(parts[2].rstrip('%'))
            actions.append((name, cost, profit))
    return actions

def optimal_actions(actions, max_budget):
    best_actions = []
    best_profit = 0

    for combination_size in range(1, len(actions) + 1):
        for combination in itertools.combinations(actions, combination_size):
            total_cost = sum(action[1] for action in combination)
            if total_cost <= max_budget:
                total_profit = sum(action[1] * action[2] / 100 for action in combination)
                if total_profit > best_profit:
                    best_profit = total_profit
                    best_actions = combination

    return best_actions, best_profit

if __name__ == "__main__":
    filename = "actions.txt"
    max_budget = 500
    actions = read_actions(filename)

    best_actions, best_profit = optimal_actions(actions, max_budget)

    print("Best actions to maximize profit:")
    for action in best_actions:
        print(f"{action[0]} - Cost: {action[1]} euros, Profit: {action[1] * action[2] / 100} euros")

    print(f"\nBest total profit: {best_profit} euros")


