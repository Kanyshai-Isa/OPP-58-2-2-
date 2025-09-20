class animals:

    def __init__(self,name, colour, eat):
        self.name = name
        self.colour = colour
        self.eat = eat

    def show_what_animal_eat(self):
        print(f' {self.name} eats {self.eat}')

lion = animals('lion', 'yellow', 'meat')
lion.show_what_animal_eat()

zebra = animals('zebra','w/b', 'grass')
zebra.show_what_animal_eat()