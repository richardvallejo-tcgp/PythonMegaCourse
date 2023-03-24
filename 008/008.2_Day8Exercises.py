'''
Day 8 Exercises
'''
folder = "008.0_Day8Files"

'''
Code Experiments
'''
# with open("008.0_Day8Files/docs.txt", "r") as file: # This code block will result in an error because the file does not exist
    # file.read()

with open("008.0_Day8Files/doc.txt") as file:
    print(file.read())

with open("008.0_Day8Files/doc.txt", "r") as file:
    print(file.read())
# file.read() # This line produces an error because it is outside of the 'with' context and 'file' is closed

with open("008.0_Day8Files/doc.txt", "w") as file:
    print("Hello")

with open("008.0_Day8Files/doc.txt", "r") as file:
    # file.read() # If this line preceded our variable definition below, 'content' would be empty
    content = file.read()

print(content)
print(content)
print(content)


'''
Bonus
'''
date = input("Enter today's date: ").replace("/", "-")
mood = input("Rate your mood from 1 to 10: ")
response = input("Describe how you're feeling today:\n")

with open(f"{folder}/journal/{date}.txt", "w") as file:
    mood = f"Mood rating: {mood}"
    file.write(mood)
    file.write("\n" + f"{len(mood) * '-'}" + 2 * "\n")
    file.write(response)


'''
Coding Exercise 1
'''
filename = f"{folder}/coin.txt"
with open(filename, "r") as file:
    results = file.readlines()
    results = [result.strip("\n") for result in results]

flip_count = int(input("Enter number of coins to flip: "))
n = 0
while n < flip_count:
    coin_result = ""
    while coin_result != "heads" and coin_result != "tails":
        coin_result = input("Flip a coin and enter which side lands facing up ('heads' or 'tails'): ")

    results.append(coin_result)
    result_rate = results.count(coin_result) / len(results)
    print(f"{coin_result.capitalize()}: {float(result_rate * 100)}%")

    n = n + 1

with open(filename, "w") as file:
    file.writelines([result + "\n" for result in results])


'''
Bug Fixing Exercise 1
'''
with open("file.txt", 'r') as file:
    # print(file.read())
    # print(len(file.read()))

    content = file.read()
    print(content)
    print(len(content))
