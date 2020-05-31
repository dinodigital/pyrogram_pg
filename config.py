from configparser import ConfigParser

cfg_parser = ConfigParser()
cfg_parser.read('config.ini')


def get_cfg(name):
    return cfg_parser[name]
