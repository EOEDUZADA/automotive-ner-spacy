import spacy

try:
    nlp = spacy.load("output/model-best") 
    
    test_text = "O cliente solicitou a substituição do jogo de pastilha de freio da marca Bosch e uma troca de óleo completa por 480,00."
    doc = nlp(test_text)

    for ent in doc.ents:
        print(f"Texto: {ent.text:<30} | Categoria: {ent.label_}")
except OSError:
    print("Erro: Treine o modelo primeiro usando 'spacy train' para gerar a pasta 'output/'.")