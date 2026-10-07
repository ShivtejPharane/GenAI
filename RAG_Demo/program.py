from langchain_community.document_loaders import TextLoader, PyPDFLoader

def load_text_file(file_name: str):
    # Create the loader 
    loader = TextLoader(file_path=file_name)

    # Load the text Data
    data = loader.load()

    print(data)

def load_pdf_file(file_name:str):
    loader = PyPDFLoader(file_path=file_name)
    data = loader.load()
    print(data)
load_text_file("./data/sample_data.txt")
load_pdf_file("./data/sample_data.pdf")