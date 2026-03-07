import importlib
import sys


def check():
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    # try to import some module
    try:
        pandas = importlib.import_module("pandas")
        print(f"[OK] pandas ({pandas.__version__})")
    except Exception as e:
        print(e)
    try:
        requests = importlib.import_module('requests')
        print(f"[OK] requests ({requests.__version__})")
    except Exception as e:
        print(e)
    try:
        matplotlib = importlib.import_module('matplotlib')
        print(f"[OK] matplotlib ({matplotlib.__version__})\n")
    except Exception as e:
        print(e)
        print("\nfor installing package do this :")
        print("pip install -r requirements.txt")
        print("or")
        print("poetry install")
        sys.exit(1)


if __name__ == "__main__":
    check()
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd
    print("Analyzing Matrix data...")
    try:
        print("Processing 600 data points...")
        print("Generating visualization...\n")
        data = np.random.randn(600)
        df = pd.DataFrame({"signal": data})
        plt.figure()
        plt.plot(df["signal"])
        plt.tight_layout()
        plt.savefig("matrix_analysis.png")
    except Exception as e:
        print(e)
        sys.exit(1)
