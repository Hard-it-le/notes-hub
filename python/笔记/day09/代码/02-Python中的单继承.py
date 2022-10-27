# 1、定义一个共性类（车类）
class Car(object):
    def run(self):
        print('i can run')
# 2、定义汽油车
class GasolineCar(Car):
    pass
# 3、定义电动车
class EletricCar(Car):
    pass

bwm = GasolineCar()
bwm.run()