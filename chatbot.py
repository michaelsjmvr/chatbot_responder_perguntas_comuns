import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget, QLineEdit
from nltk.chat.util import Chat, reflections

# Definição da classe principal do aplicativo do chatbot
class ChatbotApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configurações da janela principal
        self.setWindowTitle("Chatbot")
        self.setGeometry(100, 100, 400, 400)

        # Configuração do widget central
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Configuração do layout vertical
        self.layout = QVBoxLayout()

        # Campo de entrada de nome do usuário
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("Seu nome")
        self.layout.addWidget(self.name_edit)

        # Campo de entrada de pergunta do usuário
        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("Digite sua pergunta aqui...")
        self.layout.addWidget(self.text_edit)

        # Botão "Enviar" para enviar a pergunta
        self.send_button = QPushButton("Enviar")
        self.send_button.clicked.connect(self.process_question)
        self.layout.addWidget(self.send_button)

        # Área de exibição de respostas do chatbot
        self.response_text = QTextEdit()
        self.response_text.setReadOnly(True)
        self.layout.addWidget(self.response_text)

        # Configuração do layout vertical no widget central
        self.central_widget.setLayout(self.layout)

        # Inicialização do chatbot
        self.chatbot = Chat(pairs, reflections)

        # Variáveis para armazenar nomes
        self.user_name = None  # Nome do usuário
        self.bot_name = "Nick"  # Nome do bot

        # Exibir a janela
        self.show()

    # Função para processar a pergunta do usuário
    def process_question(self):
        user_name = self.name_edit.text()  # Obtém o nome do usuário
        user_input = self.text_edit.toPlainText()  # Obtém a pergunta do usuário

        if user_name:
            # Se o usuário inseriu seu nome, inclua-o na resposta com espaço após os dois pontos
            formatted_response = f"{user_name}: {user_input}\n{self.bot_name}: {self.chatbot.respond(user_input)}"
        else:
            # Se o usuário não inseriu um nome, apenas inclua o nome do bot na resposta com espaço após os dois pontos
            formatted_response = f"{self.bot_name}: {self.chatbot.respond(user_input)}"

        # Exibir a resposta formatada na área de respostas
        self.response_text.setPlainText(formatted_response)

        # Limpar o campo de pergunta
        self.text_edit.clear()

# Pares de padrões para respostas do chatbot
pairs = [
    [
        r"Meu nome é (.*)",
        ["Olá, %1! Como posso ajudar você hoje?",]
    ],
    [
        r"Qual é o seu nome?",
        ["Meu nome é Nick e estou aqui para ajudar.",]
    ],
    [
        r"Como você está?",
        ["Estou bem, obrigado por perguntar.",]
    ],
    [
        r"(adeus|tchau|até logo)",
        ["Tchau! Tenha um bom dia.", "Até logo!",]
    ],
]

# Inicialização do aplicativo Qt
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatbotApp()
    sys.exit(app.exec())
