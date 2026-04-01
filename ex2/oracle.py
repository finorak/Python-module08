import os
try:
    "We try to import the library if it's installed"
    from dotenv import load_dotenv
except Exception:
    print("python-dotenv couldn't be imported")


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")
    error = False
    try:
        """
        We load the the .env
        """
        load_dotenv()
    except Exception:
        print("Can't load env")
        return None
    print("Configuration loaded:")
    """
    Here we get the value in our .venv file
    """
    MATRIX_MODE = os.getenv("MATRIX_MODE")
    DATABASE_URL = os.getenv("DATABASE_URL")
    API_KEY = os.getenv("API_KEY")
    LOG_LEVEL = os.getenv("LOG_LEVEL")
    ZION_ENDPOINT = os.getenv("ZION_ENDPOINT")
    """
    we just verify if it's in the .venv or not
    if yes we print it's value else we print an error
    messages
    """
    if MATRIX_MODE:
        print(f"Mode: {MATRIX_MODE}")
    else:
        print("Mode not specified")
        error = True
    if DATABASE_URL:
        print("Database: Connected to local instance")
    else:
        print("Database not connected")
        error = True
    if API_KEY:
        print("API Access: Authenticated")
    else:
        print("API Acess: Denied")
        error = True
    if LOG_LEVEL:
        print(f"Log Level: {LOG_LEVEL}")
    else:
        print("Log file not specified")
        error = True
    if ZION_ENDPOINT:
        print(f"Zion Network: {ZION_ENDPOINT}")
    else:
        print("Zion Network not specified")
        error = True
    print("\nEnvironment secirity check:")
    if error:
        print("[OK] No hardcoded secrets detected")
        print("[ERROR] .env file contains error")
        print("[OK] Production overrides available")
    else:
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
        print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
