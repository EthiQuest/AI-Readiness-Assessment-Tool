from transformers import BertTokenizer

class AIEthicsTokenizer:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

    def encode(self, text, max_length=512):
        return self.tokenizer.encode_plus(
            text,
            add_special_tokens=True,
            max_length=max_length,
            padding='max_length',
            truncation=True,
            return_tensors='pt'
        )

    def decode(self, token_ids):
        return self.tokenizer.decode(token_ids, skip_special_tokens=True)

    @property
    def vocab_size(self):
        return self.tokenizer.vocab_size

tokenizer = AIEthicsTokenizer()