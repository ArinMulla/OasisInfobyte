import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    password_length = int(input("Enter the total length of the password: "))
    generated_password = generate_password(password_length)
    print(f"Your password is: {generated_password}")

if __name__ == "__main__":
    main()
