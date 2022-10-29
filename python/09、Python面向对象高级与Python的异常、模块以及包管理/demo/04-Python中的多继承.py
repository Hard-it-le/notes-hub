class GasolineCar(object):
    def run_with_gasoline(self):
        print('i can run with gasoline')


class EletricCar(object):
    def run_with_eletric(self):
        print('i can run with eletric')


class HybridCar(GasolineCar, EletricCar):
    pass


tesla = HybridCar()
tesla.run_with_gasoline()
tesla.run_with_eletric()