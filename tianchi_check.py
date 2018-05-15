import numpy as np
from PIL import Image, ImageDraw


def test():
    with Image.open('demo/LB1xbbUGVXXXXaIXFXXXXXXXXXX.jpg') as im:
        # draw on the origin img
        draw = ImageDraw.Draw(im)
        with open('demo/LB1xbbUGVXXXXaIXFXXXXXXXXXX.txt', 'r') as f:
            anno_list = f.readlines()
        for anno in anno_list:
            anno_colums = anno.strip().split(',')
            anno_array = np.array(anno_colums)
            xy_list = np.reshape(anno_array.astype(float), (4, 2))
            draw.line([tuple(xy_list[0]), tuple(xy_list[1]), tuple(xy_list[2]),
                       tuple(xy_list[3]), tuple(xy_list[0])],
                      width=1,
                      fill='red')
        im.save('demo/LB1xbbUGVXXXXaIXFXXXXXXXXXX_anno.jpg')


test()
