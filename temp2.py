vocabulary = []

# Read vocabulary from file
with open("NLP_Sandhi_viched.txt", "r", encoding="utf-8") as vocab_file:
    for line in vocab_file:
        word = line.strip()
        if word:
            vocabulary.append(word)
perfect_sandhi = None

with open("output.txt", "r", encoding="utf-8") as file:
    content = file.read().splitlines()

for line in content:
    print(line)
    all_words_match = True
    matching_words = []
    for word in line.split():
        word = word.strip()
        if word not in vocabulary:
            all_words_match = False
            break
        else:
            matching_words.append(word)
    if all_words_match:
        perfect_sandhi = " + ".join(matching_words)
        break

if perfect_sandhi:
    print("Perfect sandhi found:", perfect_sandhi)
else:
    print("No perfect sandhi found.")
