import os
import sys

def error_message_details(error:Exception,error_detail:sys) -> str:
    _,_,exc_tb = error_detail.exc_info()

    file_name = os.path.join(exc_tb.tb_frame.f_code.co_filename)[1]

    error_message = f"Error occurred at python filename: {file_name} , line number: {exc_tb.tb_lineno} and error: {str(error)}"

    return error_message


class XRayException(Exception):

    def __init__(self,error_message,error_detail):

        super().__init__(error_message)

        self.error_message = error_message_details(
            error_message,error_detail=error_detail
        )

    def __str__(self):
        return self.error_message