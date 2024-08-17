import torch
import torch.nn as nn
from transformers import BertConfig, BertTokenizer, BertPreTrainedModel, BertModel
from tokenizers import BertWordPieceTokenizer
from bert import BERT
from bert_dataset import BertDataset
from torch.utils.data import DataLoader

# Generated word-piece tokeniser
tokenizer = BertWordPieceTokenizer("vocab/sample-vocab.txt", lowercase=True)

config = BertConfig(vocab_size=tokenizer.get_vocab_size(), num_labels=2)
model = BERT(config)

optimizer = torch.optim.AdamW(model.parameters(), lr=2e-5)
loss_function = nn.CrossEntropyLoss()

import torchtext
from torchtext.data.utils import get_tokenizer
from torchtext.datasets import WikiText103
from torch.utils.data import random_split

train_dataset, test_dataset, valid_dataset = WikiText103()
train_size = 10000
valid_size = 2000
test_size = 2000
# Define your custom lengths
train_len = int(len(train_dataset) * train_size)
valid_len = int(len(valid_dataset) * valid_size)
test_len = int(len(test_dataset) * test_size)

# Remaining data will be used for testing
train_data, _ = random_split(train_dataset, [train_len, len(train_dataset) - train_len])
valid_data, _ = random_split(valid_dataset, [valid_len, len(valid_dataset) - valid_len])
test_data, _ = random_split(test_dataset, [test_len, len(test_dataset) - test_len])

tokenizer = BertWordPieceTokenizer("vocab/sample-vocab.txt", lowercase=True)

# Tokenize and process the dataset
train_dataset = BertDataset(train_data, tokenizer)
valid_dataset = BertDataset(valid_data, tokenizer)
test_dataset = BertDataset(test_data, tokenizer)

batch_size = 1  # Adjust based on your GPU memory

train_dataloader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
valid_dataloader = DataLoader(valid_dataset, batch_size=batch_size, shuffle=False)
test_dataloader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)


# Set up training loop, loss function, and optimizer
optimizer = torch.optim.AdamW(model.parameters(), lr=2e-5)
loss_function = nn.CrossEntropyLoss()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
num_epochs = 20
# Train the model
for epoch in range(num_epochs):
    for batch in train_dataloader:
        model.zero_grad()

        input_ids = batch["input_ids"].to(device)
        attention_mask = batch["attention_mask"].to(device)
        labels = batch["labels"].to(device)

        logits = model(input_ids, attention_mask)
        loss = loss_function(logits, labels)
        loss.backward()
        optimizer.step()
        
torch.save(model.state_dict(), 'models/bert-custom.pth')

