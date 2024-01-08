import itertools

def lire_actions(filename):
    actions = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            nom, cout, benefice = parts[0], int(parts[1]), float(parts[2].rstrip('%'))
            actions.append((nom, cout, benefice))
    return actions

def meilleures_actions(actions, budget_max):
    meilleures_actions = []
    meilleur_profit = 0
    meilleur_cout_total = 0

    for taille_combinaison in range(1, len(actions) + 1):
        for combinaison in itertools.combinations(actions, taille_combinaison):
            cout_total = sum(action[1] for action in combinaison)
            if cout_total <= budget_max:
                profit_total = sum(action[1] * action[2] / 100 for action in combinaison)
                if profit_total > meilleur_profit:
                    meilleur_profit = profit_total
                    meilleures_actions = combinaison
                    meilleur_cout_total = cout_total

    return meilleures_actions, meilleur_profit, meilleur_cout_total

if __name__ == "__main__":
    filename = "actions.txt"
    budget_max = 500
    actions = lire_actions(filename)

    meilleures_actions, meilleur_profit, meilleur_cout_total = meilleures_actions(actions, budget_max)

    print("Meilleures actions pour maximiser le profit :")
    for action in meilleures_actions:
        print(f"{action[0]} - Coût : {action[1]} euros, Bénéfice : {action[1] * action[2] / 100} euros")

    print(f"\nMeilleur profit total : {meilleur_profit} euros")
    print(f"Cout total : {meilleur_cout_total} euros")



