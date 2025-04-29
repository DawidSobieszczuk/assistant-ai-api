import datetime

class Helper:
    @staticmethod
    def get_timestamp() -> str:
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")