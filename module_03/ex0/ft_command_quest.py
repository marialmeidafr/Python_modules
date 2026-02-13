import sys


def main() -> None:
    print("=== Command Quest ===")

    total_args: int = len(sys.argv)
    if total_args < 2:
        print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    if total_args >= 2:
        print(f"Arguments received: {total_args - 1}")
        i: int = 1
        while (i < total_args):
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    print(f"Total arguments: {total_args}")


if __name__ == "__main__":
    main()
