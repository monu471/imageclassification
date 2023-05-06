from src.DogCat import logging
a = 2
b = 0 
try :
    c = a/0
except Exception as e :
    logging.info(e)
