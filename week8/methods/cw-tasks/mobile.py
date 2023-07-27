class Mobile:
    def __init__(self, imei, battery=100):
        self.__imei = imei
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        self.check_battery(0.5)
        self.__battery = value - 0.5

    def check_battery(self, limit=10.0):
        if self.battery <= limit:
            raise Exception('Battery low')

    def watch_video(self):
        self.check_battery()
        self.battery -= 7

    def listen_music(self):
        self.battery -= 5

    def charge(self, charge_amount):
        if charge_amount <= 0:
            raise Exception("Are you Kidding? Are you dump? How charging amount can be below zero? Are you want to suck out the whole soul of the battery?")
        if self.battery + charge_amount > 100:
            raise Exception(f"Yuuoooo! You are really kidding me. Battery can not hold percentage greater than 100. You really dump. Now battery percentage is {self.battery}")
        self.__battery = charge_amount


phone = Mobile(23130294, 100)
phone.charge(1)
print(phone.battery)

