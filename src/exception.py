#access system specific information
import sys
#custom logger
from logger import logging

def erorr_message_detail(error, error_detail: sys):
    #error raised
    #error_detail: sys module
    _, _, exc_tb = error_detail.exc.info()
    #exc_info(): exc_type, exc_value, exc_traceback, only need the last one
    #file name, line number, function name
    file_name = exc_tb.tb_frame.f_code.co_filename
    #get filename where error has occured
    #.tb_frame: gives stack frame where exception has occured
    #tb_frame.f_code
    #f_code: func name, file name, line number, compiled bytecode
    #f_code.co_filename: name of python file
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))
    
    return error_message

#define a custom exception class
class CustomException(Exception):
    def __init__(self, error_message, error_details:sys):
        super().__init__(error_message)
        self.error_message = error_message(error_message, error_detail = error_details)
        
    def __str__(self):
        return self.error_message
