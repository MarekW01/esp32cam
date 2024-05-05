from flask import Flask, Response, render_template
import cv2
import urllib.request
import numpy as np

app = Flask(__name__)

# Replace the URL with the IP camera's stream URL
url_high = 'http://192.168.1.52/cam-hi.jpg' #kamera + kvalita
url_mid = 'http://192.168.1.52/cam-mid.jpg' #kamera + kvalita
url_low = 'http://192.168.1.52/cam-lo.jpg'  #kamera + kvalita

def generate_frames_high():
    while True:
        img_resp = urllib.request.urlopen(url_high)
        imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
        im = cv2.imdecode(imgnp, -1)
        ret, buffer = cv2.imencode('.jpg', im)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def generate_frames_mid():
    while True:
        img_resp = urllib.request.urlopen(url_mid)
        imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
        im = cv2.imdecode(imgnp, -1)
        ret, buffer = cv2.imencode('.jpg', im)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def generate_frames_low():
    while True:
        img_resp = urllib.request.urlopen(url_low)
        imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
        im = cv2.imdecode(imgnp, -1)
        ret, buffer = cv2.imencode('.jpg', im)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed_high')
def video_feed_high():
    return Response(generate_frames_high(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed_mid')
def video_feed_mid():
    return Response(generate_frames_mid(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed_low')
def video_feed_low():
    return Response(generate_frames_low(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
