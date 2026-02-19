def response_system(files: list[str]) -> None:
    """This function iterates through a list of file paths,
    attempting to extract and display their content."""
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    print()

    for file_path in files:
        try:
            if file_path == "standard_archive.txt":
                print(f"ROUTINE ACCESS: Attempting access to '{file_path}'...")
            else:
                print(f"CRISIS ALERT: Attempting access to '{file_path}'...")
            with open(file_path, 'r') as vault:
                content = vault.read().strip()
                print(f"SUCCESS: Archive recovered - ``{content}''")
                print("STATUS: Normal operations resumed")
                print()
        except FileNotFoundError:
            print("RESPONSE: Archive not found in storage matrix")
            print("STATUS: Crisis handled, system stable")
            print()
        except PermissionError:
            print("RESPONSE: Security protocols deny access")
            print("STATUS: Crisis handled, security maintained")
            print()
        except Exception as error:
            print(f"RESPONSE: Unexpected error: {error}")
            print("STATUS: System unstable, check protocols")
            print()
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    files = [
        "lost_archive.txt",
        "classified_vault.txt",
        "standard_archive.txt"
    ]
    response_system(files)
