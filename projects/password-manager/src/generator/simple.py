import random
import string

def generate_password(
    length: int = 12,
    use_lowercase: bool = True,
    use_uppercase: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
    ) -> str:
        characters = ""
        
        if use_lowercase:
            characters += string.ascii_lowercase
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_digits:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation
            
        if not characters:
            print("Must have at least one character type.")
            
        if length <= 0:
            raise ValueError("Password length must be positive.")

        password = "".join(random.choice(characters) for _ in range(length))
        return password
        