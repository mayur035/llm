from dotenv import load_dotenv;
import os;
from langchain_core.prompts import PromptTemplate;
from langchain_core.output_parsers import StrOutputParser;
from langchain_groq import ChatGroq;
from third_parties.linkedIn import scrape_linkedin_profile;
 
load_dotenv()

if __name__ == '__main__':
    print('hello')
    api_key = os.environ['API_GROQ_TEST']
    summary_template = """
        given the linkedIn information {information} about a person from I want you to create:
        1. a short summary 
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"],template=summary_template)
    llm  =  ChatGroq(temperature=0,model="llama-3.3-70b-versatile",api_key=api_key)
    chain = summary_prompt_template | llm | StrOutputParser()
    linkedin_scrape = scrape_linkedin_profile("https://gist.githubusercontent.com/emarco177/859ec7d786b45d8e3e3f688c6c9139d8/raw/5eaf8e46dc29a98612c8fe0c774123a7a2ac4575/eden-marco-scrapin.json")
    res= chain.invoke(input={"information":linkedin_scrape})
    print(res)