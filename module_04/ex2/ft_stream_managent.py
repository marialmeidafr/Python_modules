import sys


def manage_streams() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    print()
    try:
        arch_id: str = input("Input Stream active. Enter archivist ID: ")
        status: str = input("Input Stream active. Enter status report: ")
        print()
    except (KeyboardInterrupt, EOFError):
        print("[System] Manual shutdown initiated.", file=sys.stderr)
    else:
        print(f"[STANDARD] Archive status from {arch_id}: {status}")
        print(
            "[ALERT] System diagnostic: Communication channels verified",
            file=sys.stderr
        )
        print("[STANDARD] Data transmission complete")
        print()
        print("Three-channel communication test successful.")


if __name__ == "__main__":
    manage_streams()
