class Room:
    def __init__(self, name):
        self.name = name
        self._guests = []

    # This method return guest by name 
    def find_guest_by_name(self,name):
        for guest in self._guests:
            if guest.name==name:
                return guest


    # This method checks in a guest to the room
    def check_in(self, guest):
        self._guests.append(guest)

    # This method checks out from the room either:
    # a single named person
    # or
    # all guests if name is ""
    
    def check_out(self, name):
        if not name:
            self._guests.clear()
        else:
            self._guests.remove(self.find_guest_by_name(name))