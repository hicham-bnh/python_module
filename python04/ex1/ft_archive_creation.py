if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print("Initializing new storage unit: new_discovery.txt")
    try:
        fd = open("new_discovery.txt", "w")
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")
        fd.write("[ENTRY 001] New quantum algorithm discovered\n")
        print("[ENTRY 001] New quantum algorithm discovered")
        fd.write("[ENTRY 002] Efficiency increased by 347%\n")
        print("[ENTRY 002] Efficiency increased by 347%")
        fd.write("[ENTRY 003] Archived by Data Archivist trainee")
        print("[ENTRY 003] Archived by Data Archivist trainee\n")
        fd.close()
        print("Data inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")
    except OSError as e:
        print(e)
