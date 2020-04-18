class Command:
    def __init__(self, label):
        self.label = label

    def get_label(self):
        return self.label

    def print_usage(self):
        print("Cette commande n'a pas d'usage pour le moment")

    def debug(self):
        print("Je call la commande " + self.label)

    def run(self, harpokrat_api, args):
        print("run -> " + self.label)
