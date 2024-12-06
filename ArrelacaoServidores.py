import PyPDF2
import re
from app.linkedlist import LinkedList
from app.filedialog import FileDialog
from app.node import Node

class App:
    def main(self):
        linked_list = LinkedList()
        file_dialog = FileDialog()
        file_path = file_dialog.open_file()

        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''

            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += page.extract_text()

            text = re.sub(r"\r?\n", " ", text)

            pattern = re.compile(r"(\d+\.1)\s+-\s+([\w\s]+)\s+(\d{3}\.\d{3}\.\d{3}-\d{2})")
            matches = pattern.findall(text)

            for match in matches:
                node = Node(
                    enrollment=match[0],
                    name=match[1].strip(),
                    cpf=match[2]
                )
                linked_list.insert(node)

            linked_list.to_excel("servidores.xlsx")

if __name__ == "__main__":
    app = App()
    app.main()