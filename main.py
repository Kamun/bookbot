def countwords(contents):
    words = contents.split()
    wordcount = 0
    for word in words:
        wordcount += 1
    print(f"{wordcount} words found in the document")
    return wordcount

def countcharacters(contents):
    lettercount = {}
    lowercase = contents.lower()
    for letter in lowercase:
        if letter not in lettercount:
            lettercount[letter] = 1
        else:
            lettercount[letter] += 1
    return lettercount

def sort_by(dict):
    return dict[1]

def makereport(wordcount, lettercount):
    sortletters = sorted(lettercount.items(), key=sort_by, reverse=True)
    print("--- Begin report of book/frankenstein.txt ---")
    print(f"{wordcount} words found in the document")
    for letter, count in sortletters:
        if letter.isalpha() == True:
            print(f"The '{letter}' character appears {count} times")
    print("--- End report ---")

def main ():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    wordcount = countwords(file_contents)
    lettercount = countcharacters(file_contents)
    makereport(wordcount, lettercount)
main()
