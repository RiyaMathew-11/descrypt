import torch.nn as nn
from transformers import BertModel


class SiameseBERT(nn.Module):
    def __init__(self, model_name):
        super(SiameseBERT, self).__init__()
        self.bert = BertModel.from_pretrained(model_name)
        self.cos_sim = nn.CosineSimilarity(dim=-1)

    def forward(self, input_ids1, attention_mask1, input_ids2, attention_mask2):
        output_set_1 = self.bert(input_ids=input_ids1,
                             attention_mask=attention_mask1)  
        output_set_2 = self.bert(input_ids=input_ids2,
                             attention_mask=attention_mask2)  

        # Generates out vectors with needed dims
        output_vec1 = output_set_1.last_hidden_state[:, 0]
        output_vec2 = output_set_2.last_hidden_state[:, 0]

        similarity_score = self.cos_sim(output_vec1, output_vec2)

        return similarity_score
