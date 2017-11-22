

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

frequency1 = {letter:0 for letter in alphabet}
for line in open("example.txt", encoding='utf8'):
    for char in line:
        if 'а' <= char <= 'я' or 'А' <= char <= 'Я':
            letter = char.lower()
            frequency1[letter] += 1

frequency2 = {letter:0 for letter in alphabet}
for char in input():
    if 'а' <= char <= 'я' or 'А' <= char <= 'Я':
        letter = char.lower()
        frequency2[letter] += 1
        
sum1 = sum(frequency1[letter] for letter in alphabet)
sum2 = sum(frequency2[letter] for letter in alphabet)
percent1 = ["{0:2.1f}".format(frequency1[letter]*100/sum1) for letter in alphabet]
percent2 = ["{0:2.1f}".format(frequency2[letter]*100/sum2) for letter in alphabet]
print('\t'.join(list(alphabet)))
print('\t'.join(list([str(frequency2[letter]) for letter in alphabet])))
#print('\t'.join(percent1).replace('.', ','))
print('\t'.join(percent2).replace('.', ','))
