import os
import sys
from signLanguage.logger import logging
from signLanguage.exception import SignException
from signLanguage.pipeline.training_pipeline import TrainPipeline
from signLanguage.utils.main_utils import encodeImageIntoBase64,decodeImage
from flask import Flask, render_template, request, jsonify, Response
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"


@app.route("/train")
def trainRoute():
    obj = TrainPipeline()
    obj.run_pipeline()
    return "Training Successful"

@app.route("/predict",methods=["POST","GET"])
def predictRoute():
    try:
        image = request.json["image"]
        decodeImage(image, clApp.filename)

        os.system("cd yolov5/ && python detect.py --weights my_model.pt --img 416 --conf 0.5 --source ../data/imputImage.jpg")

        opencodedbase64 = encodeImageIntoBase64("yolov5/runs/detect/exp/inputImage.jpg")
        result = {"Image": opencodedbase64.decode('utf-8')}
        os.system("rm -rf yolov5/runs")
    
    except Exception as val:
        print(val)
        return Response("Value not found inside json data")
    except KeyError:
        return Response("Key Value Error incorrect key passed")
    except Exception as e:
        print(e)
        raise "Invalid Input"
    
    return jsonify(result)

@app.route("/live",methods=["POST","GET"])
@cross_origin()
def liveRoute():
    try:
        os.system("cd yolov5/ && python detect.py --weights my_model.pt --img 416 --conf 0.5 --source 0")
        os.system("rm -rf yolov5/runs")
        return "Camera Starting!"
    
    except ValueError as val:
        print(val)
        return Response("Value not found inside json data")
    

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

if __name__ == "__main__" :
    clApp = ClientApp()
    app.run(host="0.0.0.0",port=8080)

