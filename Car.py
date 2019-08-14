#creating a class
class Car:
    # can pass values from user into class if you want to pass user information through the class
    def __init__(self, speed=60):
        #defining the attributes of the class
        self.speed = speed #speed of 60 kph
        self.odometer = 30 #number of km travelled
        self.time = 2 #took

    def say_slate(self):
        print("I'm going {} kph".format(self.speed))

    def accelerate(self):
        self.speed += 5
        print("I am now moving at {} kph!".format(self.speed))
    def brake(self):
        if self.speed < 5:
            self.speed = 0
            print("I am now stopped.")
        else:
            self.speed -= 5
            print("I am now moving at {} kph!".format(self.speed))
    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        if self.time != 0:
            return self.odometer / self.time
        else:
            pass

if __name__ == '__main__':

        my_car = Car()
        print("I'm a car!")
        my_car.say_slate()
        while True:
            action = input("what should I do? [A]ccelerate, [B]rake, "
                           "show [O]dometer, or show average [S]peed?").upper()
            if action not in "ABOS" or len(action) != 1:
                # this if statement is saying, if the action input types is not in the string
                # ABOS or the length of
                # the input action is greater than 1 character then it cannot do that action
                print("I don't know how to do that")
                continue
            if action == 'A':
                my_car.accelerate()
            elif action == 'B':
                my_car.brake()
            elif action == 'O':
                print("this car has driven {} kilometers".format(my_car.odometer))
            elif action == "S":
                print("The car's average speed was {} kph".format(my_car.average_speed()))
            my_car.step()
            pass
