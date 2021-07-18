name = input()
print('Hello', name, sep=', ', end='!')
# task1end)
#

# task2begin(
# var1
pinguins_hat = "   _~_    "
pinguins_head = "  (o o)   "
pinduins_body1 = " /  V  \  "
pinduins_body2 = "/(  _  )\ "
pinduins_feets = "  ^^ ^^   "

N = int(input())

print(pinguins_hat * N)
print(pinguins_head * N)
print(pinduins_body1 * N)
print(pinduins_body2 * N)
print(pinduins_feets * N)


# var2
# буква r перед элементами списка (массива) в строке - для того, чтобы каждый раз не писать "бэк-слеш" для экранирования управляющих символов
list_body_parts = [r'   _~_    ',
                   r'  (o o)   ',
                   r' /  V  \  ',
                   r'/(  _  )\ ',
                   r'  ^^ ^^   ']

N = int(input())

for i in range(len(list_body_parts)):
    print(list_body_parts[i] * N)
# task2end)


# task3begin(
N = int(input())
K = int(input())

print(K // N)
# task3end)


# task4bedin(
N = int(input())
K = int(input())

print(K % N)
# task4end)


# task5bedin(
N = int(input())

print(2 ** N)
# task5end)


# task6begin(
N = int(input())

print(N % 10)
# task6end)


# task7begin(
N = int(input())

print(N // 10)
# task7end)


print("don't belong to anything...string")

print("THIS BRANCH WAS CREATED BCSE OF THIS STRRRRRRRRRRRRRRRRRRIIIIIIIIIINNNNNNNNNNNGGGGGGGGG")

print("OH SHEE, HERE WE GO AGAIN.......")

print("ONLY FOR SECOND BIG PRINT")