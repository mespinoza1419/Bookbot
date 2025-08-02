import sys 
from stats import number_of_words 
from stats import number_of_characters
from stats import sort_dictionary

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents=f.read()
    return file_contents

def main():
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        r=get_book_text(sys.argv[1])
        num_words=number_of_words(r)
        dict_of_letters=number_of_characters(r)
        list_of_letters=sort_dictionary(dict_of_letters)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for ele in list_of_letters:
            print(f"{ele["char"]}: {ele["num"]}")
        print("============= END ===============")


main()
