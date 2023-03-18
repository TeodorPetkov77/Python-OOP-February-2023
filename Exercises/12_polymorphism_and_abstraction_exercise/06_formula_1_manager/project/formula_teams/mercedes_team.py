from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    def __init__(self, budget: int):
        super().__init__(budget)

    @property
    def team_expenses(self):
        return 200000

    def calculate_revenue_after_race(self, race_pos: int):
        sponsor_reward = 0
        if race_pos == 1:
            sponsor_reward = 1100000
        elif 1 < race_pos <= 3:
            sponsor_reward = 600000
        elif 3 < race_pos <= 5:
            sponsor_reward = 100000
        elif 5 < race_pos <= 7:
            sponsor_reward = 50000
        revenue = sponsor_reward - self.team_expenses
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. " \
               f"Current budget {self.budget}$"
