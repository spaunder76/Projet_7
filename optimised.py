def lire_actions(filename):
    actions = []
    with open(filename, 'r') as file:
        next(file) 
        for line in file:
            parts = line.strip().split(',')
            nom, cout, benefice = parts[0], float(parts[1]), float(parts[2].rstrip('%'))
            actions.append((nom, cout, benefice))
    return actions

def investissement_optimise(actions, budget_max):
    actions_triees = sorted(actions, key=lambda x: x[2] / x[1] if x[1] != 0 else 0, reverse=True)
    investissement = []
    cout_total = 0
    profit_total = 0

    for action in actions_triees:
        if action[1] != 0 and cout_total + action[1] <= budget_max:
            investissement.append(action)
            cout_total += action[1]
            profit_total += action[1] * action[2] / 100

    return investissement, cout_total, profit_total

if __name__ == "__main__":
    filename = "actions.txt"
    budget_max = 500
    actions = lire_actions(filename)

    investissement, cout_total, profit_total = investissement_optimise(actions, budget_max)

    print("Meilleures actions pour maximiser le profit (version optimisée) :")
    for action in investissement:
        print(f"{action[0]} - Coût : {action[1]} euros, Bénéfice : {action[1] * action[2] / 100} euros")

    print(f"\nCout total : {cout_total} euros")
    print(f"Meilleur profit total : {profit_total} euros")


