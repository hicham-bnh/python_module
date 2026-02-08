if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print("Accessing Storage Vault: ancient_fragment.txt")
    try:
        fd = open('ancient_fragment.txt', 'r')
        print("Connection established...\n")
        file = fd.read()
        print("RECOVERED DATA:")
        print(file)
        fd.close()
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
    except OSError as e:
        print(e)
