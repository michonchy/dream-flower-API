import json

# import requests
# 「とんで」を9回「まわって」を3回繰り返した後「まわる」と表示して改行する、をn回繰り返すプログラムを作成せよ。
# 「とんで」「まわって」と3行文の繰り返しは必ず繰り返し構文を使うこと。

class InvalidError(Exception):
    pass
def is_number(x: str):
    if x.startswith("-"):
        x = x[1:]
    if not x.isdigit():
        return False
    return True
def number(x):
    if not is_number(x):
        raise InvalidError("整数値を入力してください。")
    return int(x)

def is_dream_flower(n):
    dream_flower = ""
    for a in range(n):
        music = ""
        for i in range (13):
            if i <= 8:
                music += "とんで"
            elif 8 < i <= 11:
                music += "まわって"
            else:
                music += "まわる"
        dream_flower += music + "\n"
    return dream_flower




def validate_number(x):
    if x < 0:
        raise InvalidError("整数値を入力してください。")


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    print(event)
    try:
        n = event.get('queryStringParameters').get('numbers')
        n = number(n)
        validate_number(n)
        print(n)
    except Exception as e:
        return{
        "statusCode": 400,
        "headers":{
            "Content-type": "application/json;charset=UTF-8"
        },
        "body":json.dumps({
            "message":str(e)
        },ensure_ascii=False).encode("utf8"),
    }

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    return {
        "statusCode": 200,
        "headers":{
            "Content-type": "application/json;charset=UTF-8"
        },
        "body": json.dumps({
            "message": is_dream_flower(n),
            #"location": ip.text.replace("\n", "")
        },ensure_ascii=False).encode("utf8"),
    }
