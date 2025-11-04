from collections.abc import Callable
from enum import StrEnum
import os
import shutil
import subprocess
import sys

class Owner(StrEnum):
    TheBloodMan49 = 'thebloodman49'
    Alugand = 'alugand'
    Sallooh = 'sallooh'
    Theohebert = 'theohebert'

Handler = Callable[[], float] # returns the result (between 0 and 1)

def handler_dispatcher(owner: Owner) -> Handler:
    match owner:
        case Owner.TheBloodMan49: return thebloodman49_handler
        case Owner.Alugand: return alugand_handler
        case Owner.Sallooh: return sallooh_handler
        case Owner.Theohebert: return theoherbert_handler

def thebloodman49_handler() -> float:
    with open(f"{Owner.TheBloodMan49}/associativity/associativity_test_original.txt", "r") as file:
        lines = file.readlines()
        their_result = float(lines[1].split(':')[1].split('%')[0])
        normalized_result = (100.0 - their_result) / 100

        return normalized_result

def alugand_handler() -> float:
    with open(f"{Owner.Alugand}/answer_associativity.txt", "r") as file:
        lines = file.readlines()
        result = float(lines[0])

        return result


def sallooh_handler() -> float:
    with open(f"{Owner.Sallooh}/answer_associativity.txt", "r") as file:
        lines = file.readlines()
        their_result = float(lines[2].split(':')[1].split('%')[0])
        normalized_result = their_result / 100

        return normalized_result

def theoherbert_handler() -> float:
    with open(f"{Owner.Theohebert}/answer_associativity.txt", "r") as file:
        lines = file.readlines()
        their_result = float(lines[3].split(':')[1].split('%')[0])
        normalized_result = their_result / 100
        print(normalized_result)
        return normalized_result

repositories = [
    (Owner.Theohebert, "https://github.com/theohebert/rep-ti"),
    (Owner.Sallooh, "https://github.com/sallooh/rep-INSA"),
    (Owner.Alugand, "https://github.com/alugand/repro-lugand-le_sommer-associativity"),
    (Owner.TheBloodMan49, "https://github.com/TheBloodMan49/S9-Reproductibility-of-experimentations"),
]

our_result = 0.82

for (owner, repo_link) in repositories:
    subprocess.run(["git", "clone", repo_link, str(owner)])
    
    handler = handler_dispatcher(owner)
    if abs(handler() - our_result) >= 0.1:
        print(f"Found a repository with a different result: {repo_link}")
        break
else:
    print("No divergent repository found...")

directories = [
    str(Owner.Theohebert),
    str(Owner.Sallooh),
    str(Owner.Alugand),
    str(Owner.TheBloodMan49),
]

for directory in directories:
    try:
        shutil.rmtree(directory)
    except FileNotFoundError:
        pass