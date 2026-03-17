import sys
import os
import site


def check_in_venv() -> bool:
    try:
        return sys.base_prefix != sys.prefix
    except Exception as error:
        print(f"Error: {error}")
        return False


def get_package() -> str:
    try:
        package_paths = site.getsitepackages()
        return package_paths[0]
    except Exception as error:
        return f"Error: {error}"


def main() -> None:
    in_venv: bool = check_in_venv()
    py_path: str = sys.executable
    env_path: str = sys.prefix
    env_name: str = os.path.basename(env_path) if in_venv else "None detected"
    package_paths: str = get_package()
    if in_venv:
        print("MATRIX STATUS: Welcome to the construct")
        print(f"Current Python: {py_path}")
        print(f"Virtual Environment: {env_name}")
        print(f"Environment Path: {env_path}")
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print()
        print("Package installation path:")
        print(f"{package_paths}")
    else:
        print("MATRIX STATUS: You're still plugged in")
        print(f"Current Python: {py_path}")
        print(f"Virtual Environment: {env_name}")
        print()
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env")
        print("Scripts")
        print("activate # On Windows")
        print()
        print("Then run this program again.")


if __name__ == "__main__":
    main()
