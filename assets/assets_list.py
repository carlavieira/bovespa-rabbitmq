import csv

class AssetsList():
    """
    classe responsável por realizar a leitura do arquivo csv com os ativos da bolsa e responder uma lista.
    """
    @staticmethod
    def get_assetslist():
        """
        método estático que realiza a leitura do arquivo csv `bovespa_assets.csv` com os ativos da bolsa e responder uma lista com todos os códigos.
        """
        file = open('assets/bovespa_assets.csv', encoding='utf-8')
        lines = csv.reader(file, delimiter=";")

        assets = []

        for line in lines:
            assets.append(line[0])
        return assets