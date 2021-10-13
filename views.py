class AddCost:
    SHORTCUT = 'dk'
    LABEL = 'Dodaj koszt'


class ListCost:
    SHORTCUT = 'wk'
    LABEL = 'Wyświetl koszty'


class AddIncomes:
    SHORTCUT = 'dp'
    LABEL = 'Dodaj przychód'


class ListIncomes:
    SHORTCUT = 'wp'
    LABEL = 'Wyświetl przychody'


class MainMenu:
    OPTIONS = {
        AddCost.SHORTCUT: AddCost(),
        ListCost.SHORTCUT: ListCost(),
        AddIncomes.SHORTCUT: AddIncomes(),
        ListIncomes.SHORTCUT: ListIncomes()
    }

    def draw(self):
        print('Powiedz co chcesz zrobić: ')
        for shortcut, screen in MainMenu.OPTIONS.items():
            print(f'[{shortcut}] - {screen.LABEL}')

        option = None

        while option not in MainMenu.OPTIONS:
            option = input('Wybierz opcję: ')

        print(MainMenu.OPTIONS[option])
