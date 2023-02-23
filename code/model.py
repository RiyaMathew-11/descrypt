from sentence_transformers import SentenceTransformer
import pickle
model = SentenceTransformer('bert-base-nli-mean-tokens')
pickle.dump(model, open('model.pkl', 'wb'))

