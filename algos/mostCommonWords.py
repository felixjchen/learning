import string
literatureText = "Jack and Jill went to the market to buy bread and cheese. Cheese is Jack's and Jill's favorite food."
wordsToExclude = ["and", "he", "the", "to", "is", "Jack", "Jill"]


def mostCommonWords(exclude, text):

    # O(n)
    text = text.lower()

    for punctuation in string.punctuation:
        text = text.replace(punctuation, " ")

    text = text.split(" ")

    exclude = [i.lower() for i in exclude]

    # O(n^2)
    frequency = {}
    for word in text:

        if word not in exclude:
            if word not in frequency:
                frequency[word] = 1
            else:
                frequency[word] += 1

    max_frequency = 0
    words = []

    for word in frequency.keys():
        if frequency[word] > max_frequency:
            max_frequency = frequency[word]
            words = []

        if frequency[word] == max_frequency:
            words.append(word)

    return words


print(mostCommonWords(wordsToExclude, literatureText))
