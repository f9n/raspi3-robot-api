import argparse

from app import create_app
from hardware import Whells

ROBOT_CONFIG = {
    "WHELLS": {
        "LEFT": {"FORWARD_PINNO": 11, "BACKWARD_PINNO": 13},
        "RIGHT": {"FORWARD_PINNO": 12, "BACKWARD_PINNO": 16},
    }
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Robotic - Raspberry Pi 3 - Flask Api")
    parser.add_argument("--host", help="Host of the application", default="0.0.0.0")
    parser.add_argument("--port", help="Port of the application", default="5000")
    args = parser.parse_args()

    try:
        whells = Whells.with_config(ROBOT_CONFIG["WHELLS"])
        app = create_app(whells)

        app.run(host=args.host, port=args.port)
    finally:
        print("Clean up")
