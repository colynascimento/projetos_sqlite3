class Rota:
    def __init__(self, cod_rota, cod_linha_aerea, cod_iata_origem, cod_iata_destino, preco_base):
        self.cod_rota = cod_rota
        self.cod_linha_aerea = cod_linha_aerea
        self.cod_iata_origem = cod_iata_origem
        self.cod_iata_destino = cod_iata_destino
        self.preco_base = preco_base