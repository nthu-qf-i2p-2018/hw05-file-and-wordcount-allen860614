# -*- coding: utf-8 -*-

from collections import Counter

import csv
import json
import pickle
import string

def str_punc(word):
	print(word)
	if word in string.punctuation:
		return False
	else :
		return True
	end
	

def main(filename):
    # read file into lines
	txtfile = open(filename)
	lines = txtfile.readlines()

    # declare a word list
	all_words = []

    # extract all words from lines
	for line in lines:
        # split a line of text into a list words
        # "I have a dream." => ["I", "have", "a", "dream."]
		words = line.split()
		
		##print(words);
        # check the format of words and append it to "all_words" list
		for word in words:
            # then, remove (strip) unwanted punctuations from every word
			# "dream." => "dream"
			
			word = word.strip(string.punctuation)
            # check if word is not empty
			
			if word:
				# append the word to "all_words" list
				all_words.append(word)
	
    # compute word count from all_words
	txtfile.close()
	d = Counter(all_words)
	counter = d.most_common()
	
    # dump to a csv file named "wordcount.csv":
    # word,count
    # a,12345
    # I,23456
    
	with open("wordcount.csv", 'w', newline='') as csv_file:
        # create a csv writer from a file object (or descriptor)
		writer = csv.writer(csv_file)
        # write table head
		writer.writerow(['word', 'count'])
        # write all (word, count) pair into the csv writer
		writer.writerows(counter)
	csv_file.close()
    # dump to a json file named "wordcount.json"
	with open("wordcount.json", 'w') as json_file:
		json.dump(counter, json_file)
    # BONUS: dump to a pickle file named "wordcount.pkl"
    # hint: dump the Counter object directly
	with open("wordcount.pkl", 'wb') as pickle_file:
		pickle.dump(d, pickle_file)
	
if __name__ == '__main__':
    main("i_have_a_dream.txt")
