def replace_words(dictionary,sentence):
    sentence=sentence.split()
    for i in range(len(dictionary)):
        for j in range (len(sentence)):
            if dictionary[i] in sentence[j][:len(dictionary[i])]:
                sentence[j]=dictionary[i]
    return ' '.join(sentence)

dictionary = ["cat","bat","rat"]

sentence = "the cattle was rattled by the battery"

print(f'Actual Sentence->{sentence}\n'
      f'Modified Sentence->{replace_words(dictionary,sentence)}')
