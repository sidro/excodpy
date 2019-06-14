def single_letter_count(word, letter):
    count = 0
    letter = letter.lower()
    word = word.lower()
    for i, v in enumerate(word):
        if letter in word[i]:
            count += 1
    return count


print(single_letter_count("HelLlllo World", "l"))
