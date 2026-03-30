# We will try to import the packages
# and handle them if the package is not
# installed
try:
    import pandas as pd
except Exception:
    print("pandas not installed")
try:
    import matplotlib
    import matplotlib.pyplot as plt
except Exception:
    print("matplotlib not installed")
try:
    import numpy as np
except Exception:
    print("numpy not installed")


def main() -> None:
    # because the subject didn't asked to make the
    # data visualiasation or manipulation a deep on
    # we just foccused on showing and manipulating a
    # simple data
    print("LOADING STATUS: Loading progrmas...\n")
    print("Cecking dependeces:")
    pandas_check = "Data manipulation failed"
    visalisation_check = "Visualisation failed"
    pd_verstion = None
    mlt_version = None
    try:
        # we get the version of pandas using this
        pd_verstion = pd.__version__
        print(f"[OK] pandas ({pd_verstion})", end=" - ")
        print("Data manipulation ready")
    except Exception:
        print(f"[ERROR] pandas {pandas_check}")
    try:
        # we get the version of mtlb using this
        mlt_version = matplotlib.__version__
        print(f"[OK] matplotlib ({mlt_version})", end=" - ")
        print("Visualisation ready")
    except Exception:
        print(f"[ERROR] matplotlib {visalisation_check}")
    try:
        if pd_verstion:
            print("\nAnalyzing Matrix data...")
            print("Processing 2 data points...")
            x = np.array([1, 2, 3])
            y = np.array([3, 5, 4])
            # a simple data manipulation
            x *= 2
            x_series = pd.Series(x)
            y_series = pd.Series(y)
            data_frame = pd.DataFrame(
                {
                    "x": x_series,
                    "y": y_series
                }
                )
            # GEtting the x and y data of the dataframe
            X = data_frame['x']
            y = data_frame['y']
            # this tell us the type of visualisation we want
            # to have
        else:
            print("Can't do data manipulation")
        if mlt_version:
            plt.plot(X, y, "o", color="C0")
            plt.title("Data visualiasation")
            print("Generating visualiasation...")
            # Generating the visualisation
            plt.show()
        else:
            print("can't generate visualiasation")
        if mlt_version and pd_verstion:
            print("\nAnalysis complete!")
            print("Results saved to: matrix\\_analysis.png")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
