from importlib import util, metadata
import sys
import os  # noqa: F401


def check_in_venv() -> bool:
    try:
        return sys.base_prefix != sys.prefix
    except Exception as error:
        print(f"Error: {error}")
        return False


def check_module(module: str, description: str) -> dict[str, object] | bool:
    try:
        lib = util.find_spec(module)  # se o arquivo tem no pc
        version = metadata.version(module)  # le a versao instalada
        return {
            'module': lib,
            'version': version
        }
    except Exception as error:
        print(f"[ERROR] Failed to verify {module}: {error}")
        return False


def factory_of_data() -> None:
    try:
        import pandas  # type: ignore # noqa: F401
        import numpy  # type: ignore # noqa: F401
        import matplotlib.pyplot as plt  # type: ignore # noqa: F401
        import requests  # type: ignore # noqa: F401
    except (ImportError, ModuleNotFoundError) as error:
        print(f"Import Error: {error} - Please check your instalattion.")
        print("Install dependicies:")
        print("Using pip: pip install -r requirements.txt")
        print("Using poetry: ")
        return

    try:
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        response.raise_for_status()
        users_data = response.json()
        users_names = [user.get("name", "Ubnknown") for user in users_data]
        random_operators = numpy.random.choice(users_names, 1000)
        random_data = numpy.random.randint(1, 1000, 1000)
        dataframe = pandas.DataFrame({
            "name": random_operators,
            "signal": random_data
        })
        filename = "matrix_data.json"
        dataframe.to_json(filename, orient="records", indent=5)
        plt.plot(dataframe["signal"], color='blue', linewidth=1.5)
        plt.title("Matrix Signal Analysis")
        plt.xlabel("Data Point (Index)")
        plt.ylabel("Signal Strength")
        plt.savefig("matrix_analysis.png")
        print("Analyzing Matrix data..")
        print("Processing 1000 data points...")
        print("Generating visualization...")
        print()
        print("Analysis complete!")
        print("Results saved to: matrix_analysis.png}")
        plt.clf()
    except Exception as error:
        print(f"Error: {error}")
        return


def in_matrix() -> None:
    print("LOADING STATUS: Loading programs...")
    print()
    libs: dict[str, str] = {
        "pandas": "Data manipulation ready",
        "requests": "Network access ready",
        "matplotlib": "Visualization ready",
    }
    libs_not_found: list[str] = []
    for module, description in libs.items():
        verify: dict[str, object] | bool = check_module(module, description)
        if isinstance(verify, dict):
            print(f"[OK] {module} ({verify['version']}) - {description}")
        else:
            libs_not_found.append(module)
            print(f"[KO] {module} was not found")
        if libs_not_found:
            print("\nERROR: Missing dependencies.")
            print("Please load the programs into your environment:")
            print("Using pip: pip install -r requirements.txt")
            print("Using poetry: poetry install")
        else:
            print()
            factory_of_data()


def main() -> None:
    in_venv = check_in_venv()
    if in_venv:
        in_matrix()
    else:
        print("LOADING STATUS: Can't load the progams not in the matrix")


if __name__ == "__main__":
    main()
