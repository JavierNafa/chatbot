from nltk.stem import WordNetLemmatizer
from nltk import sent_tokenize,download

# download('punkt')
# download('wordnet')
# download()

def generate_response(raw_text:str,user_input:str):
    sentences = sent_tokenize(raw_text)
    if len(sentences) == 0:
        return "I'm sorry I can't find anything :("
    if 'wikipedia' in sentences:
        sentences.remove('wikipedia')
    response = ''.join(sentences)[11:]
    return response

