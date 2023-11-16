import tflearn
import pickle
import random
import json
import tensorflow
import numpy
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

nltk.download('punkt')

with open('contenido.json', encoding='utf-8') as archivo:
    datos = json.load(archivo)

palabras = []
tags = []
auxX = []
auxY = []
for contenido in datos["contenido"]:
    for patrones in contenido["patrones"]:
        auxPalabra = nltk.word_tokenize(patrones)
        palabras.extend(auxPalabra)
        auxX.append(auxPalabra)
        auxY.append(contenido["tag"])
        if contenido["tag"] not in tags:
            tags.append(contenido["tag"])
palabras = [stemmer.stem(w.lower()) for w in palabras if w != "*"]
palabras = sorted(list(set(palabras)))
tags = sorted(tags)

entrenamiento = []
salida = []
salidaVacia = [0 for _ in range(len(tags))]
for x, documento in enumerate(auxX):
    cubeta = []
    auxPalabra = [stemmer.stem(w.lower())for w in documento]
    for w in palabras:
        if w in auxPalabra:
            cubeta.append(1)
        else:
            cubeta.append(0)
    filaSalida = salidaVacia[:]
    filaSalida[tags.index(auxY[x])] = 1
    entrenamiento.append(cubeta)
    salida.append(filaSalida)

entrenamiento = numpy.array(entrenamiento)
salida = numpy.array(salida)

tensorflow.compat.v1.reset_default_graph()
red = tflearn.input_data(shape=[None, len(entrenamiento[0])])
red = tflearn.fully_connected(red, 10)
red = tflearn.fully_connected(red, 10)
red = tflearn.fully_connected(red, 10)
red = tflearn.fully_connected(red, len(salida[0]), activation="softmax")
red = tflearn.regression(red)

modelo = tflearn.DNN(red)
modelo.fit(entrenamiento, salida, n_epoch=1000, batch_size=10, show_metric=True)
modelo.save("modelo.tflearn")

def mainBot(mensage):
    entrada = mensage
    cubeta = [0 for _ in range(len(palabras))]
    entradaProcesada = nltk.word_tokenize(entrada)
    entradaProcesada = [stemmer.stem(palabra.lower()) for palabra in entradaProcesada]
    for palabraIndividual in entradaProcesada:
        for i,palabra in enumerate(palabras):
            if palabra == palabraIndividual:
                cubeta[i] = 1

    resultados = modelo.predict([numpy.array(cubeta)])
    resultadosIndices = numpy.argmax(resultados)
    probabilidad_respuesta = resultados[0][resultadosIndices]  # Probabilidad de la respuesta seleccionada

    # Definir un umbral de probabilidad para activar la respuesta por defecto
    umbral_probabilidad = 0.0

    if probabilidad_respuesta < umbral_probabilidad:
        # La probabilidad de la respuesta es baja, se activa la respuesta por defecto
        for tagAux in datos["contenido"]:
            if tagAux["tag"] == "default":
                respuesta = tagAux["respuestas"]
    else:
        # La probabilidad es suficientemente alta, se selecciona la respuesta
        tag = tags[resultadosIndices]
        for tagAux in datos["contenido"]:
            if tagAux["tag"] == tag:
                respuesta = tagAux["respuestas"]
    
    return ("Agente virtual: ", random.choice(respuesta))