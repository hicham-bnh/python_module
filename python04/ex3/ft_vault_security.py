if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    try:
        with open("classified_data.txt", "r") as fd1:
            print("Initiating secure vault access...")
            print("Vault connection established with failsafe protocols")
            print("\nSECURE EXTRACTION:")
            file = fd1.read()
            print(file)
            print()
            fd1.close()
        with open("security_protocols.txt", "r") as fd2:
            print("SECURE PRESERVATION:")
            file2 = fd2.read()
            print(file2)
            print("Vault automatically sealed upon completion")
            fd2.close()
        print("\nAll vault operations completed with maximum security.")
    except OSError as e:
        print(e)
