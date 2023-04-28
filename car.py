class Car:
    def __init__(self, model, color, speed, fuel_efficiency) -> None:
        self.model = model
        self.color = color
        self.speed = speed
        self.fuel_efficiency = fuel_efficiency
        self.fuel_consumption = 0
    
    def accelerate(self, speed):
        consumption = round(speed / self.fuel_efficiency, 2)
        self.fuel_consumption += consumption
        self.speed += speed
        return f"{self.model}이 가속해 {self.speed}km/h가 되었습니다. {consumption}L만큼 연료를 소비했습니다."
    
    def brake(self, speed):
        self.speed -= speed
        return f"{self.model}이 감속해 {self.speed}km/h가 되었습니다."
    
    def get_speed(self):
        return f"{self.model}의 현재 속도는 {self.speed}이며 현재까지 {self.fuel_consumption}L를 소비했습니다."
    

porche_911 = Car("포르쉐 911", "Yellow", 50, 5)
print(porche_911.accelerate(20))
print(porche_911.accelerate(26))
print(porche_911.brake(50))
print(porche_911.get_speed())