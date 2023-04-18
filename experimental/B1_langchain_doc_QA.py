# %%
# from langchain.document_loaders import TextLoader
# loader = TextLoader('../state_of_the_union.txt')
from langchain.document_loaders import DirectoryLoader
# %%
loader = DirectoryLoader('../text', glob="**/*.txt")
# %%
docs = loader.load()
print("Len docs: ", len(docs))
# %%
from langchain.indexes import VectorstoreIndexCreator
# %%
index = VectorstoreIndexCreator().from_loaders([loader])
# %%
query = "What model did Anderstoan and Armstrong propose?"
index.query_with_sources(query)
# %%
query = "What were the three generators used in the experiment?"
index.query_with_sources(query)

# %%
