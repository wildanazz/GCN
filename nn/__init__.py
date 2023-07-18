import logging
import json
import azure.functions as func

from .helper import write_to_temp, upload_images
from .driver import main as gcn
from .plot import plot


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    data = req.files['data']

    if data:
        write_to_temp(data)
        try:
            gcn()
            plot()
            list_url = upload_images()
            logging.info('Jobs completed.')
        except:
            logging.error('Something went wrong when performing GCN.')

        return func.HttpResponse(json.dumps(list_url))
    else:
        return func.HttpResponse(
            "Please pass valid data in the request body",
            status_code=400
        )
