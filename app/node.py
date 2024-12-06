class Node:
    def __init__(self, enrollment, name, cpf):
        self.enrollment = enrollment
        self.name = name
        self.cpf = cpf
        self.next = None

    def __str__(self):
        return f"Matricula: {self.enrollment}, Nome: {self.name}, CPF: {self.cpf}"