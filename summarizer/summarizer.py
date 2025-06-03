import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.stem import WordNetLemmatizer
import heapq

class TextSummarizer:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.download('wordnet')
        self.stop_words = set(stopwords.words("english"))
        self.lemmatizer = WordNetLemmatizer()

    def preprocess_text(self, text):
        # Tokenize sentences
        sentences = sent_tokenize(text)
        
        # Tokenize words and remove stopwords
        word_tokens = word_tokenize(text.lower())
        filtered_words = [self.lemmatizer.lemmatize(word) for word in word_tokens 
                         if word.isalnum() and word not in self.stop_words]
        
        return sentences, filtered_words

    def generate_summary(self, text, num_sentences=3):
        sentences, filtered_words = self.preprocess_text(text)
        
        # Calculate word frequencies
        word_frequencies = FreqDist(filtered_words)
        
        # Calculate sentence scores based on word frequencies
        sentence_scores = {}
        for sentence in sentences:
            for word in word_tokenize(sentence.lower()):
                if word in word_frequencies:
                    if sentence not in sentence_scores:
                        sentence_scores[sentence] = word_frequencies[word]
                    else:
                        sentence_scores[sentence] += word_frequencies[word]
        
        # Get top N sentences with highest scores
        summary_sentences = heapq.nlargest(num_sentences, 
                                          sentence_scores, 
                                          key=sentence_scores.get)
        
        # Return summary as a single string
        return " ".join(summary_sentences)
