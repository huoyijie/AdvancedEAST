import os

from tqdm import tqdm
from network import East
from predict import predict_txt
import cfg


if __name__ == '__main__':
    east = East()
    east_detect = east.east_network()
    east_detect.load_weights(cfg.saved_model_weights_file_path)

    image_test_dir = os.path.join(cfg.data_dir, 'icpr_mtwi_task3/image_test/')
    txt_test_dir = os.path.join(cfg.data_dir, 'icpr_mtwi_task3/txt_test/')
    test_imgname_list = os.listdir(image_test_dir)
    print('found %d test images.' % len(test_imgname_list))
    for test_img_name, _ in zip(test_imgname_list,
                                tqdm(range(len(test_imgname_list)))):
        img_path = os.path.join(image_test_dir, test_img_name)
        txt_path = os.path.join(txt_test_dir, test_img_name[:-4] + '.txt')
        predict_txt(east_detect, img_path, txt_path, cfg.pixel_threshold, True)
