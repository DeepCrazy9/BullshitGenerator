import random
import json

data = json.load(open("data.json", encoding="utf-8"))


def generator(title, length):
    """
    :param title: 文章标题
    :param length: 生成正文的长度
    :return: 返回正文内容
    """
    body = ""
    temp = ""
    textfilter = [""]  # 解决了重复问题
    norepeat = 50  # 50句话里没有重复。

    while len(body) < length:
        num = random.randint(0, 100)
        if num < 10:
            temp = random.choice(data["famous"]) \
                .replace('a', random.choice(data["before"])) \
                .replace('b', random.choice(data['after'])) + "\r\n"  # 解决了一句话没写完就换行的问题。比如bosh句子后有时候会直接连上一个换行。
        elif num < 20:
            temp = random.choice(data["famous"]) \
                .replace('a', random.choice(data["before"])) \
                .replace('b', random.choice(data['after']))
        else:
            temp = random.choice(data["bosh"])

        while len(textfilter) < norepeat:
            for i in textfilter:
                if i == "":
                    i = temp
                    body += temp
                elif i != temp:
                    textfilter.append(temp)
                    body += temp
                else:
                    break
            break
        else:
            textfilter.pop(0)
            continue

        body = body.replace("x", title)

    return body


if __name__ == '__main__':
    title = input("请输入文章主题:")
    length = int(input("请输入文章长度（正整数）:"))
    text = generator(title, length)
    print(text)
