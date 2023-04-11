sentence = "Hey I am walking here I am walking here o captain my captain water water everywhere nor a drop to drik"

sentence_list = []
words = sentence.split()
sentence_list.extend(words)
print(sentence_list,"\n")

sentence_set = set(sentence_list)
print(sentence_set,"\n")
num_unique = len(sentence_set)
print(num_unique)