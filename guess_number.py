# print("Word")
# age = input("Enter age: ")
# print(f"your age: {age}")

secret_number = 6
attempts = 5
while True:
    print(f"Attempts: {attempts}")
    number = int(input("Enter a number: "))
    if number > secret_number:
        print("Secret number is smaller")
    if number < secret_number:
        print("Secret number is bigger")
    if number == secret_number:
        print("Win")
        break
    attempts -= 1
    if attempts == 0:
        print("Your attempts = 0 you loser")
        break
