from InheritanceExercise.projectHero.wizard import Wizard


class DarkWizard(Wizard):
    def __init__(self, usernae, level):
        super(DarkWizard, self).__init__(usernae, level)
