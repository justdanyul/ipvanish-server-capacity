class Server:
    name = None
    capacity = None
    country = None
    city = None

    def __init__(self, name: str, capacity: int, country: str, city: str) -> None:
        self.name = name
        self.capacity = capacity
        self.country = country
        self.city = city

    def __str__(self):
        return 'Server {0} in {2},{3} is at {1}%'\
            .format(self.name, self.capacity, self.city, self.country)

    def __eq__(self, other):
        return self.name == other.name and self.capacity == other.capacity \
               and self.country == other.country and self.city == other.city
