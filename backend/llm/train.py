import torch
from torch.utils.data import DataLoader
from torch.optim import AdamW
from .model import AIEthicsModel
from .dataset import AIEthicsDataset
from .tokenizer import tokenizer

def train_model(train_csv, val_csv, epochs=10, batch_size=32, learning_rate=2e-5):
    train_dataset = AIEthicsDataset(train_csv)
    val_dataset = AIEthicsDataset(val_csv)

    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=batch_size)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = AIEthicsModel(num_labels=len(train_dataset.principles)).to(device)

    optimizer = AdamW(model.parameters(), lr=learning_rate)
    criterion = nn.CrossEntropyLoss()

    for epoch in range(epochs):
        model.train()
        total_loss = 0
        for batch in train_loader:
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            labels = batch['labels'].to(device)

            optimizer.zero_grad()
            outputs = model(input_ids, attention_mask)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            total_loss += loss.item()

        # Validation
        model.eval()
        val_loss = 0
        correct = 0
        total = 0
        with torch.no_grad():
            for batch in val_loader:
                input_ids = batch['input_ids'].to(device)
                attention_mask = batch['attention_mask'].to(device)
                labels = batch['labels'].to(device)

                outputs = model(input_ids, attention_mask)
                loss = criterion(outputs, labels)
                val_loss += loss.item()

                _, predicted = torch.max(outputs, 1)
                total += labels.size(0)
                correct += (predicted == labels).sum().item()

        print(f"Epoch {epoch+1}/{epochs}, Train Loss: {total_loss/len(train_loader):.4f}, Val Loss: {val_loss/len(val_loader):.4f}, Val Accuracy: {100 * correct / total:.2f}%")

    return model

# Usage example:
# model = train_model('path_to_train.csv', 'path_to_val.csv')
# Example usage (don't include this in the file):
# vocab_size = 10000  # This should match your actual vocabulary size
# model = AIReadinessLLM(vocab_size=vocab_size, embed_size=256, hidden_size=512, num_layers=2)
# train_dataset = AIReadinessDataset('path_to_train_data.csv', tokenizer)
# val_dataset = AIReadinessDataset('path_to_val_data.csv', tokenizer)
# trained_model = train_model(model, train_dataset, val_dataset) 