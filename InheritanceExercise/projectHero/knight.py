from InheritanceExercise.projectHero.hero import Hero


class Knight(Hero):
    def __init__(self, username, level):
        super(Knight, self).__init__(username, level)
