import stanza

# Descargar los recursos necesarios para procesar texto en español
stanza.download('es')

# Inicializar el modelo de procesamiento de idioma español
nlp = stanza.Pipeline('es')

# Definir el texto de entrada
text = "Ella ha estado cantando una canción hermosa todo el día y quiere aprender a tocar la guitarra."

# Procesar el texto con el modelo lingüístico
doc = nlp(text)

# Recorrer cada oración en el documento
for sent in doc.sentences:
    # Recorrer cada palabra en la oración
    for word in sent.words:
        # Obtener información de la palabra
        token = word.text  # Token original
        lemma = word.lemma  # Forma base (lema) de la palabra
        pos_ud = word.upos  # Etiqueta (UD)
        pos_eagles = word.xpos  # Etiqueta (EAGLES)

        # Imprimir la información de la palabra
        print(f"Token: {token}\tLemma: {lemma}\tPOS (UD): {pos_ud}\tPOS (EAGLES): {pos_eagles}")
