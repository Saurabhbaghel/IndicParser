from fastapi import FastAPI, Query, Path, File, UploadFile
from enum import Enum
from use_doctr import doctr

class model_name(str, Enum):
    pytesseract = 'Pytesseract'
    doctr = 'DocTR'
    none = None



app = FastAPI()


@app.post('/OCR')
async def choose_model(model: model_name, File: UploadFile):
    if model == model_name.pytesseract:
        return f"You've selected {model} for OCR. Please upload the .jpg, .jpeg or .png file."
    elif model == model_name.doctr:
        FILE = doctr(File)
        return FILE.ocr()
        # return f"You've selected {model} for OCR. Please upload the .jpg, .jpeg or .png or .pdf file."

    else:
        return f"Please select a model to OCR the image."

# @app.get('/OCR/file')
# async def upload(file_name: str = Query(
#     regex=".+(.jpg)|.+(.jpeg)|.+(.png)",
#     alias='Upload Image',
#
# )):
# # @app.get('/OCR/file')
# # async def upload(file_name: str = Path("The path of the file.")):
#     return file_name
