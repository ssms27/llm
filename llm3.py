import urllib.request
url = ("https://raw.githubusercontent.com/rasbt/" "LLMs-from-Scratch/main/ch02/01_main-chapter-code/" 
       "the-verdict.txt")

file_path = "the-verdict.txt"
urllib.request.urlretrieve(url, file_path)

with open(file_path, "r", encoding="utf-8") as f:
       raw_text = f.read()

print("Total number of characters in the text:", len(raw_text))  #20479
print(raw_text[:99])

preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
print(len(preprocessed))
