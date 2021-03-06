from views import MainMenu
from repositories import CategoryRepository, EntryRepository, RaportRepository


class Application:
    def main(self):
        menu = MainMenu()
        menu.draw()

        category_repository = self.get_category_repository()
        entry_repository = self.get_entry_repository()
        raport_repository = self.get_raport_repository()
        screen = menu.get_screen()
        screen.set_repository('category', category_repository)
        screen.set_repository('entry', entry_repository)
        screen.set_repository('raport', raport_repository)
        screen.draw()

    def get_entry_repository(self):
        return EntryRepository()

    def get_category_repository(self):
        return CategoryRepository()

    def get_raport_repository(self):
        return RaportRepository()


if __name__ == '__main__':
    app = Application()
    app.main()

