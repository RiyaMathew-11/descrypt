
from flask import Flask, render_template, request
import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


final_score = 0
i = 0
data = pd.read_csv('data/data_draft.csv')
model = pickle.load(open('model.pkl', 'rb'))


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/get")
def get_bot_response():
    global i
    global final_score
    userText = request.args.get('msg')

    if userText == 'stop':
        return f"Your final score is {str(round(final_score,2))}"

    if userText == 'start':
        return data.Question[i]

    elif userText == 'next':
        i += 1
        return data.Question[i]

    else:
        model_answer, user_answer = data.Model_Answer[i], userText
        model_answer_embedding = model.encode(model_answer)
        user_answer_embedding = model.encode(user_answer)
        score = cosine_similarity(
            model_answer_embedding.reshape(1, -1), user_answer_embedding.reshape(1, -1))[0][0]

        if score >= 0.9:
            user_score = 2
        elif 0.9 > score >= 0.6:
            user_score = score * 2
        else:
            user_score = 0
        final_score += user_score

        return f"Your score is {str(round(score,2))}"


if __name__ == "__main__":
    app.run(port=6030)
