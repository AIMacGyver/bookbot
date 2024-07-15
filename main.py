def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_dict = count_characters(text)
    print_book_report(num_words, char_dict)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(book_text):
    words = book_text.split()
    return len(words)


def count_characters(book_text):
    char_dict = {}
    for c in book_text:
        lowered = c.lower()
        if lowered in char_dict:
            char_dict[lowered] += 1
        else:
            char_dict[lowered] = 1
    return char_dict


def print_book_report(num_words, char_dict):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()
    for k, v in sorted(char_dict.items(), key=lambda x: x[1], reverse=True):
        if k.isalpha():
            print(f"The '{k}' character was found {v} times")
    print("--- End report ---")


if __name__ == "__main__":
    main()
