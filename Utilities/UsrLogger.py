import logging
from Utilities.comUtilities import commonUtilities as cu

class stockLogger():
    def __init__(self, module):
        super().__init__(self)
        conf = cu("./config.ini")
        logLevel = conf.get_property( "LOG", "loglevel")
        self.module = module
        self.file_handler = logging.FileHandler(conf.get_property("LOG", "fileLoc"), "w", encoding="UTF-8")
        formatter = logging.Formatter("[%(asctime)s] : %(message)s")
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self.addHandler(stream_handler)
        self.file_handler.setFormatter(formatter)
        self.setLevel(self.__get_level(logLevel))

    def get_logger(self, name):
        pass

    def __get_level(self, confLevel):
        return {'DEBUG':logging.DEBUG, 'INFO':logging.INFO, 'WARNING':logging.WARNING, 'ERROR':logging.ERROR, 'WARNING':logging.WARNING}[confLevel]