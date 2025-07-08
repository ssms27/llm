from GPTDatasetV1 import GPTDatasetV1
import tiktoken

def create_dataloader_v1(txt, batch_size=4, max_length=256,
                         stride=128, shuffle=True, drop_last=True,
                         num_workers=0):
    tokenizer = tiktoken.get_encoding("gpt2")                         #1
    dataset = GPTDatasetV1(txt, tokenizer, max_length, stride)   #2
    dataloader = DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=shuffle,
        drop_last=drop_last,     #3
        num_workers=num_workers     #4
    )

    return dataloader

 if __name__ == "__main__":
     with open("the-verdict.txt", "r", encoding="utf-8") as f:
         raw_text = f.read()

     dataloader = create_dataloader_v1(
         raw_text, batch_size=1, max_length=4, stride=1, shuffle=False)
     data_iter = iter(dataloader)  # 1
     first_batch = next(data_iter)
     print(first_batch)