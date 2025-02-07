print("--- Begin report of books/frankenstein.txt ---")
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = len(file_contents.split())
    print(f"{words} words found in the document")
main()

print("  ")

def main2():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        lowercase = file_contents.lower()
        char_dict = {}
        for char in lowercase:
            if char.isalpha():
                char_dict[char] = char_dict.get(char, 0) + 1
        dict_list = list(char_dict.items())
        dict_list.sort(reverse=True, key=lambda item: item[1])
    for yeet in dict_list:
        print(f"The '{yeet[0]}' character was found {yeet[1]} times")
main2()

