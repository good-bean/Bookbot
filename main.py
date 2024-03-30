def main():
   book_path = "books/frankenstein.txt"
   text = get_book_text(book_path)
   print(word_count(text), "words in Frankenstein")
   print("The frequency of each character is as follows:", letter_count(text))

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
      if c in letters:
         letters[c] += 1
      else:
         letters[c] = 1
   
   return letters

main()