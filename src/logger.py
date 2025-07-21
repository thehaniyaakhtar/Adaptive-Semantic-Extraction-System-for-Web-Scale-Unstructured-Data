#creates a .log for every run
#saves it in /logs folder
#import modules
import logging
import os
from datetime import datetime

#ensuring each run gets its own log file
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

#creating log folder path
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok = True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

#configure the logger
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    #       timestamp         line number, mod name;  INFO, WARNING, ERROR; custom message 
    level=logging.INFO,
    #logs INFO and above
)

if __name__ == "__main__":
    logging.info("Logging has started.")