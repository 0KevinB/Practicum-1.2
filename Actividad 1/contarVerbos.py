# Importar los módulos necesarios
import stanza

# Definir el texto de ejemplo
text = "Ella ha estado cantando una canción hermosa todo el día y quiere aprender a tocar la guitarra."

# Inicializar el modelo de procesamiento de idioma español
nlp = stanza.Pipeline('es')

# Procesar el texto
doc = nlp(text)

# Contadores para cada tipo de verbo
contador_verbos = 0
contador_auxiliares = 0
contador_principales = 0
contador_tiempos = 0
contador_infinitivo = 0

# Recorrer cada oración en el documento
for sentence in doc.sentences:
    # Recorrer cada palabra en la oración
    for word in sentence.words:
        if word.upos == 'AUX':
            contador_auxiliares += 1
        elif word.upos == 'VERB':
            contador_verbos += 1
        if word.deprel == 'root':
            contador_principales += 1
        if word.feats != "Tense=Pres" and word.feats != 'VerbForm=Inf' and word.upos == 'VERB':
            contador_tiempos += 1
        if word.feats == 'VerbForm=Inf':
            contador_infinitivo += 1

# Imprimir los resultados
print("Verbos:", contador_verbos)
print("Auxiliares:", contador_auxiliares)
print("Principales:", contador_principales)
print("Otros tiempos:", contador_tiempos)
print("Infinitivo:", contador_infinitivo)
