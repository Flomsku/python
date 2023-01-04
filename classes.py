#properties/attr of a bike: make, model, wheel count, speed, direction, location etc.
#methods of a bike: ignition on/off, turn, lean, lights on/off etc.
#class = abstract representation of an object type
#a motorcycle is a class
#instance = an actual object
#my/your motorcycle is an instance

#it is good practise to have classes in different while, sometimes even in their own files: each class gets its own file
class vehicle:
    is_engine_on = False #properties / attributes
    is_headlight_on = False
    make = None
    model = None
    is_driving = False

    def __init__(self, make, model) -> None: #magic method
        self.make = make
        self.model = model
    
    def __repr__(self) -> str: # repr is used to print out the object in string format
        return (f'{self.make} {self.model} with engine ' # f' turns the following into format strings, no need to string concatenate
                f'{"on" if self.is_engine_on else "off"} and headlight '
                f'{"on" if self.is_headlight_on else "off"}') 
                
    def turn_engine_on(self):   #method = calling a function that is on a class instance. Self refers to the instance of the class as itself. So you can use the method on all of the differnet instances and refer to them as themselves
        print('Turning enging on')
        self.is_engine_on = True

    def turn_engine_off(self): #Method to turn engine off 
        print('Turning enging off')
        if self.is_driving:
            print('You tried to turn the engine off while driving, '
                 'and crashed')
            return
        self.is_engine_on = False

    def turn_headlight_on(self): #Method to turn headlights on 
        print('Turning headlights on')
        self.is_headlight_on = True

    def turn_headlight_off(self): #Method to turn headlights off 
        print('Turning headlights off')
        self.is_headlight_on = False

    def start_driving(self):    #Method to start driving
        if self.is_engine_on: #check is engine is on before driving
            print('Starting to drive')
            self.is_driving = True
        else:
            print("You can't drive without turning the engine on!")
            return

    def stop_driving(self): #Method to stop driving
        print('Stopping')
        self.is_driving = False

class Motorcycle(vehicle):
    is_engine_on = False #properties / attributes
    is_headlight_on = False
    make = None
    model = None
    is_driving = False



    def lean(self, direction): #Method to lean in motorcycle
        if self.is_driving: 
            print(f'Leaning {direction}')
        else:
            print('You leaned while not driving and crashed!')
            return
            

    def turn_handlebars(self, direction): #turning handlebar for turning
        print(f'Turning the handlebars {direction}')

    def turn(self, direction): #turning with the bike
        if direction == 'left': #turning left
            self.turn_handlebars('right')   #to turn left with a bike you turn handlebar to right and lean left
            self.lean('left')
        elif direction == 'right': #same logic to turning right
            self.turn_handlebars('left')
            self.lean('right')
        else:
            print("Sry didn't understood that direction")

class Car(vehicle): #copy of the class Motorcycle to test if its work -> inheriting the motorcycle class properties for car
    def turn_wheel(self, direction): #turning steering wheel of the car
        print(f'Turning the wheel {direction}')

    def turn(self, direction): #testing different way to send direction to turn_wheel method
        if direction in ['left','right']: #checking if the direction is in the list and check sending it
            self.turn_wheel(direction)
        else:
            print("Sry didn't understood that direction")

# ctrl + k + c = comment out block in VScode and Ctrl + k + u to uncomment
# moto = Motorcycle('Triumph', 'Thruxton')
# MyCar = Car('Toyota','Corolla')

# for vehicles in [moto, MyCar]: #testing if the methods work as intended
#     print(vehicles)
#     vehicles.turn_engine_on()
#     vehicles.turn_headlight_on()
#     vehicles.start_driving()
#     vehicles.turn('left')
#     vehicles.turn('right')
#     vehicles.stop_driving()
#     vehicles.turn_engine_off()
#     vehicles.turn_headlight_off()
#     print(vehicles)
#     print(type(vehicles))
#     print()
    



