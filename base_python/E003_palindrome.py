# test to see if a word is a palindrome

word = str(input('Palindrome tester: '))
wordList = list()
wordListReversed = list()

for letter in word:
    wordList.append(letter)

wordListReversed = wordList.copy()
wordListReversed.reverse()

if wordListReversed == wordList:
    print(f'The word "{word}" is a palindrome')
else:
    print(f'The word "{word}" is not a palindrome')
