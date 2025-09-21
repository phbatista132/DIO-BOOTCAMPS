import speech_recognition as sr
import pyttsx3
import wikipedia


def falar(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()


def ouvir():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ouvindo...")
        audio = recognizer.listen(source)
    try:
        texto = recognizer.recognize_google(audio, language='pt-BR')
        print(f"Você disse: {texto}")
        return texto
    except sr.UnknownValueError:
        print("Não entendi.")
        return ""
    except sr.RequestError:
        print("Erro na API.")
        return ""


def buscar_info(consulta):
    wikipedia.set_lang("pt")
    try:
        resumo = wikipedia.summary(consulta, sentences=2)
        return resumo
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Seja mais específico. Você quis dizer: {e.options[0]}?"
    except wikipedia.exceptions.PageError:
        return "Não encontrei nada sobre isso."


def iniciar_assistente():
    falar("Olá, Pablo! Como posso te ajudar hoje?")
    while True:
        comando = ouvir()
        if comando.lower() in ["sair", "encerrar", "tchau"]:
            falar("Até mais!")
            break
        elif comando:
            resposta = buscar_info(comando)
            print("Resposta:", resposta)
            falar(resposta)


iniciar_assistente()