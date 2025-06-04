
from flask import Flask,request,render_template,jsonify
import os
from flask_cors import CORS,cross_origin
from src.cnnClassifier.utils.common import encodeimage,decodeimage
from src.cnnClassifier.pipeline.predict_pipeline import PredictionPipeline


app=Flask(__name__)
CORS(app)

os.putenv('LANG','en_US.UTF-8')
os.putenv('LC_ALL','en_US.UTF-8')

class ClientApp:

    def __init__(self):
        self.filename="inputimage.jpg"
        self.classifier=PredictionPipeline(self.filename)

@app.route('/',methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route('/train',methods=['GET','POST'])
@cross_origin()

def train_route():
    os.system("python main.py")
    return "Training done successfully"

@app.route('/result',methods=['POST'])
@cross_origin

def predictRoute():
    image=request.json['image']
    decodeimage(image,clApp.filename)
    result=clApp.classifier.predict()
    return jsonify(result)


if __name__=="__main__":
    clApp=ClientApp()
    app.run(host='0.0.0.0',port=5000,debug=True)