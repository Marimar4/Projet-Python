import os
import sys

# Ajouter le chemin du projet au PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importer les modules du projet
from importlib import reload
# Importer les modules du projet
from monmodule import declarations as d