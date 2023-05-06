import os,sys,logging
log_dir = "log"
logging_format = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_file_path = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(level = logging.INFO,format = logging_format,
                    handlers=[logging.FileHandler(log_file_path),logging.StreamHandler(sys.stdout)]
                    )
logger = logging.getLogger("DogCatlogger")