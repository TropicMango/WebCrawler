import AdvGoogle
import AdvDictionary
import AdvCambridge
import AdvFreeDictionary
import AdvMerriam
import csv


def generate_list(location):  # opens the text file
    file = open(location, "r")
    file_list = []
    for x, line in enumerate(file):
        if x % 1000 == 0:
            file_list.append(line[:-1])
    return file_list


def process_list(file_list):  # splits the line into word and pron
    word_list = []
    for line in file_list:
        index = line.index(" ")
        word_list.append([line[:index], line[index + 1:]])
        # print [line[:index], line[index+1:]]

    return word_list


def add_crawl_list(word_list, dictionary):  # goes onto the web and finds pron
    updated_list = []
    var = 0

    for line in word_list:
        print dictionary.lookup_word(line[0])  # the dictionary processes the word
        line.append(dictionary.getWord().encode('utf-8'))
        line.append(dictionary.getPron().encode('utf-8'))
        updated_list.append(line)
        if dictionary.getWord() == "------------":
            var += 1

    print 1 - 1.0 * var / len(word_list)  # prints the percentage of words that it have
    return updated_list


def create_file(word_list):
    with open('pronunciations.csv', 'wb') as csvfile:  # starts up writer
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(["Input", "Cantab Pron", "Dictionary Word", "Dictionary Pron"])
        for line in word_list:
            filewriter.writerow(line)


if __name__ == "__main__":
    FileList = generate_list(
        "/Users/liarch29/Desktop/Python for fun~/AISense/Dictionaries/Converter/cantab-TEDLIUM/cantab-TEDLIUM.txt")
    # ^^^ Change the location of the file above ^^^ 
    WordList = process_list(FileList)
    WordList = add_crawl_list(WordList, AdvDictionary)
    # AdvGoggle, AdvMerriam, AdvDictionary, AdvCambridge, AdvFreeDictionary
    create_file(WordList)
    # print WordList
