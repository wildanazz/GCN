import logging
import azure.functions as func

from .helper import write_to_temp
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
            logging.info('Job completed.')
        except:
            logging.error('Something went wrong when performing GCN.')

        return func.HttpResponse(f"{data.filename} received")
    else:
        return func.HttpResponse(
            "Please pass valid data in the request body",
            status_code=400
        )
