import torch.nn as nn
from transformers import BertModel, BertTokenizer


class SiameseBERT(nn.Module):
    def __init__(self, model_name):
        super(SiameseBERT, self).__init__()
        self.bert = BertModel.from_pretrained(model_name)
        self.cos_sim = nn.CosineSimilarity(dim=-1)

    def forward(self, input_ids1, attention_mask1, input_ids2, attention_mask2):
        outputs1 = self.bert(input_ids=input_ids1,
                             attention_mask=attention_mask1)  
        outputs2 = self.bert(input_ids=input_ids2,
                             attention_mask=attention_mask2)  

        
        pooled_output1 = outputs1.last_hidden_state[:, 0]
        pooled_output2 = outputs2.last_hidden_state[:, 0]

        similarity_score = self.cos_sim(pooled_output1, pooled_output2)

        return similarity_score
