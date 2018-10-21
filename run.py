import argparse
from app import app

parser = argparse.ArgumentParser(description='Robotic - Raspberry Pi 3 - Flask Api')
parser.add_argument('--host', help='Host of the application', default='0.0.0.0')
parser.add_argument('--port', help='Port of the application', default='5000')
args = parser.parse_args()

app.run(host=args.host, port=args.port)
