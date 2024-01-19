import copy
class FuelStation:
    def __init__(self,diesel,petrol,electric):
        """
        Initializes the FuelStation object with initial fuel slots for each vehicle type.
        """
        self.initial_fuel_slots = {
            'diesel':diesel,
            'petrol':petrol,
            'electric':electric
        }
        self.available_fuel_slots = copy.deepcopy(self.initial_fuel_slots)
    
    def fuel_vheicle(self,vehicle):
        """
        Attempts to fuel a vehicle of the specified type if slots are available.
        """
        if vehicle not in self.available_fuel_slots or self.available_fuel_slots[vehicle] == 0:
            return False
        else:
            self.available_fuel_slots[vehicle] -= 1
            return True
    
    def open_fuel_slot(self,vehicle):
        """
        Opens a fuel slot for the specified vehicle type if occupied slots are available.
        """
        if vehicle not in self.available_fuel_slots or self.available_fuel_slots[vehicle] == self.initial_fuel_slots[vehicle]:
            return False
        else:
            self.available_fuel_slots[vehicle]+=1
            return True

