class Config:
    def __init__(self, size_x, size_y):
        self.scale = 1
        self.speed_time = 0
        self.size_x = size_x
        self.size_y = size_y
         
        self.camera_position_x = 0
        self.camera_position_y = 0

        self.speed_camera = 10
        self.scrolling_speed = 0.1

        self.max_radius_star = 10
        self.min_radius_star = 3