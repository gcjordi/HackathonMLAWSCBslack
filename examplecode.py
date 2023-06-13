pip install requests Pillow transformers

import requests
from PIL import Image

image = Image.open(requests.get('https://fakeface.rest/face/', stream=True).raw) # API No funcional, meramente demostrativa 

from transformers import Tool

class FaceImageFetcher(Tool):
    pass
  
from transformers import Tool
from huggingface_hub import list_models

class FaceImageFetcher(Tool):
    name = "face_fetcher"
    description = ("Esta es una herramienta que obtiene una imagen real de un rostro con determinados patrones de una enfermedad mental concreta")
    inputs = []
    outputs = ["image"]

    def __call__(self):
        return Image.open(requests.get('https://fakeface.rest/face/', stream=True).raw).resize((256, 256))
      
tool = FaceImageFetcher()
tool()

from transformers.tools import HfAgent

agent = HfAgent("https://api-inference.huggingface.co/models/bigcode/starcoder", additional_tools=[tool])

agent.run("Busca una imagen de un rostro de una persona con rasgos de Síndrome de Down en línea y ponle un título")

# Nota: Código con base de inspiración (https://tinyurl.com/2xuf4fpy) y no operativo
