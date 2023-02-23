from sentence_transformers import SentenceTransformer
from data.utils import stopwords
import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import jaccard_score

data = pd.read_csv('data/data_draft.csv')
bert_model = pickle.load(open('model.pkl', 'rb'))


def preprocess(text1, text2):
    text_tokens1 = text1.split()
    text_tokens2 = text2.split()

    remove_sw1 = [word for word in text_tokens1 if not word in stopwords]
    remove_sw2 = [word for word in text_tokens2 if not word in stopwords]

    finaltext1 = ' '.join(remove_sw1)
    finaltext2 = ' '.join(remove_sw2)
    return finaltext1, finaltext2


for i in range(5):
    print(data.Question[i])
    user_input = input('Enter your answer: ')

    model_answer, user_answer = preprocess(data.Model_Answer[i], user_input)

    model_answer_embedding = bert_model.encode(model_answer)
    user_answer_embedding = bert_model.encode(user_answer)
    score = jaccard_score(
        model_answer_embedding, user_answer_embedding.reshape)

    print("\n\nSimilarity score by Jaccard: ", round(score, 2))

    print("----------------------------------------------------")
