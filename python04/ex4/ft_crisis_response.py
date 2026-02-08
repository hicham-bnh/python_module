if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    try:
        print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
        with open("lost_archive.txt", "r") as fd:
            file = fd.read()
            print("file open with succes")
            fd.close()
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    finally:
        print("STATUS: Crisis handled, system stable")
    try:
        print("\nCRISIS ALERT: Attempting access to 'classified_vault.txt'...")
        with open("classified_vault.txt", "r") as fd2:
            file = fd2.read()
            print("file open with succes")
            fd2.close()
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    finally:
        print("STATUS: Crisis handled, security maintained")
    print("\nROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    try:
        with open("standard_archive.txt", "r") as fd3:
            file = fd3.read()
            print(f"SUCCESS: Archive recovered - ``{file}''")
            fd3.close()
    except Exception as e:
        print(e)
    finally:
        print("STATUS: Normal operations resumed")
    print()
    print("All crisis scenarios handled successfully. Archives secure.")
