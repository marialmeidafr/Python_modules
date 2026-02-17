def recover_text(filename: str) -> None:
    """read and display file content with manual resource management"""
    file = None
    try:
        file = open(filename, 'r')
        print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
        print(f"Accessing Storage Vault: {filename}")
        print("Connection established...")
        print()
        print("RECOVERED DATA:")
        print(file.read())
        print("Data recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
    except Exception as error:
        print(f"An unexpected corruption occurred: {error}")
    finally:
        if file:
            file.close()


if __name__ == "__main__":
    recover_text("ancient_fragment.txt")
