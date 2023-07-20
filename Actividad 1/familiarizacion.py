# Importar el módulo 'stanza'
import stanza

# Descargar los recursos necesarios para procesar texto en español
stanza.download('es')

# Definir el texto de entrada
text = "Propone soluciones innovadoras a problemas en la sociedad sistemáticos y metodológicos del pensamiento de diseño."

# Crear un objeto de la clase 'Pipeline' para procesar texto en español
nlp = stanza.Pipeline('es')

# Procesar el texto con el modelo lingüístico
doc = nlp(text)

# Imprimir el JSON completo generado por el procesamiento del texto
print(doc)
