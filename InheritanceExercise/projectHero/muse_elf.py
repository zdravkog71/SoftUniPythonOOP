from InheritanceExercise.projectHero.elf import Elf


class MuseElf(Elf):
    def __init__(self, username, level):
        super(MuseElf, self).__init__(username, level)
