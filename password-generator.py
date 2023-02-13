import random
import array

max_len = 8

digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
lowercase_characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
uppercase_characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
symbols = ["@", "#", "$", "%", "=", ":", "?", ".", "/", "|", "~", ">", "*", "(", ")", "<", "+"]

combined_list = digits + lowercase_characters + uppercase_characters + symbols

random_digit = random.choice(digits)
random_lower = random.choice(lowercase_characters)
random_upper = random.choice(uppercase_characters)
random_symbol = random.choice(symbols)

password = random_digit + random_lower + random_upper + random_symbol

for x in range(max_len-4):
    password = password + random.choice(combined_list)
    password_list = array.array("u", password)
    random.shuffle(password_list)

final_password = " "
for x in password_list:
    final_password = final_password + x

print(final_password)
