# backend/llm/model.py

import torch
import torch.nn as nn

class AIReadinessLLM(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(AIReadinessLLM, self).__init__()
        self.layer1 = nn.Linear(input_size, hidden_size)
        self.layer2 = nn.Linear(hidden_size, output_size)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.layer1(x)
        x = self.relu(x)
        x = self.layer2(x)
        return x

# Placeholder for model instantiation
# model = AIReadinessLLM(input_size, hidden_size, output_size)