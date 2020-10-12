
from entity import Entity
from statblock import StatBlock


class Animate(Entity):

    def __init__(self, name, id):
        super().__init__(name, id)    # should inherit everything this way
        self.statBlock = StatBlock()  # empty stat block

    def get_stat(self, stat):
        self.statBlock.get_stat(stat)

    def set_stats(self, stat, num, faces=None):
        if faces is None:
            self.statBlock.modify_stat(stat, num)
        else:
            self.statBlock.modify_stat(stat, num, faces)
