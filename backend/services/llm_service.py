import torch
from backend.llm.model import AIEthicsModel
from backend.llm.dataset import AIEthicsDataset
from backend.llm.train import train_model
from transformers import BertTokenizer

class LLMService:
    def __init__(self):
        self.model = None
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.principles = None

    def train(self, train_csv, val_csv):
        train_dataset = AIEthicsDataset(train_csv)
        val_dataset = AIEthicsDataset(val_csv)
        
        self.principles = train_dataset.principles
        num_labels = len(self.principles)
        
        self.model = train_model(train_dataset, val_dataset, num_labels)
        print("Model training completed.")

    def generate_assessment(self, input_text):
        if self.model is None:
            return "Model not trained. Please train the model first."

        self.model.eval()
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(device)

        # Tokenize input
        encoded_input = self.tokenizer.encode_plus(
            input_text,
            add_special_tokens=True,
            max_length=512,
            padding='max_length',
            truncation=True,
            return_attention_mask=True,
            return_tensors='pt'
        )

        input_ids = encoded_input['input_ids'].to(device)
        attention_mask = encoded_input['attention_mask'].to(device)

        with torch.no_grad():
            outputs = self.model(input_ids, attention_mask)
            _, predicted = torch.max(outputs, 1)

        predicted_principle = self.principles[predicted.item()]
        
        assessment = f"The input text is most closely associated with the ethical principle of {predicted_principle}."
        return assessment

    def get_assessment(self, assessment_id):
        # Placeholder for retrieving a stored LLM assessment
        # In the future, we'll implement database retrieval here
        return f"Retrieved LLM assessment placeholder for ID: {assessment_id}"

llm_service = LLMService()