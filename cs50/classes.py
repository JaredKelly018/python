class Point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2
    
p = Point(2,8)
#go into the point and access the data this is dot notion
print(p.x)
print(p.y)

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    def add_passenger(self, name):
        #same as if self.open_seats() == 0:
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ['rin', 'Estrea', 'Jared', 'Fish']
for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No seats advallible for {person}")