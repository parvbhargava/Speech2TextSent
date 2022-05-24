from s2t import get_large_audio_transcription
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

path = "include/male.wav"
get_large_audio_transcription(path)

# Sentiment Analysis
Sentence = [str(text)]
analyser = SentimentIntensityAnalyzer()
for i in Sentence:
    v = analyser.polarity_scores(i)
    print(v)
