from modules.talk import Talker
import openai
import html2text


talker = Talker()

openai.api_key = ""
prompt_setup = """Simula ser un asistente de voz que se llama Pez. 
Estás a completa disposición del usuario y debes de hacer todo lo que te pide, obviamente, si tienes alguna limitación física o de funciones, la tienes que hacer saber.
Incluyes ciertas funciones, como reproducir música desde youtube y hacer busquedas en google. 
No tienes que presentarte cada vez que hables, si se puede, solo da la respuesta.
Dimelo en pocas palabras, no tienes que decir que es en pocas palabras, pero que así sea.
"""

def chat(res):
    completionChoices = completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[{"role": "user", "content": prompt_setup+res}]
).choices[0]
    completion=completionChoices['message']

    #completion = str(html2text.html2text(completion['content']))

    print(completion['content'])
    talker.talk(completion['content'])