class Car():
    def __init__(self, company, color, model, speed):
        self.company=company
        self.color=color
        self.model=model
        self.speed=speed
    def start(self):
        print("Car has started")
    def acclerate(self, newspeed):
        print(self.speed+newspeed)

car1=Car("ferrari", "black", "la", 458)
print(car1.speed)
car1.start()
car1.acclerate(300)