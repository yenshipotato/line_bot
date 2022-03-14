import requests


def pros(s):
    p = s.split("\n")
    for sentence in p:
        if sentence.__len__() < 4:
            p.remove(sentence)
    count = 0
    for sentence in p:
        count += sentence.__len__()
    return "字數 : "+str(count)


def prou(url='https://cdn.discordapp.com/attachments/758157661740073031/878642167126581258/message.txt'):
    responce = requests.get(url)
    responce.encoding = "utf-8"
    return pros(responce.text)


if __name__ == '__main__':
    prou()
