import torch
from torch.utils.data import Dataset
import pandas as pd

class AIReadinessDataset(Dataset):
    def __init__(self, csv_file, tokenizer):
        self.data = pd.read_csv(csv_file)
        self.tokenizer = tokenizer

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        text = self.data.iloc[idx]['text']
        label = self.data.iloc[idx]['label']

        # Tokenize the text
        tokens = self.tokenizer.encode(text, add_special_tokens=True, max_length=512, truncation=True, padding='max_length')
        
        return {
            'input_ids': torch.tensor(tokens, dtype=torch.long),
            'label': torch.tensor(label, dtype=torch.long)
        }

# Note: We'll define the tokenizer later when we have our vocabulary
# Example usage (don't include this in the file):
# dataset = AIReadinessDataset('path_to_your_csv_file.csv', tokenizer)