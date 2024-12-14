from src.app.interfaces.SentimentModelInterface import SentimentModelInterface
from src.domain.entities.Sentiment import SentimentAnalysis
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from typing import List
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class BERTSentimentModel(SentimentModelInterface):
    def __init__(self, model_name: str = 'nlptown/bert-base-multilingual-uncased-sentiment'):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(f"Using device: {self.device}")
        
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            self.model = AutoModelForSequenceClassification.from_pretrained(
                model_name,
                num_labels=5,
                ignore_mismatched_sizes=True
            ).to(self.device)
            print("Model loaded successfully")
        except Exception as e:
            print(f"Error loading model: {str(e)}")
            raise

        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.download('wordnet')

        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('portuguese'))

    def map_score_to_sentiment(self, score: int) -> tuple[str, float]:
        if score <= 2:
            sentiment = 'Negativo'
            confidence = 1 - (score - 1) * 0.3
        elif score >= 4:
            sentiment = 'Positivo'
            confidence = 0.4 + (score - 3) * 0.3
        else:
            sentiment = 'Neutro'
            confidence = 0.5

        return sentiment, confidence
    
    def predict(self, text: str) -> SentimentAnalysis:
        try:
            encoding = self.tokenizer.encode_plus(
                text,
                add_special_tokens=True,
                max_length=512,
                padding='max_length',
                truncation=True,
                return_attention_mask=True,
                return_tensors='pt'
            )
            
            input_ids = encoding['input_ids'].to(self.device)
            attention_mask = encoding['attention_mask'].to(self.device)
            
            with torch.no_grad():
                outputs = self.model(
                    input_ids=input_ids,
                    attention_mask=attention_mask
                )
                probabilities = torch.softmax(outputs.logits, dim=1)
                prediction = torch.argmax(probabilities, dim=1)
                score = prediction.item() + 1 
                
                sentiment, confidence = self.map_score_to_sentiment(score)
            
            return SentimentAnalysis(
                text=text,
                sentiment=sentiment,
                confidence=confidence
            )
        except Exception as e:
            print(f"Error in prediction: {str(e)}")
            raise

    def predict_batch(self, texts: List[str]) -> List[SentimentAnalysis]:
        return [self.predict(text) for text in texts]
