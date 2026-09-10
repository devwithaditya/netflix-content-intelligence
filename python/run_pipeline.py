import subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parent
for script in ["01_data_cleaning.py", "02_feature_engineering.py", "03_eda.py"]:
    print("\nRunning", script)
    subprocess.run(["python", str(ROOT/script)], check=True)
print("\nFULL ANALYTICS PIPELINE COMPLETED SUCCESSFULLY")
