from langchain.agents import create_csv_agent, create_pandas_dataframe_agent
from langchain.chat_models import ChatOpenAI
import pandas as pd
from langchain.agents.agent_types import AgentType

########################################################################################################################
df = pd.read_csv("../DataSet/llm_sample_dataset.csv")
########################################################################################################################

agent1 = create_pandas_dataframe_agent(
    ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613",
               openai_api_key="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"),
    df,
    verbose=True,
    agent_type=AgentType.OPENAI_FUNCTIONS,
)

########################################################################################################################

agent2 = create_csv_agent(
    ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613",
               openai_api_key="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"),
    "../DataSet/llm_sample_dataset.csv",
    verbose=True,
    agent_type=AgentType.OPENAI_FUNCTIONS,
)

########################################################################################################################

agent1.run("What is the maximum value of the cibil score of applicants with Personal loan")
agent2.run("What is the maximum value of the cibil score of applicants with Personal loan")
