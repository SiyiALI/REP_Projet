# Reproducibility

## Installation & execution instructions
- Download and install Python 3.14 from [this link](https://www.python.org/downloads/release/python-3140/) for Windows, or via your package manager on Linux / macOS. We used CPython.
- Clone this repository
- Run the script with `python.exe main.py` (on Windows)
- The result is approximately between 0.8 and 0.85

## TP3

### Factors that influence the evaluation of mathematical properties on floating-point numbers

- Limited precision of floating-point formats
- The way floating points are compared (`a == b`, `abs(a-b) <= 0.001`)
- Use of arbitrary precision / big number libraries
- CPU / processor architecture
- Programming language data types
- The numeric interval selected for the value generation

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
