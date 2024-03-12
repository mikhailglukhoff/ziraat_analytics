import os
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
from constants import ziraat_ai_data


openai_api_key = os.environ[ziraat_ai_data['secret_key']]

llm = OpenAI(api_token=openai_api_key)

pandas_ai = PandasAI(llm)