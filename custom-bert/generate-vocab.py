from tokenizers import BertWordPieceTokenizer
tokenizer = BertWordPieceTokenizer()

texts = ["Hi, I am Riya Mathew", "I love C programming!", "BERT is a transformer-based model."]

tokenizer.train_from_iterator(texts)

tokenizer.save_model("vocab", "sample")
