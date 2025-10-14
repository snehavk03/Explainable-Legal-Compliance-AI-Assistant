from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
class ClauseClassifier:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("law-ai/InLegalBERT")
        self.model = AutoModelForSequenceClassification.from_pretrained("law-ai/InLegalBERT")
    def classify_clause(self,text):
        inputs=self.tokenizer(text,return_tensors="pt",truncation=True)
        outputs=self.model(**inputs)
        return torch.argmax(outputs.logits,dim=1).item()
if __name__=="__main__":
    print(ClauseClassifier().classify_clause("This agreement may be terminated..."))