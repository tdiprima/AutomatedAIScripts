# Data extraction
from ollama import chat
from pydantic import BaseModel

class Pet(BaseModel):
  name: str
  animal: str
  age: int
  color: str
  favorite_toy: str

class PetList(BaseModel):
  pets: list[Pet]

response = chat(
  messages=[
    {
      'role': 'user',
      'content': '''
        I have two pets.
        A cat named Luna who is 5 years old and loves playing with yarn. She has grey fur.
        I also have a 2 year old black cat named Loki who loves tennis balls.
      ''',
    }
  ],
  model='llama3.2',
  format=PetList.model_json_schema(),
)

# pets = PetList.model_validate_json(response.message.content)
pets = PetList.model_validate_json(response["message"]["content"])
print(pets)
