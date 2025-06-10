import pandas

DATA = "50_states.csv"

class CsvHelper:

    def __init__(self):
        self.data = pandas.read_csv(DATA)

    def state_exists(self, answer):
        if self.data.state.isin([answer]).any():
            return True
        else:
            return False

    def get_x_y(self, state):
        x = self.data[self.data["state"] == state]["x"].item()
        y = self.data[self.data["state"] == state]["y"].item()
        return x, y