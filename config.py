import yaml

class Config():
    mysql_host:str
    mysql_port:int
    mysql_user:str
    mysql_password:str
    mysql_database:str

    @staticmethod
    def load_from_file(file:str,) -> None:
        with open(file, "r") as config_file:
            config = yaml.safe_load(config_file)

        Config.mysql_host = config["mysql"]["host"]
        Config.mysql_port = config["mysql"]["port"]
        Config.mysql_user = config["mysql"]["user"]
        Config.mysql_password = config["mysql"]["password"]
        Config.mysql_database = config["mysql"]["database"]

        Config.entity_app = config["entities"]["app_id"]
        Config.entity_system = config["entities"]["system_id"]
        Config.entity_agent_basic_info = config["entities"]["agents"]["basic_info_id"]