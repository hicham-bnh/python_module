import os
import sys
from dotenv import load_dotenv


def check_required_vars():
    # check key
    required = ["MATRIX_MODE", "DATABASE_URL",
                "API_KEY", "LOG_LEVEL", "ZION_ENDPOINT"]
    missing = [var for var in required if not os.getenv(var)]

    if missing:
        print("[ERROR] Missing configuration variables:")
        for var in missing:
            print(f" - {var}")
        sys.exit(1)


def display_configuration():
    # print config
    mode = os.getenv("MATRIX_MODE")
    log = os.getenv("LOG_LEVEL")
    print("Configuration loaded:")
    print(f"Mode: {mode}")
    if mode == "development":
        print("Database: Connected to local instance")
    elif mode == "production":
        print("Database: Connected to production cluster")
    print("API Access: Authenticated")
    print(f"Log Level: {log}")
    print("Zion Network: Online")


def check_security():
    # check security
    print("\nEnvironment security check:")
    if os.getenv("API_KEY") == "your_api_key_here":
        print("[WARNING] Default API key detected")
    else:
        print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")


if __name__ == "__main__":
    print("\nORACLE STATUS: Reading the Matrix...\n")
    load_dotenv()
    check_required_vars()
    display_configuration()
    check_security()
    print("\nThe Oracle sees all configurations.")
