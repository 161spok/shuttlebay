# pip install --upgrade transformers huggingface_hub

from langchain.agents import load_huggingface_tool

tool = load_huggingface_tool("lysandre/hf-model-downloads")

print(f"{tool.name}: {tool.description}")

tool.run("text-classification")
