from InheritanceExercise.projectHero.dark_wizard import DarkWizard


class SoulMaster(DarkWizard):
    def __init__(self, username, level):
        super(SoulMaster, self).__init__(username, level)
