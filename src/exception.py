import sys

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() # on which file the exception got occured.
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="error occured in python script name[{0}] line number[{1}] error message[{2}]".format(
    file_name,exc_tab.tb_lineno,str(error)
    return error_message
    )
class CustomException(Exception):
    def __inti__(self,error_message,error_detail:sys):
        super.__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    
if __name__=="__main__":
    logging.info("Logging has started")