import random

global generated_password
alphabet = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e',
            'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j',
            'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o',
            'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't',
            'U', 'u', 'V', 'v', 'X', 'x', 'Y', 'y', 'Z', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '.', ',', ':', ';', '#', '%', '&', '/', '?']

class Password:
    def generate():
        global generated_password
        generated_password = random.choice(alphabet) + random.choice(alphabet) + random.choice(numbers) + random.choice(symbols) + random.choice(alphabet) + random.choice(numbers) + random.choice(symbols) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(numbers) + random.choice(symbols) + random.choice(alphabet) + random.choice(numbers) + random.choice(symbols) + random.choice(alphabet)

        return generated_password

    generate()


Password()

