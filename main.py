#Write Python code for both the Novel and Magazine classes modelled in the previous slide. Include a suitable constructor method which uses the Book constructor method. Instantiate 2 novels and 2 magazines and print their details.
#Create the Book class (plus methods and attributes)
#Create the Novel class that inherits from Book class.
#Create the Magazine class that inherits from Book class.
import random
import csv

class Book:
    def __init__(self, author, title, year, numPages):
        self.author = author
        self.title = title
        self.year = year
        self.numPages = numPages

    def method1(self):
        return "Parent method 1"

class Evolution(Book):
    def __init__(self, author, title, year, numPages):
        self.author = author
        self.title = title
        self.year = year
        self.numPages = numPages
        super().__init__(author, title, year, numPages)

    
    def Evolve(self):
        with open('BookEvolutions.csv', 'r') as file:
                reader = csv.reader(file)
                evolutions = [row[0] for row in reader]
                random_evolution = random.choice(evolutions)
                while random_evolution == 1:
                    random_evolution = random.choice(evolutions)
                print(f"Random evolution: {random_evolution}")
                name = random_evolution[1]; Type_1 = random_evolution[2]; Type_2 = random_evolution[3]; Hp = random_evolution[5]; Attack,Defense,Sp_Atk,Sp_Def,Speed,Generation,Legendary = random_evolution[7],random_evolution[8],random_evolution[9],random_evolution[10],random_evolution[11],random_evolution[12],random_evolution[13]

                print(f"Random evolution: {name}")
                self.name = f"{name}"
                print(f"New name: {self.name}")
                print(f"New Attack: {Attack}")
                print(f"New Defense: {Defense}")
                print(f"New Special Attack: {Sp_Atk}")
                print(f"New Special Defense: {Sp_Def}")
                print(f"New Speed: {Speed}")
                print(f"New Generation: {Generation}")
                print(f"New Legendary: {Legendary}")
                print(f"New Type_1: {Type_1}")
                print(f"New Type_2: {Type_2}")
                print(f"New Hp: {Hp}")

evo = Evolution('me', 'you', 'who', 'I')
evo.Evolve()