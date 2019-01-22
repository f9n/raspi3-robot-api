# raspi3-robot-api

## Streaming on Raspi3

### 1. raspivid

```bash
$ # On raspi3
$ raspivid -t 0 -l -o tcp://0.0.0.0:3333
$ # On client
$ vlc tcp/h264://192.168.1.101:3333
```

### 2. motion

```bash
$ apt install motion
$ # Activate the offical driver for camera.
$ sudo modprobe bcm2835-v4l2
$ # We also have to tell the Pi to active the driver after any reboot so our camera will always be available.
$ sudo vim /etc/modules
  # at the end of the file, add this line:
  bcm2835-v4l2
$ ###
$ systemctl enable motion
$ systemctl start motion
$ # cat /etc/motion/motion.conf
$ # Default streaming port: 8081
```

### 3. Vlc

```bash
$ # on Raspi
$ raspivid -o - -t 0 -hf -w 640 -h 360 -fps 25 -n | cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8080' :demux=h264
$ # on Client
$ vlc http://192.168.1.101:8080
```

### 4. v4l2rtspserver

https://github.com/mpromonet/v4l2rtspserver

```bash
$ 
```

### 5. UV4L

```bash
$ curl http://www.linux-projects.org/listing/uv4l_repo/lpkey.asc | sudo apt-key add -
$ # Add /etc/apt/sources.list
$ deb http://www.linux-projects.org/listing/uv4l_repo/raspbian/stretch stretch main
$ apt update
$ apt install uv4l uv4l-raspicam uv4l-raspicam-extras
$ sudo systemctl restart uv4l_raspicam
$ uv4l --driver raspicam --auto-video_nr --width 640 --height 480 --encoding jpeg
$ dd if=/dev/video0 of=snapshot.jpeg bs=11M count=1
$ apt install uv4l-server uv4l-uvc uv4l-xscreen uv4l-mjpegstream uv4l-dummy uv4l-raspidisp uv4l-webrtc uv4l-demos

```
