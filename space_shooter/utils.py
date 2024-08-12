import os

def read_high_score(file_path):
    """Read the high score from the file."""
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return int(file.read().strip() or 0)
    return 0

def write_high_score(file_path, score):
    """Write the high score to the file."""
    with open(file_path, "w") as file:
        file.write(str(score))
