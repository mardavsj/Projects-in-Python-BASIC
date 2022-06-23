# Password Generator
import random
import array

# maximum length for the password.
max_len = 8

# declaration of characters array that we need in our password.
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
lowercase_characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
uppercase_characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
symbols = ["@", "#", "$", "%", "=", ":", "?", ".", "/", "|", "~", ">", "*", "(", ")", "<", "+"]

# combine all the characters arrays to form one array.
combined_list = digits + lowercase_characters + uppercase_characters + symbols

# select at least one character from each character set randomly.
random_digit = random.choice(digits)
random_lower = random.choice(lowercase_characters)
random_upper = random.choice(uppercase_characters)
random_symbol = random.choice(symbols)

# combine the random characters.
password = random_digit + random_lower + random_upper + random_symbol

# max length of password is 7, so we have to fill the rest 3 characters.
for x in range(max_len-4):
    password = password + random.choice(combined_list)
    # prevent the password from having a consistent pattern.
    password_list = array.array("u", password)
    random.shuffle(password_list)

# now append the characters to form the password.
final_password = " "
for x in password_list:
    final_password = final_password + x

# print out the password.
print(final_password)