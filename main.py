import sys
from stats import get_book_text, words_count, chara_count, dict_to_list, sort_on

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    book_path = sys.argv[1]
#find words count
    count = words_count(book_path)
#find charater count    
#    print(f"Found {len(count)} total words")
    c_count = chara_count(book_path)
#words dict to list with dict {char,num}
    list = dict_to_list(c_count)
    list.sort(reverse=True, key=sort_on)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {len(count)} total words")
    print("--------- Character Count -------")
    for item in list:
        if item['chara'].isalpha():
            print(f"{item['chara']}: {item['num']}") 
    print("============= END ===============")
main()