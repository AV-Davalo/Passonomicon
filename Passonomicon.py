import argparse
from itertools import product
import datetime

# ASCII Banner
banner = """

 ██▓███   ▄▄▄        ██████   ██████  ▒█████   ███▄    █  ▒█████   ███▄ ▄███▓ ██▓ ▄████▄   ▒█████   ███▄    █ 
▓██░  ██▒▒████▄    ▒██    ▒ ▒██    ▒ ▒██▒  ██▒ ██ ▀█   █ ▒██▒  ██▒▓██▒▀█▀ ██▒▓██▒▒██▀ ▀█  ▒██▒  ██▒ ██ ▀█   █ 
▓██░ ██▓▒▒██  ▀█▄  ░ ▓██▄   ░ ▓██▄   ▒██░  ██▒▓██  ▀█ ██▒▒██░  ██▒▓██    ▓██░▒██▒▒▓█    ▄ ▒██░  ██▒▓██  ▀█ ██▒
▒██▄█▓▒ ▒░██▄▄▄▄██   ▒   ██▒  ▒   ██▒▒██   ██░▓██▒  ▐▌██▒▒██   ██░▒██    ▒██ ░██░▒▓▓▄ ▄██▒▒██   ██░▓██▒  ▐▌██▒
▒██▒ ░  ░ ▓█   ▓██▒▒██████▒▒▒██████▒▒░ ████▓▒░▒██░   ▓██░░ ████▓▒░▒██▒   ░██▒░██░▒ ▓███▀ ░░ ████▓▒░▒██░   ▓██░
▒▓▒░ ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ░ ▒░   ░  ░░▓  ░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
░▒ ░       ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒  ░ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░  ░ ▒ ▒░ ░  ░      ░ ▒ ░  ░  ▒     ░ ▒ ▒░ ░ ░░   ░ ▒░
░░         ░   ▒   ░  ░  ░  ░  ░  ░  ░ ░ ░ ▒     ░   ░ ░ ░ ░ ░ ▒  ░      ░    ▒ ░░        ░ ░ ░ ▒     ░   ░ ░ 
               ░  ░      ░        ░      ░ ░           ░     ░ ░         ░    ░  ░ ░          ░ ░           ░ 
                                                                                 ░                            
                        Password Generator Tool - Made with <3 by Davalo
"""


current_year = datetime.datetime.now().year
current_month = datetime.datetime.now().strftime('%B')

symbols = ['!', '#', '$', '@']
common_suffixes = ['123', '321', '2024', '1', '2']

def generate_variations(base_name):
    variations = []
    variations.append(base_name.lower())
    variations.append(base_name.upper())
    variations.append(base_name.capitalize())
    char_replacements = {
        'a': ['a', '@'],
        'i': ['i', '1'],
        'o': ['o', '0'],
        'e': ['e', '3']
    }
    replacement_combinations = [char_replacements.get(char, [char]) for char in base_name]
    for combo in product(*replacement_combinations):
        variations.append(''.join(combo))
    return variations

def generate_passwords(name):
    variations = generate_variations(name)
    passwords = []
    
    for variation in variations:
        passwords.append(f"{variation}{current_year}")
        passwords.append(f"{variation}{current_month}{current_year}")
        
        for symbol in symbols:
            passwords.append(f"{variation}{current_year}{symbol}")
            passwords.append(f"{variation}{current_month}{current_year}{symbol}")
            for suffix in common_suffixes:
                passwords.append(f"{variation}{current_year}{suffix}{symbol}")
                passwords.append(f"{variation}{suffix}{current_year}{symbol}")
                passwords.append(f"{variation}{current_month}{current_year}{suffix}{symbol}")

    return list(set(passwords)) 

def main():
    print(banner)
    
    parser = argparse.ArgumentParser(description="Generate password variations for a given name.")
    parser.add_argument("name", type=str, help="The company name to base password variations on.")
    parser.add_argument("-o", "--output", type=str, help="Specify an output file to save generated passwords.")
    args = parser.parse_args()
    
    password_list = generate_passwords(args.name)

    if args.output:
        with open(args.output, 'w') as f:
            for password in password_list:
                f.write(password + "\n")
        print(f"\nPasswords saved to {args.output}")
    else:
        print("\nGenerated Passwords:")
        for password in password_list:
            print(password)

if __name__ == "__main__":
    main()
