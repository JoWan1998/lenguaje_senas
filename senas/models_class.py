class movement:
    def __init__(self):
        self.hand_posX = 0
        self.hand_posy = 0
        self.noise_pos = 0
        self.eye_left  = 0
        self.eye_rigth = 0
        self.dimension = 0

class move_id:
    def __init__(self,movement):
        self.weigth     = 0
        self.move_stats = movement