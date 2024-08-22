from google.colab import files
uploaded = files.upload()

import fitz  # PyMuPDF

# É necessario selecionar exatamente o texto que voce mencionou no codigo

def pdf_to_text(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)
    for page in doc:
        text += page.get_text()
    return text

# Insira o nome do arquivo PDF que você carregou

pdf_path = 'Davi.pdf'  # Substituir pelo nome do seu arquivo (Se não, não funciona)
texto_extraido = pdf_to_text(pdf_path)

# Salvando o texto em um arquivo .txt
with open("texto_extraido.txt", "w", encoding="utf-8") as f:
    f.write(texto_extraido)

# Para baixar o arquivo .txt gerado
files.download("texto_extraido.txt")

