from flask import request, jsonify, Flask
from flask_cors import CORS
import os
import time
import predict
import common
from baidu_api import textGO
import shutil

app = Flask(__name__)
CORS(app, resources=r'/*')

@app.route("/", methods=["GET"])
def html():
    return app.send_static_file("index.html")

@app.route("/recognition", methods=["POST"])
def recognition():
    if request.form["original_img"]:
        t = time.time()
        path = "./temp/%d/"%int(round(t * 1000))
        os.mkdir(path)
        ori_img_path = path + "%d.jpg"%int(round(t * 1000))
        common.base64_to_image(request.form["original_img"], ori_img_path)
        pre_img_path, sub_imgs = predict.predict(east_detect, ori_img_path, pixel_threshold=0.9)
        pre_img = common.image_to_base64(pre_img_path)
        # print(pre_img)
        result_text = ""
        if sub_imgs != []:
            for sub_img in sub_imgs:
                if sub_img != "":
                    # print(sub_img)
                    args = textGO.get_args()
                    text_GO = textGO.TextGO(args.config)
                    words = text_GO.ocr(sub_img)
                    result_text += words
            # print(result_text)
        shutil.rmtree(path)
        return jsonify(img=pre_img, text=result_text)

if __name__ == "__main__":
    east_detect = predict.east_detect()
    app.run()