Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> text_1 = "hello this is python programming and python is used for game development also. You can use python for machine learning also"
>>> text_2 = "python programming is a general purpose language used for machine learning, game development and few other things"
>>> token_1 = text_1.split()
>>> token_1
['hello', 'this', 'is', 'python', 'programming', 'and', 'python', 'is', 'used', 'for', 'game', 'development', 'also.', 'You', 'can', 'use', 'python', 'for', 'machine', 'learning', 'also']
>>> token_2 = text_2.split()
>>> token_2
['python', 'programming', 'is', 'a', 'general', 'purpose', 'language', 'used', 'for', 'machine', 'learning,', 'game', 'development', 'and', 'few', 'other', 'things']
>>> stopwords = ['and','am','are','the','also','is','use','you','for','few','this','a','used','can']
>>> words_1 = []
>>> words_2 = []
>>> for word in token_1:
	if word not in stopwords:
		words_1.append(word)

		
>>> words_1
['hello', 'python', 'programming', 'python', 'game', 'development', 'also.', 'You', 'python', 'machine', 'learning']
>>> for word in token_2:
	if word not in stopwords:
		words_2.append(word)

		
>>> words_2
['python', 'programming', 'general', 'purpose', 'language', 'machine', 'learning,', 'game', 'development', 'other', 'things']
>>> set_1 = set(words_1)
>>> set_2 = set(words_2)
>>> set_1
{'hello', 'game', 'also.', 'learning', 'You', 'machine', 'python', 'development', 'programming'}
>>> set_2
{'game', 'things', 'learning,', 'machine', 'language', 'other', 'python', 'development', 'purpose', 'programming', 'general'}
>>> len(set_1 & set_2) / len(set_1 | set_2)
0.3333333333333333
>>> 
