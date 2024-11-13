import pandas as pd
import zipfile
import httpx
from io import BytesIO
from sqlalchemy import create_engine

def download_data(link):
    web_value = httpx.get(link)
    if(web_value.status_code == 200):
        with zipfile.ZipFile(BytesIO(web_value.content)) as zip:
            with zip.open(zip.namelist()[0]) as csv:
                df = pd.read_csv(csv)
                return df
        
    return None

def create_dataset(dataframe):
    writer = create_engine("sqlite:///./data/resturnent.sqlite")
    dataframe.to_sql('resturent', con = writer, index = False)


if __name__ == '__main__':
    link = "https://storage.googleapis.com/kaggle-data-sets/4435273/7615817/bundle/archive.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20241113%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20241113T153923Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=881e76b875b6b3a38c8fcc54c3fc095adaceef1cb512ccea8059be209b8016d5438d4f82ac63759bcfbe4fed63f4a0c4e835461491aef5900a90abea0b5020442a1e353188274ebb08f476e7b1a1ae42101d0f93972664fe6dc419dddf1662fd0e9231e3d3e950a16da5c296b00ac2ad75ed47ea1657675a4f31d8db266f1452cf0bf9c2c1b0b978a57a823be5b5bc9824528b9780f64ff62aeac65f21a6132f8974252453dc6d14cc780fcc67657a87ec2ccca18b337078220fd55365d43ff8fa3a3f0832056f8295bba30ac15234321cb467f27d05fa0b622584b6fe0b221e9cea36ae0feae2cce6975fe8357dcd82e3af3647644e42c2628fea4af7467260"
    dataframe = download_data(link)
    create_dataset(dataframe)