# assignment1.py

#Task 1
def hello():
    return "Hello!"

#Task 2
def greet(name):
    return f"Hello, {name}!"

#Task 3
def calc(a, b, operation="multiply"):
    try:
        match operation:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b
            case "modulo":
                return a % b
            case "int_divide":
                return a // b
            case "power":
                return a ** b
            case _:
                return "Invalid operation"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"

#Task 4
def data_type_conversion(value, dtype):
    try:
        match dtype:
            case "int":
                return int(value)
            case "float":
                return float(value)
            case "str":
                return str(value)
            case _:
                return "Invalid type"
    except ValueError:
        return f"You can't convert {value} into a {dtype}."

#Task 5
def grade(*args):
    try:
        avg = sum(args) / len(args)
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"
    except (TypeError, ZeroDivisionError):
        return "Invalid data was provided."

#Task 6
def repeat(string, count):
    result = ""
    for _ in range(count):
        result += string
    return result

#Task 7 - possible solution
# def student_scores(method, **kwargs):
#     if method == "best":
#         return max(kwargs, key=kwargs.get)
#     elif method == "mean":
#         return sum(kwargs.values()) / len(kwargs)
#     return "Invalid method"

#Task 7 - the 2nd possible solution
def student_scores(method, **kwargs):
    if not kwargs:
        return "No student scores provided."

    if method == "best":
        return max(kwargs.items(), key=lambda item: item[1])[0]  # Returns the student with the highest score
    elif method == "mean":
        return sum(kwargs.values()) / len(kwargs)  # Returns the average score

    return "Invalid method. Use 'best' or 'mean'."

#Task 8
# def titleize(text):
#     little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}
#     words = text.split()
#     titleized = [words[0].capitalize()] + [word if word in little_words else word.capitalize() for word in words[1:-1]] + [words[-1].capitalize()]
#     return " ".join(titleized)

#Task 8 - the 2nd possible solution
def titleize(text):
    little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}
    words = text.split()

    # Ensure there is at least one word
    if not words:
        return ""

    titleized = []

    for i, word in enumerate(words):
        # Capitalize the first and last word, otherwise follow the little word rule
        if i == 0 or i == len(words) - 1 or word not in little_words:
            titleized.append(word.capitalize())
        else:
            titleized.append(word.lower())

    return " ".join(titleized)


#Task 9
def hangman(secret, guess):
    return "".join([char if char in guess else "_" for char in secret])

#Task 10
def pig_latin(sentence):
    vowels = "aeiou"
    words = sentence.split()
    pig_latin_words = []

    for word in words:
        if word[0] in vowels:
            pig_latin_words.append(word + "ay")
        elif "qu" in word[:3]:  # If "qu" appears early, handle it as a unit
            qu_index = word.index("qu") + 2  # Move everything before and including "qu"
            pig_latin_words.append(word[qu_index:] + word[:qu_index] + "ay")
        else:
            consonant_cluster_end = 0
            while consonant_cluster_end < len(word) and word[consonant_cluster_end] not in vowels:
                consonant_cluster_end += 1
            pig_latin_words.append(word[consonant_cluster_end:] + word[:consonant_cluster_end] + "ay")

    return " ".join(pig_latin_words)

print(hello())
print(greet("Alice"))
print(calc(10, 5, "add"))
print(data_type_conversion("123", "int"))
print(grade(90, 85, 88))
print(repeat("hi", 3))
print(student_scores("best", Alice=85, Bob=92, Carol=78))
print(titleize("the quick brown fox jumps over the lazy dog"))
print(hangman("alphabet", "ab"))
print(pig_latin("quick brown fox"))
