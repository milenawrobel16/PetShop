class Pet:

    def __init__(self, name, species, price):
        self.name = name
        self.species = species
        self.price = price


class Customer:

    def __init__(self, name):
        self.name = name
        self.pets = []

    def buy_pet(self, pet):
        self.pets.append(pet)

    def count_pets(self):
        return len(self.pets)

    def display_pets(self):
        for pet in self.pets:
            print(f"{pet.name} - {pet.species}")


class PetShop:

    def __init__(self):
        self.pets_for_sale = []

    def add_pet(self, pet):
        self.pets_for_sale.append(pet)

    def display_pets(self):
        for pet in self.pets_for_sale:
            print(f"{pet.name} - {pet.species}")

    def find_pet(self, name):
        for pet in self.pets_for_sale:
            if pet.name == name:
                return pet
        return None

    def sell_pet(self, pet, customer):
        pet_for_sale = self.find_pet(pet.name)
        if pet_for_sale is not None:
            customer.buy_pet(pet_for_sale)
            self.pets_for_sale.remove(pet_for_sale)
            return True
        return False


pet1 = Pet("Burek", "dog", 500)
pet2 = Pet("Mruczek", "cat", 300)

shop = PetShop()
shop.add_pet(pet1)
shop.add_pet(pet2)

anna = Customer("Anna")

print(anna.count_pets())
shop.display_pets()
shop.sell_pet(pet1, anna)


