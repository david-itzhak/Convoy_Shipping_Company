# work with the preset variable `words`

words_begin_with_a = [word for word in words if word.startswith(('a', 'A'))]
print(words_begin_with_a)