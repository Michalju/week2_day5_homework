class Room:
    def __init__(self, name):
        self.name = name
        self._guests = []

    def check_in(self, guest):
        self._guests.append(guest)