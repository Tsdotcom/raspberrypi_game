
class User:
    def __init__(self):
        self.live = 3
        self.user_point = 0

    def get_score(self):
        return self.user_point
    def set_score(self,point):
        self.user_point = point
    def get_name(self):
        return self.user_name
    