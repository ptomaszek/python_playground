import glob
from pathlib import Path

source_dir = '/home/ac/notes'

for filepath in glob.glob(f"{source_dir}/**", recursive=True):
    path = Path(filepath)
    if path.is_file() and not path.suffix:
        print(path)
        # path.rename(f"{path}.txt")
