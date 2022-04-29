def firstlastword(sentence):
    words = sentence.split()
    if len(words)== 1:
        return words[0]
    new_words = [words[-1]] + words[1:-1] + [words[0]]
    return " ".join(new_words)
    
# print(firstlastword("I Love Food"))
