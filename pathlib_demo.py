# Execute pathlib demos and tests
from pathlib import *

print(f"{Path('.')}")
p = Path('.')
print(f"{p}")
list(p.glob('**/*.py'))
