# Reproductibilité

## Instructions d'installation et d'exécution
- Télécharger et installer Python 3.14 depuis [ce lien](https://www.python.org/downloads/release/python-3140/)
- Cloner ce dépôt
- Lancer le script avec la commande `python.exe main.py`
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
 |    ├─ test.yml
 |    └─ banking.yml          
 ├─ BankingProblem/
 |    ├─ banking_cli_laucher.py
 |    ├─ banking_cli.py
 |    ├─ banking_template.py.jinja
 |    ├─ generate_banking_0.py
 |    ├─ ......
 |    ├─ generate_banking_2.py
 |    └─ MainBanking.py           
 ├─ AssociativeProblem/
 |    ├─ generated_property_check_0.py
 |    ├─ ......
 |    ├─ generated_property_check_53.py
 |    ├─ jinja_call.py
 |    ├─ main_cli_laucher.py
 |    ├─ main_cli.py
 |    ├─ main.py
 |    └─ property_template.py.jinja
 ├─ .gitignore
 ├─ README.md
 └─ Result_Analyse.ipynb           
