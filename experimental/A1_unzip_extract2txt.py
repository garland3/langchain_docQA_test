# find the .zip file in /documents and unzip
# %%
from pathlib import Path
import zipfile

documents = Path("../documents")
print(f"Documents: {documents} exists {documents.exists()}")
# %%
myzipfiles =list( documents.glob("*.*"))
print(myzipfiles)
# %%
for myzipfile in myzipfiles:
    with zipfile.ZipFile(myzipfile) as myzip:
        myzip.extractall(documents)
# %%

# convert pdfs to txt save in dir text
textfolder = Path("../text")
textfolder.mkdir(exist_ok=True)
# %%
pdffiles = list(documents.glob("*.pdf"))
print("Num Found pdf files: ", len(pdffiles))
# %%
from unstructured.partition.auto import partition
# %%

# single_file = pdffiles[0]
for single_file in pdffiles:
    elements = partition(single_file)
    pdftext = "\n".join([e.text for e in elements])
    # save the text
    filename = textfolder / (single_file.stem + ".txt")
    open(filename, "w").write(pdftext)

# %%
