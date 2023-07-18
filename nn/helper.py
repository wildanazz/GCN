import os
import uuid
import logging
import tempfile
from azure.storage.blob import BlobServiceClient

tempFilePath = tempfile.gettempdir()


def write_to_temp(data):
    logging.info('Storing file in a temporary directory...')

    try:
        with open(f"{tempFilePath}/data.npz", 'wb') as f:
            try:
                f.write(data.read())
            except:
                logging.error(
                    'Something went wrong when writing to temporary file.')
            finally:
                f.flush()
    except:
        logging.error('Something went wrong when opening temporary file.')


def upload_images():
    logging.info('Uploading file...')

    logging.info(os.environ["ConnectionString"])

    blob_service_client = BlobServiceClient.from_connection_string(
        os.environ["ConnectionString"])

    container_name = str(uuid.uuid4())

    list_url = {}
    for m in ["loss", "accuracy", "embeddings"]:
        blob_client = blob_service_client.get_blob_client(
            container=f"gcn/{container_name}", blob=f"{m}.png")

        with open(file=f"{tempFilePath}/{m}.png", mode="rb") as data:
            blob_client.upload_blob(data)
            list_url[m] = blob_client.url

    return list_url
