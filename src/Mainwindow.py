import requests

if __name__ == '__main__':
    response = requests.get("https://www.baidu.com/")
    response.encoding = "utf-8"
    print(response.text)