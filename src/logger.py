import os
import logging

from datetime import datetime

#log file naming convention
#day_month_year_hour_minute_seconds
LOG_FILE=f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"

#log path
#os.path.join(folder,sub-folder,file)
log_path = os.path.join(os.getcwd(),  "Logs", LOG_FILE)
#create directory to path, ignore if it already exists
os.makedirs(log_path,exist_ok=True)
#combine paths
LOG_FILE_PATH = os.path.join(log_path,LOG_FILE)

#overide functionality of imported logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",level=logging.INFO,
)
