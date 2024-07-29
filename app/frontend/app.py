import sys
import os

# Adiciona o diretório raiz do projeto ao PYTHONPATH
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
sys.path.insert(0, project_root)

from automata_app import AutomataApp  

if __name__ == "__main__":
    AutomataApp()
