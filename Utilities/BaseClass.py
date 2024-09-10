import inspect
import logging
import pytest


@pytest.mark.usefixtures("LoginSetup")
class Baseclass:
    def Get_Logger(self):
        LoggerName = inspect.stack()[1][3]
        Logger = logging.getLogger(LoggerName)
        Filehandler = logging.FileHandler('logfile.log')
        Formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        Filehandler.setFormatter(Formatter)
        Logger.addHandler(Filehandler)
        Logger.setLevel(logging.DEBUG)
        return Logger