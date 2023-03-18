from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    def __init__(self, budget: int):
        super().__init__(budget)

    @property
    def team_expenses(self):
        return 250000

    def calculate_revenue_after_race(self, race_pos: int):
        sponsor_reward = 0
        if race_pos == 1:
            sponsor_reward = 1520000
        elif race_pos == 2:
            sponsor_reward = 820000
        elif 2 < race_pos <= 8:
            sponsor_reward = 20000
        elif 8 < race_pos <= 10:
            sponsor_reward = 10000
        revenue = sponsor_reward - self.team_expenses
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. " \
               f"Current budget {self.budget}$"