import pandas as pd
from app.node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def __del__(self):
        while self.head is not None:
            self.remove()

    def insert(self, node):
        new_node = Node(
            node.enrollment, 
            node.name, 
            node.cpf
        )
        new_node.next = self.head
        self.head = new_node

    def remove(self):
        if self.head is not None:
            temp = self.head
            self.head = self.head.next
            del temp

    def print_list(self):
        current = self.head
        while current is not None:
            print(current)
            current = current.next

    def to_excel(self, filename: str):
        data = []
        current = self.head
        while current:
            data.append({
                "Matricula": current.enrollment,
                "Nome": current.name,
                "CPF": current.cpf
            })
            current = current.next

        df = pd.DataFrame(data)

        df.to_excel(filename, index=False)