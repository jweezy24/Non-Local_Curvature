import yaml

class parser:

    def __init__(self, file_path="./config.yaml"):
        file = open(file_path, "r")
        self.args = yaml.load(file)
        file.close()
