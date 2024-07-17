import torch
from torch.utils.data import DataLoader
from torch.optim import Adam
from .model import AIReadinessLLM
from .dataset import AIReadinessDataset

def train_model(model, train_dataset, val_dataset, epochs=10, batch_size=32, learning_rate=0.001):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=batch_size)

    criterion = torch.nn.CrossEntropyLoss()
    optimizer = Adam(model.parameters(), lr=learning_rate)

    for epoch in range(epochs):
        model.train()
        total_loss = 0
        for batch in train_loader:
            inputs = batch['input_ids'].to(device)
            labels = batch['label'].to(device)

            optimizer.zero_grad()
            outputs, _ = model(inputs)
            loss = criterion(outputs.view(-1, outputs.size(-1)), labels.view(-1))
            loss.backward()
            optimizer.step()

            total_loss += loss.item()

        # Validation
        model.eval()
        val_loss = 0
        with torch.no_grad():
            for batch in val_loader:
                inputs = batch['input_ids'].to(device)
                labels = batch['label'].to(device)
                outputs, _ = model(inputs)
                loss = criterion(outputs.view(-1, outputs.size(-1)), labels.view(-1))
                val_loss += loss.item()

        print(f"Epoch {epoch+1}/{epochs}, Train Loss: {total_loss/len(train_loader):.4f}, Val Loss: {val_loss/len(val_loader):.4f}")

    return model

# Example usage (don't include this in the file):
# vocab_size = 10000  # This should match your actual vocabulary size
# model = AIReadinessLLM(vocab_size=vocab_size, embed_size=256, hidden_size=512, num_layers=2)
# train_dataset = AIReadinessDataset('path_to_train_data.csv', tokenizer)
# val_dataset = AIReadinessDataset('path_to_val_data.csv', tokenizer)
# trained_model = train_model(model, train_dataset, val_dataset) 