#hw2

scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
def scores_after_75(big):
    for i in big:
        if i > 75:
            print(i)

scores_after_75(scores)

print(list(i for i in scores if i > 75))

#hw3

words = ["Anna", "Alexey", "Alla", "Kazak"]
def polindrom_words(p_words):
    for i in p_words:
        if i == i[::-1]:
            print(i)


polindrom_words(words)


#hw 6

list_1 = ['apple', 'banana', 'cherry']
list_2 = ['orange', 'lemon', 'pineapple']
print(list(map(['apple', 'banana', 'cherry'], ['orange', 'lemon', 'pineapple'])))

# hw 5
list_2 = ('apple', 'banana', 'cherry')
def letter_quantity(letters):
    for i in letters:
        for x in i:
            print(len(x), end="")

letter_quantity(list_2)

print(len(list_2))

#hw 4
num_1 = int(input("Введите число: "))
def range_num(num_input):
    start = time.time()
    print(list(range(1, num_input+1)))
    end = time.time()
    print("время операции: ", f"{(end - start):.3f}")
range_num(num_1)

# #hw 1
names = ['alfred', 'tabitha', 'william', 'arla']
def upper_letter(upp):
    for i in upp:
        print((str(i.capitalize())))

upper_letter(names)

print(list(i.capitalize() lambda i: names))

