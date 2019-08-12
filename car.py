class Car:
    Foo = "A"
    def __init__ (self, v=0, car_name = "Def_name"):
        self.name = car_name
        self.coordinate_x = 0
        self.coordinate_y = 0
        self.velocity = v
        self.direction = 0
    
    def move_forward(self, speed):
        self.velocity = speed

    def turn_right(self, angle):
        self.direction -= angle

    def turn_left(self, angle):
        self.direction += angle

    def stop(self):
        self.velocity = 0
    def __del__(self):
        print("Car", self.name, "moved out of frame.")
        self.coordinate_x = 0
        self.coordinate_y = 0
        self.velocity = 0
        self.direction = 0
        self.name = ""
        