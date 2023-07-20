import pandas as pd
import stanza

ra1 = "Elige y evalúa los factores influyentes que permitan definir de forma apropiada la organización física requerida para un implementar una base de datos"
ra2 = "Propone soluciones innovadoras a problemas en la sociedad sistemáticos y metodológicos del pensamiento de diseño."
ra3 = "Aplica la metodología del pensamiento de diseño para identificar problemas locales relacionados a la ingeniería en computación."
ra4 = "Diseña prototipos aplicando técnicas y herramientas de prototipado rápido de Ingeniería en Computación para crear soluciones innovadoras"
ra5 = "Diseña prototipos aplicando técnicas y herramientas de prototipado rápido de Ingeniería en Computación para crear soluciones innovadoras"

# Inicializar el modelo de procesamiento de idioma español
nlp = stanza.Pipeline('es')

# Textos de ejemplo
textos = [ra1, ra2, ra3, ra4, ra5]

# Lista para almacenar los resultados
resultados_vertical = []
resultados_horizontal = []

# Procesar cada texto en la lista
for i, texto in enumerate(textos, start=1):
    # Procesar el texto
    doc = nlp(texto)

    # Para almacenar palabras por categorías
    palabras_por_categoria = {
        'PRON': [], 'NOUN': [], 'ADJ': [], 'VERB': [], 'ADV': [], 
        'AUX': [], 'ADP': [], 'PUNCT': [], 'DET': [], 'CCONJ': []
    }

    # Recorrer cada oración en el documento
    for sentence in doc.sentences:
        # Recorrer cada palabra en la oración
        for word in sentence.words:
            # Agregar a la tabla vertical
            resultados_vertical.append([
                f"RA{i}",
                word.text,
                word.lemma,
                word.upos,
                word.xpos if word.xpos is not None else 'N/A'
            ])

            # Agregar a la tabla horizontal
            if word.upos in palabras_por_categoria:
                palabras_por_categoria[word.upos].append(word.text)

    # Guardar los resultados en una lista
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

# Crear DataFrames a partir de los resultados
df_vertical = pd.DataFrame(resultados_vertical, columns=['RA', 'Token', 'Lemma', 'POS (UD)', 'POS (EAGLES)'])
df_horizontal = pd.DataFrame(resultados_horizontal, columns=['RA', 'Pronombres', 'Sustantivos', 'Adjetivos', 'Verbos', 'Adverbios',
                                                             'Auxiliares', 'Adposiciones', 'Puntuacion', 'Determinantes', 'Conjunciones'])

# Crear un escritor de Excel
writer = pd.ExcelWriter('salida.xlsx', engine='xlsxwriter')

# Escribir DataFrames a Excel en la misma hoja pero separadas por algunas celdas
df_horizontal.to_excel(writer, sheet_name='Sheet1', index=False)
df_vertical.to_excel(writer, sheet_name='Sheet1', index=False, startrow=len(df_horizontal) + 3)

# Guardar el archivo de Excel
writer._save()
