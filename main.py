from views import MainMenu

class Application:
    @staticmethod
    def main():
        menu = MainMenu()
        menu.draw()


if __name__ == '__main__':
    Application.main()
