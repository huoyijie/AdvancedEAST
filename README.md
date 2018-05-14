# AdvancedEAST
AdvancedEAST is an algorithm used for Scene image text detect, which is primarily based on [EAST:An Efficient and Accurate Scene Text Detector](https://arxiv.org/abs/1704.03155v2), and the significant improvement was also made, which make long text predictions more accurate.

# setup
* python 3.6.3+
* tensorflow-gpu 1.5.0+(or tensorflow 1.5.0+)
* keras 2.1.4+
* numpy 1.14.1+
* tqdm 4.19.7+

# train
* pre-process data:
    preprocess.py,resize image
* label data:
    label.py,produce label info
* define network
    network.py
* define loss function
    losses.py
* execute training
    advanced_east.py and data_generator.py
* predict
    predict.py and nms.py

# demo results
![001原图](demo/001.png)
![001激活图](demo/001.png_act.jpg)
![001预测图](demo/001.png_predict.jpg)

![004原图](demo/004.jpg)
![004激活图](demo/004.jpg_act.jpg)
![004预测图](demo/004.jpg_predict.jpg)

![005原图](demo/005.png)
![005激活图](demo/005.png_act.jpg)
![005预测图](demo/005.png_predict.jpg)

![007原图](demo/007.png)
![007激活图](demo/007.png_act.jpg)
![007预测图](demo/007.png_predict.jpg)

# references
* [EAST:An Efficient and Accurate Scene Text Detector](https://arxiv.org/abs/1704.03155v2)

* [CTPN:Detecting Text in Natural Image with Connectionist Text Proposal Network](https://arxiv.org/abs/1609.03605)
