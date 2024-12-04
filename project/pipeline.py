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
    link = "https://storage.googleapis.com/kaggle-data-sets/4435273/7615817/bundle/archive.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20241204%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20241204T165640Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=558f22c136d99948fca0f5d214524c941ebad06c788f4561c7c4711e4e0bad9146c3024326f7a0a3bea607c0f04fd571c6a5f46e04996028447a01764bb78044eab8f1419306269223edf2e45c38d816993d6327f816dd6fc9cc0ac624eeb49d45f6c68082192012a2e4302169fc7ce143bfddefd6c234f2483fa22cd67cb537a3271b4cb2cb0ee69351d0063e2e3cfd252550163467bf5e47c2d6f5b719d91c89cdeff94624d2cde704c3744795fa13a55d51341e951f102fe39444f26deb5fd9f0cf1af5bea22e06092b4e1a94021e409b4bf3e480906bb0fd15529964b97ae1fa449d3ab067d8f988a9b7f2c7f1f7267a1c25db33726953fe33663efbc48e"
    dataframe = download_data(link)
    create_dataset(dataframe)