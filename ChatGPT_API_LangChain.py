from langchain_openai import OpenAI
#from dotenv import load_dotenv

#load_dotenv()

def generate_pet_name():
    llm =OpenAI(temperature=0.7, openai_api_key="")
    print(llm)

    name = llm("I have a dog pet and I want a cool name for it. Suggest me five cool names foe my pet.")
    print(name)

#generate_pet_name()

#if __name__ == "__main__":
#    print(generate_pet_name())

llm =OpenAI(temperature=0.7, openai_api_key="")
print(llm)

name = llm("I have a dog pet and I want a cool name for it. Suggest me five cool names for my pet.")
print(name)