# Fonction pour lire les actions depuis un fichier
def read_actions(filename):
    actions = []
    with open(filename, 'r') as file:
        # Ignorer la première ligne (en-tête)
        next(file)
        for line in file:
            # Diviser la ligne en parties en utilisant la virgule comme séparateur
            parts = line.strip().split(',')
            # Extraire les éléments de chaque partie
            name, cost, benefit = parts[0], float(parts[1]), float(parts[2].rstrip('%'))
            # Ajouter les informations dans la liste des actions
            actions.append((name, cost, benefit))
    return actions

# Fonction pour l'investissement optimisé
def optimized_investment(actions, max_budget):
    # Trier les actions en fonction du rapport bénéfice/coût de manière décroissante
    sorted_actions = sorted(actions, key=lambda x: x[2] / x[1] if x[1] != 0 else 0, reverse=True)
    investment = []
    total_cost = 0
    total_profit = 0

    # Sélectionner les actions pour l'investissement en respectant le budget maximal
    for action in sorted_actions:
        # Calculer le bénéfice potentiel si l'action est achetée
        potential_profit = action[1] * action[2] / 100
        # Vérifier si l'achat de l'action respecte le budget maximal
        if action[1] != 0 and total_cost + action[1] <= max_budget:
            # Si l'achat respecte le budget, ajouter l'action à l'investissement
            investment.append(action)
            total_cost += action[1]
            total_profit += potential_profit

    return investment, total_cost, total_profit


# Point d'entrée du script
if __name__ == "__main__":
    # Fichier contenant les données des actions
    filename = "actions.txt"
    # Budget maximal pour l'investissement
    budget_max = 500
    # Lire les actions depuis le fichier
    actions = read_actions(filename)

    # Calculer l'investissement optimisé
    investment, total_cost, total_profit = optimized_investment(actions, budget_max)

    # Afficher les résultats
    print("Meilleures actions pour maximiser le profit (version optimisée) :")
    for action in investment:
        print(f"{action[0]} - Coût : {action[1]} euros, Bénéfice : {action[1] * action[2] / 100} euros")

    print(f"\nCoût total : {total_cost} euros")
    print(f"Meilleur profit total : {total_profit} euros")




