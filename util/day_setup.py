import argparse
import os

# settings.py
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(f"{dirname(__file__)}", "..", ".env.local")
puzzle_day_path = join(f"{dirname(__file__)}", "..", "days")
load_dotenv(dotenv_path)

print(dotenv_path)


def main():
    parser = argparse.ArgumentParser(
        description="A simple script to setup your day for solving!"
    )

    # Add arguments
    parser.add_argument(
        "day", help="Required field for the day - please prefix with 0 if singular"
    )

    args = parser.parse_args()
    day = args.day
    day_folder = f"{puzzle_day_path}/day_{day}"

    # Create day directory if it doesn't exist.
    if not os.path.exists(day_folder):
        os.makedirs(day_folder)
        print(f"Directory '{day_folder}' created successfully.")
    else:
        print(f"Directory '{day_folder}' already exists.")

    # Create the text file for the input
    input_filename = f"input_{day}.txt"
    with open(f"{day_folder}/{input_filename}", "w") as input_file:
        input_file.write(f"This is the input file for {day}")

    # Create main.py file
    main_content = """from util import models


def main():
    Puzzle = models.Puzzle("01")
    print(Puzzle.data)


if __name__ == "__main__":
    main()"""
    with open(f"{day_folder}/main.py", "w") as main_file:
        main_file.write(main_content)

    # Create README.md file
    readme_content = """# Readme File
This is a README file for the project."""
    with open(f"{day_folder}/README.md", "w") as readme_file:
        readme_file.write(readme_content)


if __name__ == "__main__":
    main()
