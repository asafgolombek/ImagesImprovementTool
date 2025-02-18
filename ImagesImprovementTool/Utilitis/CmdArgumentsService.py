import argparse
from Consts import FilesConts

class CmdArgumentsService:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="app cmd line arguments")
        self.parser.add_argument("--configuration_file", help="Path to the configuration file", default=FilesConts.default_configuration_file)
        self.args = self.parser.parse_args()

    def getConfigurationFilePath(self):
        return self.args.configuration_file


