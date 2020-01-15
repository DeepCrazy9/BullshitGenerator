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
    norepeat = 30  # 50句话里没有重复。
    enter = 0

    while len(body) < length:
        num = random.randint(0, 100)
        a = textfilter[-1]
        if num < 10 and a not in data["bosh"] and enter != 0:
            enter = 0
            body += "\r\n"  # 解决了一句话没写完就换行的问题。比如bosh句子后有时候会直接连上一个换行。
        elif num < 20:
            enter += 1
            temp = random.choice(data["famous"]) \
                .replace('a', random.choice(data["before"])) \
                .replace('b', random.choice(data['after']))
        else:
            enter += 1
            temp = random.choice(data["bosh"])

        while len(textfilter) < norepeat:
            if temp not in textfilter:
                textfilter.append(temp)
                body += temp
            else:
                break
        else:
            textfilter.pop(0)

        body = body.replace("x", title)

    return body


if __name__ == '__main__':
    title = input("请输入文章主题:")
    length = int(input("请输入文章长度（正整数）:"))
    text = generator(title, length)
    print(text)
