import streamlit as st
import pandas as pd
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import nltk
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer

# Fonction pour nettoyer le texte
def clean_text(text):
    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub(f'[{string.punctuation}]', '', text)
    text = re.sub('\n', '', text)
    return text

# Fonction pour extraire le sujet principal de la phrase
def extract_subject(sentence):
    tokens = word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    subjects = [word for word, tag in tagged if tag.startswith('NN')]
    return subjects

# Fonction pour déterminer le sentiment de la phrase
def analyze_sentiment(sentence):
    sid = SentimentIntensityAnalyzer()
    sentiment_score = sid.polarity_scores(sentence)['compound']
    if sentiment_score > 0.05:
        return 'positive'
    elif sentiment_score < -0.05:
        return 'negative'
    else:
        return 'neutral'

# Chargement des données d'entraînement
train = pd.read_csv('tweet_train.csv')
train.dropna(inplace=True)
train['original_text'] = train['text'].copy()
train['original_selected_text'] = train['selected_text'].copy()
train['text'] = train['text'].apply(clean_text)
train['selected_text'] = train['selected_text'].apply(clean_text)

# Création de l'application Streamlit
def main():
    st.title("Analyse des Tweets")

    # Affichage des données d'entraînement
    st.subheader("Données d'entraînement")
    st.write(train)

    # Sélection d'un tweet aléatoire
    sample_tweet = st.selectbox("Sélectionner un tweet aléatoire", train['original_text'])

    # Affichage du tweet sélectionné
    st.subheader("Tweet sélectionné")
    st.write(sample_tweet)

    # Génération de commentaires
    st.subheader("Génération de commentaires")
    nbr_comment = st.number_input("Combien de commentaires générer?", min_value=1, max_value=10, value=1)

    if st.button("Générer les commentaires"):
        # Nettoyage du tweet sélectionné
        cleaned_tweet = clean_text(sample_tweet)

        # Génération des commentaires
        comments = generate_comments(cleaned_tweet, nbr_comment)

        # Affichage des commentaires générés
        for i, comment in enumerate(comments):
            st.write(f"{i+1}. {comment}")

# Fonction pour générer des commentaires
def generate_comments(tweet, num_comments):
    torch.random.manual_seed(0)

    model = AutoModelForCausalLM.from_pretrained(
        "microsoft/Phi-3-mini-4k-instruct",
        device_map="cpu",
        torch_dtype="auto",
        trust_remote_code=True,
    )
    tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-4k-instruct")

    messages = [
        {"role": "system", "content": f"Generate {num_comments} distinct and independent Twitter comments representing {num_comments} user reactions. Each comment should reflect the viewpoint of the tweet in question, adapt to the written language, stay within the 280-character limit, and appear realistic for a Twitter comment."},
        {"role": "user", "content": tweet},
    ]

    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
    )

    generation_args = {
        "max_new_tokens": 500,
        "return_full_text": False,
        "temperature": 0.0,
        "do_sample": False,
    }

    output = pipe(messages, **generation_args)

    comments = []
    for i in range(num_comments):
        comment_text = output[0]['generated_text'].split('\n')[i]
        comments.append(comment_text)

    return comments

if __name__ == "__main__":
    main()
