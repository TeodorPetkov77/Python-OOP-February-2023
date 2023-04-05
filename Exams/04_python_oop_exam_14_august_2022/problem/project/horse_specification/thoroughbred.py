from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    @property
    def max_speed(self):
        return 140

    @property
    def speed_per_training(self):
        return 3
