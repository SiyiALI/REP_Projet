# Reproducibility

## Structure des dossiers
```bash
#Branchs
Branch 
 ├─ main
 ├─ Associativity_solution2  # change in main.py            
 └─ Banking_solution2        # change in BankingProblem/MainBanking.py   


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
 |    ├─ jinja_call.py
 |    └─ results_banking.csv
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
