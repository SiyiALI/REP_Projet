# Reproducibility

This project uses Python 3.14 (CPython).

## Branchs
```bash

Branch 
 ├─ main
 ├─ Associativity_solution2    # change in main.py            
 └─ Banking_solution2          # change in BankingProblem/MainBanking.py   

```

## Folder structure
```bash

REP_Projet/
 ├─ .github/workflows/                   # CI pipelines (GitHub Actions)
 │    ├─ associativity.yml               # CI that runs the associativity computations
 │    └─ banking.yml                     # CI that runs the banking computations
 │
 ├─ banking_problem/                     # banking algorithm + CLI + CSV generation
 │    ├─ banking_algorithm.py            # prototype / first version of the banking problem code
 │    ├─ banking_cli_laucher.py          # entry point wrapper to launch the CLI
 │    ├─ banking_cli.py                  # argument parsing / CLI interface
 │    ├─ banking_template.py.jinja       # Jinja template for code / output generation
 │    ├─ generate_csv.py                 # runs experiments and writes a CSV
 │    └─ jinja_call.py                   # helpers to call Jinja templates
 │
 ├─ associativity/                       # associativity experiment + CLI + CSV generation
 │    ├─ associativity_cli_launcher.py   # entry point wrapper to launch the CLI
 │    ├─ associativity_cli.py            # argument parsing / CLI interface
 │    ├─ associativity_template.py.jinja # Jinja template for the associativity study
 │    ├─ generate_csv.py                 # runs experiments and writes a CSV
 │    ├─ jinja_call.py                   # helpers to call Jinja templates
 │    ├─ repository_scanner.py           # scans directories / repositories for analysis
 │    ├─ results_associativity.csv       # precomputed results
 │    └─ tp1.py                          # prototype / first version of the associativity code
 │
 ├─ .gitignore                           # ignore rules
 ├─ answer_associativity.py              # standalone script with the associativity result
 ├─ Dockerfile                           # containerised execution environment
 ├─ nixpkgs-pin.nix                      # pinned version for reproducible Nix environment
 ├─ README.md                            # this documentation file
 ├─ Result_Analyse.ipynb                 # Jupyter notebook for analysis / plots
 └─ shell.nix                            # development environment (Nix shell)

```
