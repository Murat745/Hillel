"""
Lesson 15, homework 12, task 1 solution.
Vehicle classes inheritance.
"""


class Vehicle:
    def __init__(self, transport_mode, estimated_range, fuel_type, speed):
        self.transport_mode = transport_mode
        self.estimated_range = estimated_range
        self.fuel_type = fuel_type
        self.speed = speed

    def description(self):
        print("Transport mode according to UN Trade Facilitation Implementation Guide: ", self.transport_mode)
        print('Estimated range on a single refueling/charge: ', self.estimated_range)
        print('Fuel type: ', self.fuel_type)


class Train(Vehicle):
    def __init__(self, transport_mode, estimated_range, fuel_type, speed, departure_station, arrival_station):
        super().__init__(transport_mode, estimated_range, fuel_type, speed)
        self.departure_station = departure_station
        self.arrival_station = arrival_station

    def info(self):
        print(f'Train: {self.departure_station}-{self.arrival_station}')


class Aircraft(Vehicle):
    def __init__(self, transport_mode, estimated_range, model, make):
        super().__init__(transport_mode, estimated_range, fuel_type='kerosene', speed=800)
        self.model = model
        self.make = make

    def flying(self, destination):
        print(f'We are going to {destination}')


oberig = Train('rail(UIC)', 700, 'electric', 100, 'Kharkiv', 'Kyiv')
intercity = Train('rail(UIC)', 1000, 'electric', 180, 'Kharkiv', 'Lviv')
cessna = Aircraft('air', 500, 'Cessna 172', 'Cessna Aircraft Company')
boeing = Aircraft('air', 12000, 'Boeing 777', 'Boeing Corp')
oberig.info()
intercity.description()
cessna.description()
cessna.flying('Truskavets')
