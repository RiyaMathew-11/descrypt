from sentence_transformers import SentenceTransformer
import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv('data/data_draft.csv')

bert_model = pickle.load(open('model.pkl', 'rb'))

output_file = open("data/output.txt", "a")
output_file.write("Question,Model_Answer,User_Answer,Score")


for i in range(len(data)):
    print(data.Question[i])
    model_answer = bert_model.encode(data.Model_Answer[i])
    print("Model answer: ",data.Model_Answer[i])

    user_input = data.User_Answer[i]
    print("User Answer: ", data.Model_Answer[i])

    user_answer_embedding = bert_model.encode(user_input)
    score = cosine_similarity(
        model_answer.reshape(1, -1), user_answer_embedding.reshape(1, -1))[0][0]

    print("\n\nSimilarity score by Cosine: ", score)

    output_file.write(f"\n'{data.Question[i]}','{data.Model_Answer[i]}','{data.User_Answer[i]}',{score}")







