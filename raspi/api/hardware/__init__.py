from .whells import Whells
from gpiozero import _Robot


class Robot(object):
    @staticmethod
    def with_config(config, mode=""):
        if mode == "gpiozero":
            whells = {
                whell_name: tuple(whell.values())
                for whell_name, whell in config["WHELLS"].items()
            }
            robot = _Robot(left=whells["LEFT"], right=whells["RIGHT"])
            return robot
        else:
            robot = Whells.with_config(config["WHELLS"])
            return robot
