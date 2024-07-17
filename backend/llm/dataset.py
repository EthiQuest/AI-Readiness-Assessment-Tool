import torch
from torch.utils.data import Dataset
import pandas as pd
from transformers import BertTokenizer

class AIEthicsDataset(Dataset):
    def __init__(self, csv_file='data/ethics_assessment/ai_ethics_dataset.csv', max_length=512):
        self.data = pd.read_csv(csv_file)
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.max_length = max_length
        self.principles = self.data['principle'].unique()
        self.principle_to_id = {principle: i for i, principle in enumerate(self.principles)}

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        text = self.data.iloc[idx]['text']
        principle = self.data.iloc[idx]['principle']

        encoding = self.tokenizer.encode_plus(
            text,
            add_special_tokens=True,
            max_length=self.max_length,
            return_token_type_ids=False,
            padding='max_length',
            truncation=True,
            return_attention_mask=True,
            return_tensors='pt',
        )

        principle_id = self.principle_to_id[principle]

        return {
            'input_ids': encoding['input_ids'].squeeze(),
            'attention_mask': encoding['attention_mask'].squeeze(),
            'labels': torch.tensor(principle_id, dtype=torch.long)
        }

# Usage example:
# dataset = AIEthicsDataset()