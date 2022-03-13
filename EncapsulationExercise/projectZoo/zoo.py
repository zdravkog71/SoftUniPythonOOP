class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):

        if len(self.animals) < self.__animal_capacity:
            if self.__budget - price >= 0:
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {type(animal).__name__} added to the zoo"
            else:
                return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        return f"Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        workers_salary = sum([worker.salary for worker in self.workers])
        if workers_salary <= self.__budget:
            self.__budget -= workers_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        animal_tend_amount = sum([animal.money_for_care for animal in self.animals])
        if animal_tend_amount <= self.__budget:
            self.__budget -= animal_tend_amount
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        message = f"You have {len(self.animals)} animals\n"
        lions_statuses = [repr(animal) for animal in self.animals if type(animal).__name__ == "Lion"]
        tigers_statuses = [repr(animal) for animal in self.animals if type(animal).__name__ == "Tiger"]
        cheetahs_statuses = [repr(animal) for animal in self.animals if type(animal).__name__ == "Cheetah"]

        #Lions
        message += f"----- {len(lions_statuses)} Lions:\n"
        message += "\n".join(lions_statuses)
        message += "\n"

        #Tigers
        message += f"----- {len(tigers_statuses)} Tigers:\n"
        message += "\n".join(tigers_statuses)
        message += "\n"

        #Cheetah
        message += f"----- {len(cheetahs_statuses)} Cheetahs:\n"
        message += "\n".join(cheetahs_statuses)

        return message

    def workers_status(self):
        message = f"You have {len(self.workers)} workers\n"
        keepers_statuses = [repr(worker) for worker in self.workers if type(worker).__name__ == "Keeper"]
        caretakers_statuses = [repr(worker) for worker in self.workers if type(worker).__name__ == "Caretaker"]
        vets_statuses = [repr(worker) for worker in self.workers if type(worker).__name__ == "Vet"]

        #Keepers
        message += f"----- {len(keepers_statuses)} Keepers:\n"
        message += "\n".join(keepers_statuses)
        message += "\n"

        #Caretakers
        message += f"----- {len(caretakers_statuses)} Caretakers:\n"
        message += "\n".join(caretakers_statuses)
        message += "\n"

        #Vets
        message += f"----- {len(vets_statuses)} Vets:\n"
        message += "\n".join(vets_statuses)

        return message



