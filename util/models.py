import os


class Puzzle:
    def __init__(self, day):
        self.day = day
        # Works for this project, but not if run outside
        self.root = os.path.abspath(os.curdir)
        self.data = self.load_data()

    def load_data(self):
        input_path = f"{self.root}/days/day_{self.day}/input_{self.day}.txt"
        try:
            with open(input_path, "r") as file:
                data = file.read()
                return data
        except FileNotFoundError:
            return f"No input data found for {self.day}"
