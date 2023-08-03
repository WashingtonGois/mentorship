import random

def main():

    secret_number = random.randint(1,100)

    i = 0
    while i < 5:
        ask = int(input("Guess a number: "))

        if secret_number == ask:
            print("Right number!")
            break
        elif ask > secret_number:
            print("Secret number is lesser than this number.")
        else:
            print("Secret number is bigger than this number.")
        
        i += 1
        
    print(f"The secret number is {secret_number}.")

if __name__ == "__main__":
    main()