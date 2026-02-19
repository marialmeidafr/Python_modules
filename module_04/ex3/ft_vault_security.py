def security_system(filename: str) -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print()
    print("Initiating secure vault access...")
    try:
        with open(filename, 'r') as file:
            print("Vault connection established with failsafe protocols")
            print()
            print("SECURE EXTRACTION:")
            content = file.read()
            print(content)
            print()
        with open(filename, 'w') as file:
            print("SECURE PRESERVARION:")
            text: str = "[CLASSIFIED] New security keys recovered"
            file.write(text)
            print(text)
        print("Vault automatically sealed upon completion")
        print()
        print("All vault operations completed with maximum security.")
    except FileNotFoundError:
        print(f"CRISIS: Access failed - Vault '{filename}' not found.")
    except Exception as error:
        print(f"CRITICAL: Unexpected security breach: {error}")


if __name__ == "__main__":
    security_system("classified_data.txt")
