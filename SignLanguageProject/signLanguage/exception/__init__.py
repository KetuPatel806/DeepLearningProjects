import sys

def error_message_detail(error, error_detail:sys) :
    #error_detail.exc_info() returns a tuple containing:
    #Exception type (ignored here with _).
    #Exception value (ignored here with _).
    #Traceback object (exc_tb): Contains information about where the exception occurred.
    #Result: exc_tb holds the traceback details.
    _, _, exc_tb = error_detail.exc_info()
    #Explanation:
    #exc_tb.tb_frame: Accesses the frame object of the traceback.
    #tb_frame.f_code: Provides the code object from the frame.
    #f_code.co_filename: Retrieves the name of the Python script where the exception occurred.
    #Result: file_name contains the script’s name where the error occurred.
    file_name = exc_tb.tb_frame.f_code.co_filename
    #A formatted string is created that includes:
    #{0}: Name of the Python script (file_name).
    #{1}: Line number where the error occurred (exc_tb.tb_lineno).
    #{2}: Actual error message from the exception (str(error)).
    error_message = "Error occured python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno, str(error)
    )

    return error_message

class SignException(Exception) :
    ## The constructor (__init__) initializes the exception object.
    ## Parameters:
    ## error_message: A string representing the error message.
    ## error_detail: The sys module used to extract error details.
    def __init__(self, error_message, error_detail):
        """
        Param error_message: error message is string format
        """
    ## Calls the parent Exception class's constructor to initialize it with the provided error_message.
        super().__init__(error_message)
    ## Calls the error_message_detail function to generate a detailed error message.
    ## Stores this detailed message in the instance variable self.error_message.
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )
    ## Overrides the __str__ method to return the detailed error message 
    ## whenever the exception object is printed or converted to a string.
    def __str__(self):
        return self.error_message