# Reproductibilité

## Instructions d'installation et d'exécution
- Télécharger et installer Python 3.14 depuis [ce lien](https://www.python.org/downloads/release/python-3140/) pour Windows, ou depuis votre package manager pour Linux / MacOS. Nous avons utilisé CPython.
- Cloner ce dépôt
- Lancer le script avec la commande `python.exe main.py` (Windows)
- Le résultat est à peu près entre 0.8 et 0.85

## TP3

### Facteurs impactant l'évaluation des propriétés mathématiques sur les flottants

- Précision limitée des flottants
- Manière de comparer les flottants (`a==b`, `abs(a-b) <= 0.001`)
- Utilisation d'une bibliothèque de grands nombres (précision arbitraire)
- Architecture du processeur
- Type de données des langages de programmation
- L'intervalle choisi pour la génération des nombres

## Structure des dossiers
```bash
#Branchs
Branch 
 ├─ main
 ├─ use_float32            
 └─ solution2         


REP_Projet/
 ├─ .github/workflows/
 |    ├─ associativity.yml
 |    └─ banking.yml          
 ├─ banking_problem/
 |    ├─ banking_algorithm.py
 |    ├─ banking_cli_laucher.py
 |    ├─ banking_cli.py
 |    ├─ banking_template.py.jinja
 |    ├─ generate_csv.py
 |    └─ jinja_call.py
 ├─ associativity/
 |    ├─ associativity_cli_launcher.py
 |    ├─ associativity_cli.py
 |    ├─ associativity_template.py.jinja
 |    ├─ generate_csv.py
 |    ├─ jinja_call.py
 |    ├─ repository_scanner.py
 |    ├─ results_associativity.csv
 |    └─ tp1.py 
 ├─ .gitignore
 ├─ answer_associativity.py
 ├─ Dockerfile
 ├─ nixpkgs-pin.nix
 ├─ README.md
 ├─ Result_Analyse.ipynb           
 └─ shell.nix