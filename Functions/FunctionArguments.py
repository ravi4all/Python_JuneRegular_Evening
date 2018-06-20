def jaccard_dist(str_1, str_2):

    str_1 = str_1.split()
    str_2 = str_2.split()

    stopwords = ['is','am','are','the','has','a','you',
                 'can','use','this','that','for']

    words_1 = []
    words_2 = []

    for word in str_1:
        if word not in stopwords:
            words_1.append(word)

    for word in str_2:
        if word not in stopwords:
            words_2.append(word)

    set_1 = set(words_1)
    set_2 = set(words_2)

    intersection = set_1.intersection(set_2)
    union = set_1.union(set_2)

    outcome = len(intersection) / len(union)

    print("String Match :",outcome * 100,"%")

text_1 = input("Enter text_1 : ")
text_2 = input("Enter text_2 : ")

jaccard_dist(text_1, text_2)