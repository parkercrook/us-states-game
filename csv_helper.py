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

    def create_missing_states_csv(self, correct_guesses):
        data_dict = {
            "Missing State": []
        }
        for state in self.data["state"]:
            if state not in correct_guesses:
                data_dict["Missing State"].append(state)

        df = pandas.DataFrame(data_dict)
        df.to_csv("missing_states.csv")