import datetime
from functools import wraps


#Log Module Decorator
#Creates log file, with additional message
#log file available in Logs folder, filename "Log_YYYY-mm-DD.txt"
def write_log_custom(str_message='no message'):
    try:
        def write_log(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                now_datetime = datetime.datetime.now()
                log_file_name= "log_{}.txt".format(now_datetime.strftime("%Y-%m-%d"))
                with open("Logs\{}".format(log_file_name),'a') as log_file:
                    log_file.write("[{}] - ({}) - {} \n".format(now_datetime.strftime("%Y-%m-%d %H:%M:%S"),func.__name__,str_message))
                return func(*args, **kwargs)
            return wrapper
        return write_log
    except Exception as err:
        print('log module error: {}, type: {}'.format(err,type(err)))