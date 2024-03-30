def main():
   book_path = "books/frankenstein.txt"
   text = get_book_text(book_path)
   print(f"--- Begin report of {book_path} ---")
   print(word_count(text), "words found in the document\n")
   format_letter_count(letter_count(text))
   print("--- End report ---")

def get_book_text(path):
   with open(path) as f:
      return f.read()

def word_count(text):
   words = len(text.split())
   return words

def letter_count(text):
   letters = {}
   lower_text = text.lower()

   for c in lower_text:
      if c.isalpha():
         if c in letters:
            letters[c] += 1
         else:
            letters[c] = 1
   
   return letters

def format_letter_count(letters):
   for key, val in letters.items():
      print(f"The {key} character was found {val} times")

main()