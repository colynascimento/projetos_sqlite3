class Cliente:
    def __init__(self, id_cliente, nome, data_nascimento, nacionalidade, documento, telefone, email, deficiencia_legal_check, deficiencia_legal):
        self.id_cliente = id_cliente
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.nacionalidade = nacionalidade
        self.documento = documento
        self.telefone = telefone
        self.email = email
        self.deficiencia_legal_check = deficiencia_legal_check
        self.deficiencia_legal = deficiencia_legal