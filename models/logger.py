import datetime
class Logger:
    def __init__(self, log_file):
        self.log = log_file
    
    def __repr__(self):
        return f"File Name: {self.log}"

    def setup(self):
        log_file = open(self.log, "w")
        log_file.writelines("LOGGING\n\n")
        log_file.close()

    def log_change(self, method, route, results):
        log_file = open(self.log, "a")
        now = datetime.datetime.now().strftime("%c")
        log_file.writelines(f"{method}\t{now}\t{route}\t")
        if(results is not None):
            log_file.writelines(f"{results}\n")
        log_file.close()