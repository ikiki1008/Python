class Car:
    name = ''
    speed = 0

    def upSpeed(self,value):
        self.speed += value

    def downSpeed(self,value):
        self.speed -= value


myCar1 = Car()
myCar1.name = 'myLittlePony'
myCar1.speed = 0

myCar2 = Car()
myCar2.name = 'Tesla'
myCar2.speed = 0

myCar3 = Car()
myCar3.name = '마티즈'
myCar3.speed = 0

myCar1.upSpeed(200)
print('the name of this car is %s, current speed is %d' % (myCar1.name, myCar1.speed))

myCar2.upSpeed(170)
print('the name of this car is %s, current speed is %d' % (myCar2.name, myCar2.speed))

myCar3.upSpeed(199)
print('the name of this car is %s, current speed is %d' % (myCar3.name, myCar3.speed))