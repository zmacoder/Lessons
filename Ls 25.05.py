file = open ('file.txt', 'w', encoding='utf-8')
if file.writable():
    print(file.write())
else:
    


# if file.readable():
#     print(file.read)
# else:
#     file.write('dssa')
# print(file.read())
# print(file.read().split('\n'))
# print(file.readline())
# print(file.readline())


# for line in file:
#     # print(line, end="")
#     print(line.replace('\n', " "), end="")
#     # print(line.replace('\n', ''))
# # print(dir(file))