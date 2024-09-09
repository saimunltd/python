import random


lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!@#$%^&*()_-+=/.><?/"
numbers = "1234567890"

all_chars = lower + upper + symbols + numbers
lengths = int(input("Enter your length\n: "))

password = "".join(random.sample(all_chars,lengths))
print("Generated password:",password)