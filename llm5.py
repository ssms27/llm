import tiktoken

tokenizer = tiktoken.get_encoding("gpt2")

text = (
    "Hello, do you like tea? <|endoftext|> In the sunlit terraces"
     "of someunknownPlace."
)
# integers = tokenizer.encode(text, allowed_special={"<|endoftext|>"})
# print(integers)
#
# strings = tokenizer.decode(integers)
# print(strings)

awk = "Akwirw ier"

eawk = tokenizer.encode(awk)
print(eawk)

for i in eawk:
    print(i, tokenizer.decode([i]))

dawk = tokenizer.decode(eawk)
print(dawk)