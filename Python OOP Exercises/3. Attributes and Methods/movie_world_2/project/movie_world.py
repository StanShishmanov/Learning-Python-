# from project.customer import Customer
# from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def find_dvd_by_id(self, dvd_id):
        for dvd in self.dvds:
            if dvd.id == dvd_id:
                return dvd

    def find_customer_by_id(self, customer_id):
        for customer in self.customers:
            if customer.id == customer_id:
                return customer

    def add_customer(self, customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        # is_dvd_rented = False
        # is_same_renter_customer = False
        # age_restricted = False
        dvd = self.find_dvd_by_id(dvd_id)
        customer = self.find_customer_by_id(customer_id)

        if dvd.is_rented:
            # is_dvd_rented = True
            # TODO
            return "DVD is already rented"

        if dvd.name in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
            # TODO

        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = self.find_customer_by_id(customer_id)
        dvd = self.find_dvd_by_id(dvd_id)
        for d in customer.rented_dvds:
            if d.id == dvd_id:
                d.is_rented = False
                customer.rented_dvds.remove(d)
                return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        nl = '\n'
        repr_customers = []
        with_cust_nl = []
        repr_dvds = []
        with_dvd_nl = []
        for c in self.customers:
            repr_customers.append(c.__repr__())
        for c in repr_customers:
            if c != repr_customers[-1]:
                with_cust_nl.append(c + nl)
            else:
                with_cust_nl.append(c)

        for d in self.dvds:
            repr_dvds.append(d.__repr__())
        for d in repr_dvds:
            if d != repr_dvds[-1]:
                with_dvd_nl.append(d + nl)
            else:
                with_dvd_nl.append(d)

        return f"{''.join(r for r in with_cust_nl)}\n{''.join(re for re in with_dvd_nl)}"

#
# from project.customer import Customer
# from project.dvd import DVD
# from project.movie_world import MovieWorld

#
# c1 = Customer("John", 16, 1)
# c2 = Customer("Anna", 55, 2)
#
# d1 = DVD("Black Widow", 1, 2020, "April", 18)
# d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)
#
# movie_world = MovieWorld("The Best Movie Shop")
#
# movie_world.add_customer(c1)
# movie_world.add_customer(c2)
#
# movie_world.add_dvd(d1)
# movie_world.add_dvd(d2)
#
# print(movie_world.rent_dvd(1, 1))
# print(movie_world.rent_dvd(2, 1))
# print(movie_world.rent_dvd(1, 2))
#
# print(movie_world)
