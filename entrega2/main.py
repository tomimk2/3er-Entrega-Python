class Client:

    def __init__ (self, name, lastName, email, phone, purchase):
        self.name = name 
        self.lastname = lastName
        self.email = email
        self.phopne = phone
        self.purchase = purchase
        self.purchases = []

    def add_purchase(self, purchase):

        self.purchases.append(purchase)
        
    def total_items_purchase (self):
        
        return sum([purchase ['amount'] for purchase in self.purchases])

    def __str__ (self):
        return f"el cliente {self.name} ha comprado con exito!"