class Car(object):
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def run(self):
        print('i can run')


class GasolineCar(Car):
    def __init__(self, brand, model, color):
        super().__init__(brand, model, color)

    def run(self):
        print('i can run with gasoline')


class ElectricCar(Car):
    def __init__(self, brand, model, color):
        super().__init__(brand, model, color)
        # 电池属性
        self.battery = 70

    def run(self):
        print(f'i can run with electric，remain:{self.battery}')


bwm = GasolineCar('宝马', 'X5', '白色')
bwm.run()

tesla = ElectricCar('特斯拉', 'Model S', '红色')
tesla.run()