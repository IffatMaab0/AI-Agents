## Modifying Agent Using Langchain

import os
from dotenv import load_dotenv
import requests
from langchain_core.tools import tool
from langchain.agents import initialize_agent, AgentType