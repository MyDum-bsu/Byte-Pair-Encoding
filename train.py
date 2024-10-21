import os
import time
from bpe.basic import BasicTokenizer

# open some text and train a vocab of 512 tokens
text = open("test/TitansOfCreation.txt", "r", encoding="utf-8").read()

os.makedirs("models", exist_ok=True)

t0 = time.time()

# construct the Tokenizer object and kick off verbose training
tokenizer = BasicTokenizer()
tokenizer.train(text, 512, verbose=True)
t1 = time.time()
# prefix = os.path.join("models", "basic")
# TODO: tokenizer.save(prefix)
print(f"Training took {t1 - t0:.2f} seconds")