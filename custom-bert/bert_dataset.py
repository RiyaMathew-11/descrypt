import torch
import torch.nn as nn


class BertDataset(torch.utils.data.Dataset):
    def __init__(self, texts, tokenizer, max_len=128):
        self.texts = texts
        self.tokenizer = tokenizer
        self.max_len = max_len

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        text = self.texts[index]
        encoding = self.tokenizer.encode(text, add_special_tokens=True)
        ids = encoding.ids
        mask = encoding.attention_mask

        # Padding
        padding_len = self.max_len - len(ids)
        ids += [0] * padding_len
        mask += [0] * padding_len

        return {
            "input_ids": torch.tensor(ids, dtype=torch.long),
            "attention_mask": torch.tensor(mask, dtype=torch.long),
        }
