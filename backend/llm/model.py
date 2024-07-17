import torch.nn as nn
from transformers import BertModel

class AIEthicsModel(nn.Module):
    def __init__(self, num_labels):
        super(AIEthicsModel, self).__init__()
        self.bert = BertModel.from_pretrained('bert-base-uncased')
        self.dropout = nn.Dropout(0.1)
        self.classifier = nn.Linear(self.bert.config.hidden_size, num_labels)

    def forward(self, input_ids, attention_mask):
        outputs = self.bert(input_ids=input_ids, attention_mask=attention_mask)
        pooled_output = outputs.pooler_output
        pooled_output = self.dropout(pooled_output)
        logits = self.classifier(pooled_output)
        return logits

# Example usage (you don't need to include this in the file):
# model = AIReadinessLLM(vocab_size=10000, embed_size=256, hidden_size=512, num_layers=2)