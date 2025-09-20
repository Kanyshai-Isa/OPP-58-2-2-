class Books:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def write_name(self):
        print(f'Наименование книги: "{self.name}"')

    def write_author(self):
        print(f'Автором книги является {self.author}')

first = Books("The Great Gatsby", "F. Scott Fitzgerald.", "1925")
second = Books("The Lord of the Rings", "J. R. R. Tolkien", "1954")

first.write_name()
second.write_author()

class Dictionary(Books):

    def __init__(self, name, author, year, colour):
       super().__init__(name, author, year)
       self.colour = colour

    def write_colour(self):
        print(f'Цвет словаря {self.colour}')

    def write_name(self):
        print(f'Теперь наименование книги: {(self.name)}')

thirst = Dictionary("Kyrgyz-Russian", "Yudakhin", "1944", 'red')
thirst.write_colour()

fourth = Dictionary('Диван лугат ат-турк', 'Махмуд аль Кашгари', '1101', 'blue')
fourth.write_name()