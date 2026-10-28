class Phone:

    def __init__(self, brand, model, price, color):
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color


    def show_info(self):
        print("men telefonman")


p01 = Phone('Samsung', 'S26 ultra', '2000', 'grey')
p02 = Phone('Iphone', '18 Pro', '2500', 'cherry')

p01.show_info()
p02.show_info()
