import sys
from pathlib import Path

project_root = str(Path(__file__).parent.absolute())
if project_root not in sys.path:
    sys.path.append(project_root)

from IsingCorrelationsSolver import IsingCorrelationsSolver
from HeisenbergCorrelationSolver import HeisenbergCorrelationSolver
from SpinCorrelationSolver import SpinCorrelationSolver