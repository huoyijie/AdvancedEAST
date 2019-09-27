""" textGO img2text tool"""
import os
import json
import argparse
from base64 import b64encode

import requests


def get_args() -> argparse.Namespace:
    """ 获取命令参数 """
    parser = argparse.ArgumentParser(description="OCR 识别图片中的文字")
    # parser.add_argument("img", help="指定要识别的图片")
    parser.add_argument(
        "-c", "--config", default="/home/develkone/Code/python/AdvancedEAST/baidu_api/config.json", help="指定配置文件")
    return parser.parse_args()


class TextGO:
    """ 定义 ocr 类 """

    def __init__(self, config_file):
        config = self.read_config(config_file)
        if not (config.get("api_key") and config.get("secret_key")):
            print("请指定一个合理的配置文件，配置文件中要包含 api_key 和 secret_key!")
            self.access_token = ""
            return
        access_token = config.get("access_token")
        if access_token is None or access_token == "":
            access_token = self.get_access_token(
                config.get("api_key"), config.get("secret_key"))
            config["access_token"] = access_token
            self.write_config(config_file, config)
        self.access_token = config.get("access_token")

    @staticmethod
    def read_config(config_file) -> dict:
        """ 从 json 文件中读取配置 """
        if not os.path.exists(config_file):
            print(f"指定的配置文件 {config_file} 不存在!")
            return {}
        with open(config_file, "r") as load_file:
            return json.load(load_file)
        return {}

    @staticmethod
    def write_config(config_file, config):
        """ 将配置写入文件 """
        with open(config_file, "w") as f_obj:
            json.dump(config, f_obj)

    @staticmethod
    def img_to_base64(img):
        """ convert img to base64 data """
        with open(img, "rb") as img_f:
            file_data = img_f.read()
            b64_data = b64encode(file_data)
            b64_str = str(b64_data, "utf-8")
        return b64_str

    @staticmethod
    def get_access_token(api_key, secret_key):
        """ 获取百度 AI 的文字识别 access_token """
        print("获取百度 AI 文字识别的 Access Token ...")
        url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s"
        response: requests.models.Response = requests.get(
            url % (api_key, secret_key))
        body_str = str(response.content, "utf-8")
        body_dict = json.loads(body_str)
        return body_dict.get("access_token")

    def ocr(self, img):
        """ 利用百度 AI 识别文字 """
        if self.access_token == "":
            print("没有 access_token")
            return ""
        url = f"https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic?access_token={self.access_token}"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {
            "image_type": "BASE64",
            "image": self.img_to_base64(img),
            "group_id": "textGO_test",
            "user_id": "5km"
        }
        response = requests.post(url=url, data=data, headers=headers)
        if response.status_code == 200:
            body_str = str(response.content, "utf-8")
            body_dict = json.loads(body_str)
            print(body_dict)
            words = ""
            if "words_result" in body_dict.keys():
                for line in body_dict.get("words_result"):
                    words += line.get("words") + "\n"
                return words
            else:
                return ""
        return ""


def main():
    """ 主函数 """
    args = get_args()
    textGO = TextGO(args.config)
    words = textGO.ocr(args.img)
    print(words)


if __name__ == "__main__":
    main()