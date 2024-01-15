import itertools

# Fonction pour lire les actions depuis un fichier
def read_actions(filename):
    actions = []
    with open(filename, 'r') as file:
        for line in file:
            # Diviser la ligne en parties en utilisant la virgule comme séparateur
            parts = line.strip().split(',')
            # Extraire les éléments de chaque partie
            name, cost, benefit = parts[0], int(parts[1]), float(parts[2].rstrip('%'))
            # Ajouter les informations dans la liste des actions
            actions.append((name, cost, benefit))
    return actions

# Fonction pour trouver les actions optimales pour maximiser le profit
def optimal_actions(actions, max_budget):
    best_actions = []  # Liste pour stocker les meilleures actions
    best_profit = 0  # Variable pour stocker le meilleur profit
    best_total_cost = 0  # Variable pour stocker le meilleur coût total

    # Boucle sur toutes les tailles possibles de combinaisons d'actions
    for combination_size in range(1, len(actions) + 1):
        # Générer toutes les combinaisons possibles d'actions de la taille actuelle
        for combination in itertools.combinations(actions, combination_size):
            # Calculer le coût total de la combinaison
            total_cost = sum(action[1] for action in combination)
            # Vérifier si le coût total est inférieur ou égal au budget maximal
            if total_cost <= max_budget:
                # Calculer le profit total de la combinaison
                total_profit = sum(action[1] * action[2] / 100 for action in combination)
                # Mettre à jour les meilleures actions et le meilleur profit si nécessaire
                if total_profit > best_profit:
                    best_profit = total_profit
                    best_actions = combination
                    best_total_cost = total_cost

    # Retourner les meilleures actions, le meilleur profit et le meilleur coût total
    return best_actions, best_profit, best_total_cost

# Point d'entrée du script
if __name__ == "__main__":
    # Fichier contenant les données des actions
    filename = "actions.txt"
    # Budget maximal pour l'investissement
    max_budget = 500
    # Lire les actions depuis le fichier
    actions = read_actions(filename)

    # Trouver les actions optimales pour maximiser le profit
    best_actions, best_profit, best_total_cost = optimal_actions(actions, max_budget)

    # Afficher les résultats
    print("Meilleures actions pour maximiser le profit :")
    for action in best_actions:
        print(f"{action[0]} - Coût : {action[1]} euros, Bénéfice : {action[1] * action[2] / 100} euros")

    print(f"\nMeilleur profit total : {best_profit} euros")
    print(f"Coût total : {best_total_cost} euros")





