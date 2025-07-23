from datetime import datetime

class Date:

    def formatDate(self):
        current_time = datetime.now()
        return current_time.strftime("%B %d, %Y %H:%M:%S") 