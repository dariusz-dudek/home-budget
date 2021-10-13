from views import MainMenu


class Application:
    @staticmethod
    def main():
        menu = MainMenu()
        menu.draw()

        option = menu.get_screen()
        option.draw()


if __name__ == '__main__':
    Application.main()
