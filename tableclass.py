class PoolTable:
    def __init__(self, number, start_time = 0, end_time = 0, total_time = 0, occupied = False, total_cost = 0):
        self.number = number
        self.start_time = start_time
        self.end_time = end_time
        self.total_time = total_time
        self.occupied = occupied
        self.total_cost = total_cost
    
    @staticmethod
    def from_dictionary(dict):
        return PoolTable(dict["number"], dict["start_time"], dict["end_time"], dict["total_time"], dict["occupied"]), dict["total_cost"]