class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def get_sub_by_id(self, subscription_id):
        for sub in self.subscriptions:
            if sub.id == subscription_id:
                return sub

    def get_cust_by_id(self, cust_id):
        for cust in self.customers:
            if cust.id == cust_id:
                return cust

    def get_trainer_by_id(self, trainer_id):
        for tr in self.trainers:
            if tr.id == trainer_id:
                return tr

    def get_exercise_by_id(self, plan_id):
        for pl in self.plans:
            if pl.id == plan_id:
                return pl

    def get_equipment_by_id(self, eq_id):
        for eq in self.equipment:
            if eq.id == eq_id:
                return eq

    def subscription_info(self, subscription_id):
        sub = self.get_sub_by_id(subscription_id)
        customer = self.get_cust_by_id(sub.customer_id)
        trainer = self.get_trainer_by_id(sub.trainer_id)
        exercise = self.get_exercise_by_id(sub.exercise_id)
        # equipment = self.get_equipment_by_id(sub.eq)
        return sub.__repr__() + '\n' + customer.__repr__() + '\n' + trainer.__repr__() + \
               '\n' + self.equipment[0].__repr__() + '\n' + exercise.__repr__()

#cc