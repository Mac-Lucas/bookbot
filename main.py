import sys
from stats import count_words,numb_characters,chars_dict_to_sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
       return f.read()

"""book_path = 'books/frankenstein.txt'"""
if len(sys.argv) !=2:
     print (" Usage: python3 main.py <path_to_book>")
     sys.exit(1)

text=get_book_text(sys.argv[1])
count=numb_characters(text)
dic_to_list=chars_dict_to_sorted_list(count)
print("============ BOOKBOT ============")
print(f"Analyzing book fout at {sys.argv[1]}")
print("----------- Word Count ----------")
print (f"Found {count_words(text)} total words")
print('--------- Character Count -------')
for item in dic_to_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

print("============= END ===============")