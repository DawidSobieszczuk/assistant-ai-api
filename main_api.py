from config import Config

class App():
    def __init__(self):
        Config.load_from_file("config.yaml")

App()