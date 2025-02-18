from Utilitis.CmdArgumentsService import CmdArgumentsService
from Utilitis.ConfigurationService import ConfigurationService

def main():
    cmd_arguments_service = CmdArgumentsService()
    configurationService = ConfigurationService(cmd_arguments_service)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

