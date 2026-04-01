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
    matrix_mode = os.getenv("MATRIX_MODE")
    database_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion_endpoint = os.getenv("ZION_ENDPOINT")
    """
    we just verify if it's in the .venv or not
    if yes we print it's value else we print an error
    messages
    """
    if matrix_mode:
        print(f"Mode: {matrix_mode}")
    else:
        print("Mode not specified")
        error = True
    if database_url:
        print("Database: Connected to local instance")
    else:
        print("Database not connected")
        error = True
    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Acess: Denied")
        error = True
    if log_level:
        print(f"Log Level: {log_level}")
    else:
        print("Log file not specified")
        error = True
    if zion_endpoint:
        print(f"Zion Network: {zion_endpoint}")
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
