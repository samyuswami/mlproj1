
'''The sys module gives you access to interpreter-level functions, parameters, and settings.
#allows interaction with python runtime environment
#allows access to system specific parameters and functions'''

'''This code creates a custom error handler that prints where the error happened (file + line number + message).

🧩 Step-by-step pipeline:
import sys
→ Loads the sys module to get error info from the Python interpreter.

def error_message_detail(error, error_detail:sys):
→ A function that takes an error and uses sys to get detailed info.

error_detail.exc_info()
→ Gets info about the most recent exception (type, value, traceback).

exc_tb.tb_frame.f_code.co_filename
→ Gets the filename where the error occurred.

exc_tb.tb_lineno
→ Gets the line number where the error happened.

error_message=...
→ Formats a message like:
"Error occurred in python script name [filename] line number [X] error message [Y]"

class CustomException(Exception):
→ Creates a custom exception class that:

Uses error_message_detail() to build a detailed error message.

Stores this message in self.error_message.

__str__ method
→ When you print the exception, it shows the full custom message.'''
import sys
from src.logger import logging 

#when we get an error from interpreter(we know using sys) we push that here
def error_message_detail(error,error_detail:sys):
    #what exception,which file,which line?->exc_tb (first two not interested)
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    
    error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message) #we have inherited from the built-in python exception class and we are running the parent init function
        self.error_message=error_message_detail(error_message,error_detail=error_detail)    
    def __str__(self):
        return self.error_message  


