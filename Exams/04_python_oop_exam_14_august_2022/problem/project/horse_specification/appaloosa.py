from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    @property
    def max_speed(self):
        return 120

    @property
    def speed_per_training(self):
        return 2
