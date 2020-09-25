import csv

class AssetsList():

    @staticmethod
    def get_assetslist():
        file = open('bovespa_assets.csv', encoding='utf-8')
        lines = csv.reader(file, delimiter=";")

        assets = []

        for line in lines:
            assets.append(line[0])
        print(assets)
        return assets
