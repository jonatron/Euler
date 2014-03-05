# The answer to Life, the Universe and Everything
words_file = open("words.txt", "rb")
words_list = words_file.read().split(",")

words = [quoted_word.strip('"') for quoted_word in words_list]

word_values = []
for word in words:
    word_values.append(sum([ord(l) - 64 for l in word]))  # A is #65 in ASCII
max_word_value = max(word_values)

# Generate Triangle Numbers up to max word value
triangles = []
triangle = 1
i = 1
while triangle < max_word_value:
    triangle = (i * 0.5) * (i + 1)
    triangles.append(int(triangle))
    i += 1

num_triangle_words = 0
for word_value in word_values:
    if word_value in triangles:
        num_triangle_words += 1
print num_triangle_words
