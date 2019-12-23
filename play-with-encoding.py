import codecs

f = codecs.open("README.txt", encoding="gb2312")
for line in f:
    print(repr(line))
