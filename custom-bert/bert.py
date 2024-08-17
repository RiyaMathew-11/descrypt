import torch.nn as nn
from transformers import BertConfig, BertTokenizer, BertPreTrainedModel, BertModel


class BERT(nn.Module):
    def __init__(self, config):
        super(BERT, self).__init__()
        self.config = config
        self.bert = BertModel(config)
        self.dropout = nn.Dropout(config.hidden_dropout_prob)
        self.classifier = nn.Linear(config.hidden_size, config.num_labels)

    def forward(self, input_ids, attention_mask=None):
        outputs = self.bert(input_ids, attention_mask=attention_mask)
        pooled_output = outputs[1]
        pooled_output = self.dropout(pooled_output)
        logits = self.classifier(pooled_output)
        return logits