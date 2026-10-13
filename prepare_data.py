import json
import spacy
from spacy.tokens import DocBin
from sklearn.model_selection import train_test_split


with open("label_studio_export.json", "r", encoding="utf-8") as f:
    label_studio_data = json.load(f)

nlp = spacy.blank("pt")
converted_docs = []

# Converte Label Studio -> spaCy
for item in label_studio_data:
    text = item["text"]
    doc = nlp.make_doc(text)
    entities = []
    for start, end, label in item["entities"]:
        span = doc.char_span(start, end, label=label, alignment_mode="contract")
        if span is not None: 
            entities.append(span)
    try:
        doc.ents = spacy.util.filter_spans(entities)
        converted_docs.append(doc)
    except Exception: 
        pass

# 80% treino e 20% validação
train_docs, valid_docs = train_test_split(converted_docs, test_size=0.2, random_state=42)

# Exporta os arquivos binários do spaCy (.spacy)
def save_docbin(docs, filepath):
    db = DocBin()
    for doc in docs: 
        db.add(doc)
    db.to_disk(filepath)

save_docbin(train_docs, "train.spacy")
save_docbin(valid_docs, "valid.spacy")

print("Pronto para iniciar treinamento")