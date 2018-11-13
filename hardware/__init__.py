# from .whells import Whells
from .camera import Camera, genFrame

class Whells:
    def __init__(
        self,
        left_whell_forward_pinno=11,
        left_whell_backward_pinno=13,
        right_whell_forward_pinno=12,
        right_whell_backward_pinno=16,
    ):
        print("Whells initializing...")

    @staticmethod
    def with_config(config):
        return Whells()

    def forward(self):
        print("Forwarding....")

    def backward(self):
        print("Backwarding....")

    def turn_left(self):
        print("Turning Left....")

    def turn_right(self):
        print("Turning Right...")

    def stop(self):
        print("Stopping...")
