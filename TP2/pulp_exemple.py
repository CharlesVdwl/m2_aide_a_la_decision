from pulp import *

if __name__ == '__main__':
    # Paramètres
    n_caoutchouc = 400
    n_acier = 600
    prix_citadine = 10000
    prix_suv = 16000

    # Définition des variables
    x = LpVariable('x', lowBound=0, cat=LpInteger)
    y = LpVariable('y', lowBound=0, cat=LpInteger)

    # Problème
    probleme = LpProblem(name='chiffre_affaires', sense=LpMaximize)

    # Contraintes
    contrainte_caoutchouc = LpConstraint(e=x + y, sense=LpConstraintLE, name='contrainte_caouthouc', rhs=n_caoutchouc)
    probleme.add(contrainte_caoutchouc)
    contrainte_acier = LpConstraint(e=2 * x + y, sense=LpConstraintLE, name='contrainte_acier', rhs=n_acier)
    probleme.add(contrainte_acier)
    # ou bien ecrire ...
    # probleme += (x+y <= n_caoutchouc)
    # probleme += (2*x+y <= n_acier)

    # Fonction objectif
    fonction_objectif = LpAffineExpression(e=prix_suv*x + prix_citadine*y)
    probleme.setObjective(fonction_objectif)
    # ou bien ecrire ...
    # probleme += prix_suv*x + prix_citadine*y

    # Résolution
    probleme.solve(COIN_CMD())
    # ou utiliser autre solveurs ...
    # probleme.solve(GLPK_CMD())
    # probleme.solve(GUROBI_CMD())
    # probleme.solve(CPLEX_CMD())

    # solver = PULP_CBC_CMD(timeLimit=20, msg=True)
    # probleme.solve(solver=solver)

    # Résultat
    print(f'x = {x.value()}')
    print(f'y = {y.value()}')
    print(f"status = {LpStatus[probleme.status]}")
