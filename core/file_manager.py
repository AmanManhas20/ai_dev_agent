import os


GENERATED_DIR = "generated_code"
SOLUTION_FILE = "solution.py"


def ensure_directory():
    """
    Ensure generated_code directory exists
    """

    if not os.path.exists(GENERATED_DIR):
        os.makedirs(GENERATED_DIR)


def get_solution_path():
    """
    Return full path to the generated solution file
    """

    ensure_directory()
    return os.path.join(GENERATED_DIR, SOLUTION_FILE)


def save_code(code: str):
    """
    Save generated Python code into solution file
    """

    if not code or len(code.strip()) == 0:
        raise ValueError("Cannot save empty code")

    path = get_solution_path()

    with open(path, "w", encoding="utf-8") as file:
        file.write(code)

    print(f"[FileManager] Code saved to {path}")


def read_code():
    """
    Read generated code from solution file
    """

    path = get_solution_path()

    if not os.path.exists(path):
        raise FileNotFoundError("Generated solution file does not exist")

    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def delete_code():
    """
    Delete generated solution file if needed
    """

    path = get_solution_path()

    if os.path.exists(path):
        os.remove(path)
        print("[FileManager] solution.py deleted")
    else:
        print("[FileManager] No solution file to delete")