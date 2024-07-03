import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name='tweet'

list_of_file=[
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_training.py",
    f"{project_name}/components/text_tokenization.py",
    f"{project_name}/components/model_evalution.py",
    f"{project_name}/pipeline/training.py",
    f"{project_name}/pipeline/prediction.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/exception/__init__.py",
    "app.py",
    "demo.py",
    "setup.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore"

]


for filepath in list_of_file:
    filepath = Path(filepath)

    filedir, filename= os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating filedir: {filedir} for the filename:{filename}")


    if (not os.path.exists(filepath)) or (os.path.getsize(filepath==0)):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty  file {filepath}")

    else:
        logging.info(f"{filename} is already exists")      

