import urllib.request
import re
from SimpleTokenizerV1 import SimpleTokenizerV1
from SimpleTokenizerV2 import SimpleTokenizerV2

url = ("https://raw.githubusercontent.com/rasbt/" "LLMs-from-Scratch/main/ch02/01_main-chapter-code/" 
       "the-verdict.txt")

file_path = "the-verdict.txt"
urllib.request.urlretrieve(url, file_path)

with open(file_path, "r", encoding="utf-8") as f:
       raw_text = f.read()

# print("Total number of characters in the text:", len(raw_text))  #20479
# print(raw_text[:99])

preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]

#section 2.3
all_words = sorted(set(preprocessed))
vocab_size = len(all_words)
# print('Len of all words:', vocab_size)

#listing 2.2
vocab = {token:integer for integer, token in enumerate(all_words)}
for index, item in enumerate(vocab.items()):
       # if index == 1126:
       #        print(index, item)
       if index >= 2000:
              break

tokenizer = SimpleTokenizerV1(vocab)
text = """"It's the last he painted, you know," 
       Mrs. Gisburn said with pardonable pride."""
ids = tokenizer.encode(text)
# print(ids)
decoded_text = tokenizer.decode(ids)
# print(decoded_text)

all_tokens = sorted(list(set(preprocessed)))
all_tokens.extend(["<|endoftext|>", "<|unk|>"])
vocab = {token:integer for integer,token in enumerate(all_tokens)}
print(vocab)
print(len(vocab))
# print('len of all tokens:', len(vocab.items()))
#
# for index, item in enumerate(list(vocab.items())[-5:]):
#        print(item)


text1 = "Hello, do you like tea?"
text2 = "In the sunlit terraces of the palace."
text = " <|endoftext|> ".join((text1, text2))
print(text)
tokenizer = SimpleTokenizerV2(vocab)
print(tokenizer.encode(text))
print(tokenizer.decode(tokenizer.encode(text)))
