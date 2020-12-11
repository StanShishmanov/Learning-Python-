from project.elf import Elf


class MuseElf(Elf):
    def __init__(self, username, level):
        super().__init__(username, level)

#
# hero = Hero("H", 4)
# print(hero.username)
# print(hero.level)
# print(str(hero))
# elf = Elf("E", 4)
# print(str(elf))
# print(elf.__class__.__bases__[0].__name__)
# print(elf.username)
# print(elf.level)
#
# muse_elf = MuseElf("Muse Elf", 12)
# print(str(muse_elf))
# print(muse_elf.__class__.__bases__[0].__name__)
# print(muse_elf.username)
# print(muse_elf.level)