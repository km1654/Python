from cs50 import get_string

sentence = get_string("Text ")
count_letters = 0
count_sentences = 0

for i in range(len(sentence)):
    if sentence[i].islower() or sentence[i].isupper():
        count_letters += 1

for i in range(len(sentence)):
    if sentence[i] == "!" or sentence[i] == "." or sentence[i] == "?":
        count_sentences += 1

count_words = len(sentence.split())
# print(len(sentence.split()))
# print(count_words)

avg_letters = (100 * count_letters) / count_words
avg_sentences = (100 * count_sentences) / count_words

index = (0.0588 * avg_letters) - (0.296 * avg_sentences) - 15.8
# print(index)

if index < 1:
    print("Before Grade 1")
if index >= 1 and index < 16:
    print("Grade: ", round(index))
if index >= 16:
    print("Grade: 16+")
