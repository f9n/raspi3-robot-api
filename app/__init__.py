from datetime import datetime

from flask import Flask, jsonify, render_template, Response, send_from_directory
import RPi.GPIO as GPIO
import picamera

from hardware import Camera, genFrame


def create_app(whells):
    app = Flask(__name__)

    ##### Video Stream

    @app.route("/v1")
    def index_v1():
        return render_template("index1.html")

    @app.route("/api/v1/video_feed")
    def video_feed():
        """Video streaming route. Put this in the src attribute of an img tag."""
        return Response(
            genFrame(Camera()), mimetype="multipart/x-mixed-replace; boundary=frame"
        )

    @app.route("/v2")
    def index_v2():
        return render_template("index2.html")

    @app.route("/api/v1/robot/stream/<cid>")
    def manuel_live_stream(cid):
        with picamera.PiCamera() as camera:
            camera.capture("app/static/image.jpg")
        return send_from_directory(directory="static", filename="image.jpg")

    #####  Hardware
    @app.route("/api/v2/robot/direction/<string:action>", methods=["POST"])
    def robot_direction_action(action):
        if not hasattr(whells, action):
            return (
                jsonify(
                    status="error", message="Robot api doesn't support this action"
                ),
                403,
            )

        action_method = getattr(whells, action)
        action_method()
        return (
            jsonify(status="success", message="Successfully completed the action."),
            200,
        )

    return app
