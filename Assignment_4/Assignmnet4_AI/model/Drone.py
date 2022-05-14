class DroneClass:

    def __init__(self):
        self.position = (16, 17)
        self.energy = 50
        self.photo = "drona.png"

    def set_position(self, new_position):
        self.position = (new_position[1], new_position[0])

    def get_position(self):
        return self.position

    def set_energy(self, new_energy):
        self.energy = new_energy

    def get_energy(self):
        return self.energy

    def get_photo(self):
        return self.photo