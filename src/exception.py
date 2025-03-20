import sys
from scripts.logger import logger

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = CustomException.get_detailed_error_message(error_message, error_detail)

    @staticmethod
    def get_detailed_error_message(error_message, error_detail: sys):
        _, _, exc_tb = error_detail.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        detailed_message = (
            f"Error occurred in file [{file_name}] at line [{line_number}]: {error_message}"
        )
        return detailed_message

    def __str__(self):
        return self.error_message

# Example usage
if __name__ == "__main__":
    try:
        x = 1 / 0
    except Exception as e:
        logger.error(CustomException(str(e), sys))
