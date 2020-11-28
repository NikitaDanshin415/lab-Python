import pickle
import string
import re


def deletePunctuation(text):
    return text.translate(str.maketrans(dict.fromkeys(string.punctuation))).replace("\n", " ")


# <количество слов>,
def getWordsCount(text):
    return len(deletePunctuation(text).split(" "))


# <количество предложений>,
def getPrepCount(text):
    split_regex = re.compile(r'[.|!|?|…]')
    sentences = list(filter(lambda t: t, [t.strip() for t in split_regex.split(text)]))
    return len(sentences)


# список из кортежей из 2-х элементов вида (само предложение, <количество слов>),
def getPrepWithLen(text):
    result = []
    for s in re.split(r'(?<=[.!?…]) ', text):
        result.append([s, len(s.split())])
    return result


#  словарь из элементов {слово: <количество букв>},
def printWordsWithLen(text):
    dict = {}
    list(map(lambda x: dict.update({x: len(x)}), deletePunctuation(text).split()))
    return dict


# словарь из элементов {знак препинания: <количество таких знаков в тексте>}.
def printPunctuationCount(text):
    dict = {}
    for i in range(0, len(string.punctuation)):
        if text.count(string.punctuation[i]) > 0:
            dict.update({string.punctuation[i]: text.count(string.punctuation[i])})
    return dict


# Сохранить полученный объект в двоичный файл с помощью модуля pickle
def saveToBinFile(fileName, obj):
    with open(fileName, "wb") as file:
        pickle.dump(obj, file)


def readToBinFile(fileName):
    with open(fileName, "rb") as file:
        res = pickle.load(file)
    return res


def printObj(obj):
    for i in obj:
        print(f"{i} : {obj[i]}")


# Разбить текст на абзацы
def getParagText(text):
    paragDivider = int(input("Введите количество предложений в параграфе: "))

    finalText = "    "
    allPreps = list(re.split(r'(?<=[.!?…]) ', text))
    count = 0
    for i in range(len(allPreps)):
        if count == paragDivider:
            finalText += "\n"
            finalText += "    "
            count = 0
        finalText += allPreps[i] + " "
        count += 1
        if i == len(allPreps)-1:
            finalText += "\n"
    return finalText

# Абзацы отсортировать по количеству слов в них.
def sortText(text):
    listParag = list(re.split(r'(?<=[\n])', text))
    listParag.sort(key=len)
    return("".join(listParag))


def saveAsTxt(fileName, obj):
    paragFile = open(fileName, "w", encoding="UTF-8")

    for i in obj:
        paragFile.write(i)
    paragFile.close()