def mapper(sentences):
    words = sentences.split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

def reducer(frequencies):
    word_count = {}
    for frequency in frequencies:
        for word, count in frequency.items():
            if word in word_count:
                word_count[word] += count
            else:
                word_count[word] = count
    return word_count


txt = [" "]

mapper_result=[]
print("\nMapper result:")
for sentences in txt:
    result = mapper(sentences)
    mapper_result.append(result)
    for word, count in result.items():
        print(f"{word} : {count}")

reduce_result = reducer(mapper_result)

print("\nReducer result:")
for word, count in reduce_result.items():
    print(f"{word}: {count}")
