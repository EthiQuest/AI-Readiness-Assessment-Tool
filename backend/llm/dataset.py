import torch
from torch.utils.data import Dataset
import pandas as pd
from .tokenizer import tokenizer

class AIEthicsDataset(Dataset):
    def __init__(self, csv_file='data/ethics_assessment/ai_ethics_dataset.csv'):
        self.data = pd.read_csv(csv_file)
        self.principles = self.data['principle'].unique()
        self.principle_to_id = {principle: i for i, principle in enumerate(self.principles)}

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        text = self.data.iloc[idx]['text']
        principle = self.data.iloc[idx]['principle']

        encoded = tokenizer.encode(text)
        principle_id = self.principle_to_id[principle]

        return {
            'input_ids': encoded['input_ids'].squeeze(),
            'attention_mask': encoded['attention_mask'].squeeze(),
            'labels': torch.tensor(principle_id, dtype=torch.long)
        }

# Note: We'll define the tokenizer later when we have our vocabulary
# Example usage (don't include this in the file):
# dataset = AIReadinessDataset('path_to_your_csv_file.csv', tokenizer)