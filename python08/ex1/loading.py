import importlib
import sys


if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
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
    print("Analyzing Matrix data...")
    try:
        n = int(sys.argv[1])
        print(f"Processing {n} data points...")
        print("Generating visualization...\n")
    except Exception:
        print("No data points plaese put data...")
        sys.exit(1)
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")
    print("Generating visualization...")

    data = np.random.randn(1000)
    df = pd.DataFrame({"signal": data})

    plt.figure()
    plt.plot(df["signal"])
    plt.tight_layout()
    plt.savefig("matrix_analysis.png")

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")
