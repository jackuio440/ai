from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import OpenAI
from langchain_groq import ChatGroq
from langchain.agents import load_tools
from langchain.prompts import PromptTemplate
import os

os.environ["TAVILY_API_KEY"] = "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"
os.environ["LANGCHAIN_API_KEY"] = "sv2_pt_0b5e556536224e12b0b96559693a74aa_64d388f217"
os.environ["SERPER_API_KEY"] = 'bad5e8f36ebb8ce93c755ab8b11283ad8152a017'

#prompt = hub.pull("hwchase17/react")
template = '''Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action(don't need to show url)
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought:{agent_scratchpad}
(in this part don't need to print the url)
'''

prompt = PromptTemplate.from_template(template)
llm = ChatGroq(temperature=0, groq_api_key="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", model_name="mixtral-8x7b-32768")
tools = [TavilySearchResults(max_results=2)]
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
agent_executor.invoke({"input": "喜馬拉雅山多高?疊幾座喜馬拉雅山可以到月球"})
