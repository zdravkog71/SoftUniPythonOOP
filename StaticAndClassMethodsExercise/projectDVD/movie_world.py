class MovieWorld:
    CAPACITY = 15
    CUSTOMER_CAPACITY = 10
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return MovieWorld.CAPACITY

    @staticmethod
    def customer_capacity():
        return MovieWorld.CUSTOMER_CAPACITY

    def add_customer(self, customer):
        if len(self.customers) < MovieWorld.CUSTOMER_CAPACITY:
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < MovieWorld.CAPACITY:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        for customer in self.customers:
            if customer.id == customer_id:
                customer_name = customer.name
                for dvd in customer.rented_dvds:
                    if dvd.id == dvd_id:
                        return f"{customer_name} has already rented {dvd.name}"
                for dvd in self.dvds:
                    if dvd.id == dvd_id:
                        if dvd.is_rented:
                            return f"DVD is already rented"
                for dvd in self.dvds:
                    if dvd.id == dvd_id:
                        if dvd.age_restriction > customer.age:
                            return f"{customer_name} should be at least {dvd.age_restriction} to rent this movie"
                customer.rented_dvds.append([dvd for dvd in self.dvds if dvd.id == dvd_id][0])
                for dvd in self.dvds:
                    if dvd.id == dvd_id:
                        dvd.is_rented = True
                return f"{customer_name} has successfully rented {[dvd.name for dvd in self.dvds if dvd.id == dvd_id][0]}"

    def return_dvd(self, customer_id, dvd_id):
        for customer in self.customers:
            if customer.id == customer_id:
                customer_name = customer.name
                for dvd in customer.rented_dvds:
                    if dvd.id == dvd_id:
                        dvd.is_rented = False
                        customer.rented_dvds.remove(dvd)
                        return f"{customer_name} has successfully returned {dvd.name}"
                return f"{customer_name} does not have that DVD"

    def __repr__(self):
        message = ""
        for customer in self.customers:
            message += f"{customer.__repr__()}\n"
        for dvd in self.dvds:
            message += f"{dvd.__repr__()}\n"

        return message