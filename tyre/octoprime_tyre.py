from tyre.tyre import Tyre


class OctoprimeTyre(Tyre):
    def __init__(self, front_left_tyre_wear, front_right_tyre_wear, back_left_tyre_wear, back_right_tyre_wear):
        self.front_left_tyre_wear = front_left_tyre_wear
        self.front_right_tyre_wear = front_right_tyre_wear
        self.back_left_tyre_wear = back_left_tyre_wear
        self.back_right_tyre_wear = back_right_tyre_wear

    def needs_service(self):
        if self.front_left_tyre_wear + self.front_right_tyre_wear + self.back_left_tyre_wear + self.back_right_tyre_wear >= 3:



