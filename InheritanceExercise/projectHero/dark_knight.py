from InheritanceExercise.projectHero.knight import Knight


class DarkKnight(Knight):
    def __init__(self, username, level):
        super(DarkKnight, self).__init__(username, level)
