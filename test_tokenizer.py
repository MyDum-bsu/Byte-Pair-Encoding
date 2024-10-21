import os
import pytest
from bpe.basic import BasicTokenizer

test_strings = [
    "",
    "?",
    "hello world!!!? (안녕하세요!) lol123 😉",
    "FILE:test/TitansOfCreation.txt",
]

def unpack(text):
    if text.startswith("FILE:"):
        dirname = os.path.dirname(os.path.abspath(__file__))
        taylorswift_file = os.path.join(dirname, text[5:])
        contents = open(taylorswift_file, "r", encoding="utf-8").read()
        return contents
    else:
        return text

@pytest.mark.parametrize("tokenizer_factory", [BasicTokenizer])
@pytest.mark.parametrize("text", test_strings)
def test_encode_decode_identity(tokenizer_factory, text):
    text = unpack(text)
    tokenizer = tokenizer_factory()
    ids = tokenizer.encode(text)
    decoded = tokenizer.decode(ids)
    assert text == decoded

if __name__ == "__main__":
    pytest.main()