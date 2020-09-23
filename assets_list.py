import csv

class AssetsList():

    @staticmethod
    def get_assetslist():

        file = open('bovespa_assets.csv')

        lines = csv.reader(file, delimiter=";")

        assets = []

        for line in lines:
            assets.append(line[0])

        return assets
