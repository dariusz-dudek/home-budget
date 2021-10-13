from abc import ABC, abstractmethod


class AbstractView(ABC):
    def __init__(self):
        self.repositories = {}

    @abstractmethod
    def draw(self):
        pass

    def set_repository(self, name, repository):
        self.repositories[name] = repository


class AddCost(AbstractView):
    SHORTCUT = 'dk'
    LABEL = 'Dodaj koszt'

    def draw(self):
        print(AddCost.LABEL)
        title = input('Tytuł: ')
        category_name = input('Kategoria: ')
        amount = float(input('Wartość: '))

        category = self.repositories['category'].get_by_name(category_name)
        self.repositories['entry'].save(title, category, amount)


class ListCost(AbstractView):
    SHORTCUT = 'wk'
    LABEL = 'Wyświetl koszty'

    def draw(self):
        print(ListCost.LABEL)


class AddIncome(AbstractView):
    SHORTCUT = 'dp'
    LABEL = 'Dodaj przychód'

    def draw(self):
        print(AddIncome.LABEL)


class ListIncomes(AbstractView):
    SHORTCUT = 'wp'
    LABEL = 'Wyświetl przychody'

    def draw(self):
        print(ListIncomes.LABEL)


class MainMenu(AbstractView):
    OPTIONS = {
        AddCost.SHORTCUT: AddCost(),
        ListCost.SHORTCUT: ListCost(),
        AddIncome.SHORTCUT: AddIncome(),
        ListIncomes.SHORTCUT: ListIncomes()
    }

    def get_screen(self):
        option = None
        while option not in MainMenu.OPTIONS:
            option = input('Wybierz opcję: ')

        return MainMenu.OPTIONS[option]

    def draw(self):
        print('Powiedz co chcesz zrobić: ')
        for shortcut, screen in MainMenu.OPTIONS.items():
            print(f'[{shortcut}] - {screen.LABEL}')
