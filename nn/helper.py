import logging
import tempfile


def write_to_temp(data):
    logging.info('Storing file in a temporary directory...')

    tempFilePath = tempfile.gettempdir()

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
