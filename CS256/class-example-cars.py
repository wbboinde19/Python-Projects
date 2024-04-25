class Car:
    """
    blueprint for car
    """
    def __init__(self, model, color, company, speed_limit):
      self.color = color
      self.company = company
      self.speed_limit = speed_limit
      self.model = model

      #define getters and setters
    def get_color(self):
        return self.color
    def set_color(self,new_color):
        self.color = new_color

    def get_company(self):
        return self.get_company
    def set_company(self,new_company):
        self.company = new_company

    def get_speed_limit(self):
        return self.speed_limit
    def set_speed_limit(self,new_speed_limit):
        self.speed_limit = new_speed_limit

    def get_model(self):
        return self.model
    def set_model(self,new_model):
        self.model = new_model

    #define other methods
    def start(self):
        print("started")
        "starting functionality here"

    def stop(self):
        print("stopped")
        "stopping functionality here"

    def accelarate(self):
        print("accelarating...")
        "accelarator functionality here"

    def change_gear(self, gear_type):
        print("gear changed to", gear_type)
        " gear related functionality here"

#define module tester
if __name__ == "__main__":
    firstCar = Car("CR-V", "Blue", "Honda", 100)

    firstCar.change_gear("first")
