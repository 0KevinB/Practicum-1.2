import pandas as pd
import stanza
from typing import List

def process_text(textos: List[str]):
    nlp = stanza.Pipeline('es')
    resultados_vertical = []
    resultados_horizontal = []

    for i, texto in enumerate(textos, start=1):
        doc = nlp(texto)
        palabras_por_categoria = {
            'PRON': [], 'NOUN': [], 'ADJ': [], 'VERB': [], 'ADV': [], 
            'AUX': [], 'ADP': [], 'PUNCT': [], 'DET': [], 'CCONJ': []
        }

        for sentence in doc.sentences:
            for word in sentence.words:
                resultados_vertical.append([
                    f"RA{i}",
                    word.text,
                    word.lemma,
                    word.upos,
                    word.xpos if word.xpos is not None else 'N/A'
                ])

                if word.upos in palabras_por_categoria:
                    palabras_por_categoria[word.upos].append(word.text)

        resultados_horizontal.append([
            f"RA{i}",
            ', '.join(palabras_por_categoria['PRON']),
            ', '.join(palabras_por_categoria['NOUN']),
            ', '.join(palabras_por_categoria['ADJ']),
            ', '.join(palabras_por_categoria['VERB']),
            ', '.join(palabras_por_categoria['ADV']),
            ', '.join(palabras_por_categoria['AUX']),
            ', '.join(palabras_por_categoria['ADP']),
            ', '.join(palabras_por_categoria['PUNCT']),
            ', '.join(palabras_por_categoria['DET']),
            ', '.join(palabras_por_categoria['CCONJ'])
        ])

    df_vertical = pd.DataFrame(resultados_vertical, columns=['RA', 'Token', 'Lemma', 'POS (UD)', 'POS (EAGLES)'])
    df_horizontal = pd.DataFrame(resultados_horizontal, columns=['RA', 'Pronombres', 'Sustantivos', 'Adjetivos', 'Verbos', 'Adverbios',
                                                                 'Auxiliares', 'Adposiciones', 'Puntuacion', 'Determinantes', 'Conjunciones'])

    return {"Analisis de texto": df_horizontal.to_dict('records'), "Eaggles": df_vertical.to_dict('records')}
