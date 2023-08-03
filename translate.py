from textblob import TextBlob
# pip install textblob
# python -m textblob.download_corpora


def translate_(text_to_translate, from_lag, to_lag):
    blob = TextBlob(text_to_translate)
    return blob.translate(from_lang=from_lag, to=to_lag)
