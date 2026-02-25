import sys, site, os

if __name__ == "__main__":
    if (sys.prefix == sys.base_prefix):
        print("MATRIX STATUS: You're still plugged in")
        print(f"Current Python: {sys.version}")
        print("Virtual Environment: None detected")
    else:
        print("MATRIX STATUS: Welcome to the construct")
        print(f"Current Python: {sys.path}")