class Car(object):
    def __init__(self,model,color,company,speed_limit):
        self.color=color
        self.company=company
        self.model=model
        self.speed_limit=speed_limit

    def start(self):
        print('started')
    
    def stop(self):
        print('stop')

    def accelerate(self):
        print('accelareting')

    def changeGear(self):
        print('gearChange')

audi=Car("A6", "red", "audi", "80")
print(audi.color)
audi.stop()
