from InheritanceExercise.projectHero.hero import Hero


class Wizard(Hero):
    def __init__(self, username, level):
        super(Wizard, self).__init__(username, level)
