import pandas as pd
import stanza
from typing import List

def process_text(textos: List[str]):
    # Inicializar el modelo de procesamiento de idioma español
    nlp = stanza.Pipeline('es')
    resultados_vertical = []
    resultados_horizontal = []

    # Procesar cada texto en la lista
    for i, texto in enumerate(textos, start=1):
        # Procesar el texto con el modelo lingüístico
        doc = nlp(texto)
        palabras_por_categoria = {
            'PRON': [], 'NOUN': [], 'ADJ': [], 'VERB': [], 'ADV': [],
            'AUX': [], 'ADP': [], 'PUNCT': [], 'DET': [], 'CCONJ': []
        }

        # Recorrer cada oración en el documento
        for sentence in doc.sentences:
            # Recorrer cada palabra en la oración
            for word in sentence.words:
                # Guardar los resultados en una lista vertical
                resultados_vertical.append([
                    f"RA{i}",
                    word.text,
                    word.lemma,
                    word.upos,
                    word.xpos if word.xpos is not None else 'N/A'
                ])

                # Contar palabras por categoría gramatical
                if word.upos in palabras_por_categoria:
                    palabras_por_categoria[word.upos].append(word.text)

        # Guardar los resultados en una lista horizontal
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

    # Crear DataFrames con los resultados
    df_vertical = pd.DataFrame(resultados_vertical, columns=['RA', 'Token', 'Lemma', 'POS (UD)', 'POS (EAGLES)'])
    df_horizontal = pd.DataFrame(resultados_horizontal, columns=['RA', 'Pronombres', 'Sustantivos', 'Adjetivos', 'Verbos', 'Adverbios',
                                                                 'Auxiliares', 'Adposiciones', 'Puntuacion', 'Determinantes', 'Conjunciones'])

    # Devolver los resultados en forma de diccionario
    return {"Analisis de texto": df_horizontal.to_dict('records'), "Eagles": df_vertical.to_dict('records')}
