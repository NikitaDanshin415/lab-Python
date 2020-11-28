import functions

file = open("test.txt", "r", encoding="UTF-8")

text = file.read().replace("\n", " ")

# #Анализ
# result = {}
# result["Всего слов"] = functions.getWordsCount(text)
# result["Всего предложений"] = functions.getPrepCount(text)
# result["Предложения"] = functions.getPrepWithLen(text)
# result["Слова"] = functions.printWordsWithLen(text)
# result["Знаки препинания"] = functions.printPunctuationCount(text)

# #работа с бинарным файлом
# functions.saveToBinFile("qwe", result)
# obj = functions.readToBinFile("qwe")

# #Печать объекта
# functions.printObj(result)

# работа с параграфами
# paragList = functions.getParagText(text)
# print(paragList)
# print(functions.sortText(paragList))
#
# functions.saveAsTxt("paragFile.txt", paragList)
