import sys
import os


def main() -> None:
    # sys.prefic is the current environment we are in
    # base_prefix is the base environment for all python
    # packages that doesn't run on a custom virtual environment

    # here we check if the current evironment is the same
    # as the base environment
    venv = 'None detected'
    # the current python path (the executable)
    python_path = sys.executable
    # we use this to detect if we're on a venv or not
    # None if global
    warning = None
    if sys.prefix != sys.base_prefix:
        # if it's not the same environment (custom venv)
        print("MATRIX STATUS: Welcome to the construct\n")
        venv = os.path.basename(sys.prefix)
    else:
        print("MATRIX STATUS: You're still plugged in\n")
        warning = "You're in the global environment"
        # otherwise we print do this
    print(f"Current Python: {python_path}")
    print(f"Virtual Environment: {venv}\n")
    if warning is not None:
        print(f"Warning: {warning}")
        print("The machine can see everything you install.")
        print("To enter construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env")
        print("Scripts")
        print("activate # On Windows\n")
        print("Then run this program again.")
    else:
        print("You're in an isolated environment!")
        print("Safe to install packages withou", end=" ")
        print("affecting the global system.")
        print()
        print("Package installation path")


if __name__ == "__main__":
    main()
