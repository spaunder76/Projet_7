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

# Fonction pour l'investissement optimisé avec programmation dynamique
def optimized_investment(actions, max_budget):
    n = len(actions)
    dp = []
    for i in range(n + 1):
        row = [0] * (max_budget + 1)
        dp.append(row)

    for i in range(1, n + 1):
        for j in range(max_budget + 1):
            current_action = actions[i - 1]
            action_cost = int(current_action[1])  # Convertir le coût en entier
            action_benefit = current_action[2] / 100

            if action_cost <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - action_cost] + action_cost * action_benefit)
            else:
                dp[i][j] = dp[i - 1][j]

    # Retracer les actions sélectionnées
    selected_actions = []
    i, j = n, max_budget
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_actions.append(actions[i - 1])
            j -= int(actions[i - 1][1])  # Convertir le coût en entier
        i -= 1

    return selected_actions, dp[n][max_budget]

# Point d'entrée du script
if __name__ == "__main__":
    # Fichier contenant les données des actions
    filename = "actions.txt"
    # Budget maximal pour l'investissement
    budget_max = 500
    # Lire les actions depuis le fichier
    actions = read_actions(filename)

    # Calculer l'investissement optimisé
    investment, total_profit = optimized_investment(actions, budget_max)

# Afficher les résultats
print("Meilleures actions pour maximiser le profit (version optimisée) :")
total_cost = sum(action[1] for action in investment)
for action in investment:
    print(f"{action[0]} - Coût : {action[1]} euros, Bénéfice : {action[1] * action[2] / 100} euros")

print(f"\nCoût total des actions achetées : {total_cost} euros")
print(f"Meilleur profit total : {total_profit} euros")









