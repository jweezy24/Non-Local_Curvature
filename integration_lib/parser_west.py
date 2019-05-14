import yaml

class parser:

    def __init__(self):
        file = open("./config.yaml", "r")
        self.args = yaml.load(file)
