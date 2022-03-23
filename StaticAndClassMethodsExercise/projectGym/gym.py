class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if not customer in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if not trainer in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if not equipment in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if not plan in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if not subscription in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        message = ""
        for subscription in self.subscriptions:
            if subscription.id == subscription_id:
                message += f"{subscription}\n"
                customer_id = subscription.customer_id
                trainer_id = subscription.trainer_id
                exercise_id = subscription.exercise_id
                for customer in self.customers:
                    if customer.id == customer_id:
                        message += f"{customer}\n"
                for trainer in self.trainers:
                    if trainer.id == trainer_id:
                        message += f"{trainer}\n"
                for exercise in self.plans:
                    if exercise.id == exercise_id:
                        equipment_id = exercise.equipment_id
                        for equipment in self.equipment:
                            if equipment.id == equipment_id:
                                message += f"{equipment}\n"
                        message += f"{exercise}"
        return message