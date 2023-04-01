from project.delicacies.delicacy import Delicacy


class Stolen(Delicacy):
    @property
    def portion(self):
        return 250

    def details(self):
        return f"Stolen {self.name}: {self.portion}g - {self.price:.2f}lv."
