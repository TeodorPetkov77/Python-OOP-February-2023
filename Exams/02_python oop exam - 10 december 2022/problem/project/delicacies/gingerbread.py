from project.delicacies.delicacy import Delicacy


class Gingerbread(Delicacy):
    @property
    def portion(self):
        return 200

    def details(self):
        return f"Gingerbread {self.name}: {self.portion}g - {self.price:.2f}lv."
