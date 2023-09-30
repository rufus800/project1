import sys
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QGridLayout, QMessageBox

# Sample trivia questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris",
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Venus", "Jupiter"],
        "answer": "Mars",
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["Elephant", "Giraffe", "Lion", "Blue Whale"],
        "answer": "Blue Whale",
    },
    {
        "question": "What is the capital of Japan?",
        "options": ["Tokyo", "Beijing", "Seoul", "Bangkok"],
        "answer": "Tokyo",
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Mars", "Venus", "Jupiter"],
        "answer": "Jupiter",
    },
    {
        "question": "What is the tallest mountain in the world?",
        "options": ["Mount Kilimanjaro", "Mount Everest", "Mount Fuji", "Mount McKinley"],
        "answer": "Mount Everest",
    },
    {
        "question": "Which gas do plants absorb from the atmosphere during photosynthesis?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        "answer": "Carbon Dioxide",
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["Au", "Ag", "Fe", "Cu"],
        "answer": "Au",
    },
    {
        "question": "Which famous scientist formulated the theory of general relativity?",
        "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Stephen Hawking"],
        "answer": "Albert Einstein",
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": "Pacific Ocean",
    },
    {
        "question": "Which gas makes up the majority of Earth's atmosphere?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        "answer": "Nitrogen",
    },
    {
        "question": "Which planet is often referred to as the 'Red Planet'?",
        "options": ["Earth", "Mars", "Venus", "Jupiter"],
        "answer": "Mars",
    },
    {
        "question": "What is the largest species of shark?",
        "options": ["Great White Shark", "Hammerhead Shark", "Tiger Shark", "Whale Shark"],
        "answer": "Whale Shark",
    },
    {
        "question": "Which country is known as the Land of the Rising Sun?",
        "options": ["China", "South Korea", "Japan", "Vietnam"],
        "answer": "Japan",
    },
    {
        "question": "What is the capital of Italy?",
        "options": ["Rome", "Madrid", "Berlin", "Athens"],
        "answer": "Rome",
    },
    {
        "question": "Which gas do humans breathe out when they exhale?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        "answer": "Carbon Dioxide",
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"],
        "answer": "William Shakespeare",
    },
    {
        "question": "What is the largest desert in the world?",
        "options": ["Sahara Desert", "Arctic Desert", "Gobi Desert", "Atacama Desert"],
        "answer": "Sahara Desert",
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["H2O", "CO2", "O2", "N2"],
        "answer": "H2O",
    },
    {
        "question": "Who painted the 'Mona Lisa'?",
        "options": ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Claude Monet"],
        "answer": "Leonardo da Vinci",
    },

]

class TriviaGame(QWidget):
    def __init__(self, width=600, height=500):
        super().__init__()
        self.width = width
        self.height = height
        self.initUI()
        
        # Set window icon
        app_icon = QIcon("app_icon.ico")  # Replace with your icon file path
        self.setWindowIcon(app_icon)

        # Set background color
        self.setStyleSheet('background: #A1C7D3;')

    def initUI(self):
        self.setWindowTitle('TriviaFrenzy')
        self.resize(self.width, self.height)

        self.score = 0
        self.current_question_index = 0

        self.layout = QVBoxLayout()

        self.question_label = QLabel('')
        self.layout.addWidget(self.question_label)
        self.question_label.setStyleSheet("font-size: 21px; ")  # Increase font size
        self.options_grid = QGridLayout()
        self.layout.addLayout(self.options_grid)

        self.option_buttons = []

        for i in range(4):
            option_button = QPushButton('')
            self.option_buttons.append(option_button)
            self.options_grid.addWidget(option_button, i // 2, i % 2)
            option_button.clicked.connect(self.check_answer)
            option_button.setStyleSheet(
                "*{background: #4D5FE7;" +
                "color: white;" +
                "border: 2px solid '#000000';" +
                "border-radius: 18px;" +
                "font-size: 18px;" +
                "margin: 5px;" +  # Add margin to space out the buttons
                "padding: 10px 24px}" +
                "*:hover{border:none;}"
            )

        self.answer_button = QPushButton('Submit Answer')
        self.answer_button.clicked.connect(self.next_question)
        self.layout.addWidget(self.answer_button)
        self.answer_button.setStyleSheet(
            "*{background: #4D5FE7;" +
            "color: white;" +
            "border: 2px solid '#000000';" +
            "border-radius: 18px;" +
            "font-size: 20px;" +
            "margin: 0px 128px;" +
            "padding: 10px 24px}" +
            "*:hover{border:none;}"
        )

        self.play_again_button = QPushButton('Play Again')
        self.play_again_button.clicked.connect(self.play_again)
        self.layout.addWidget(self.play_again_button)
        self.play_again_button.setStyleSheet(
            "*{background: #4D5FE7;" +
            "color: white;" +
            "border: 2px solid '#000000';" +
            "border-radius: 15px;" +
            "font-size: 18px;" +
            "margin: 0px 128px;" +
            "padding: 10px 24px}" +
            "*:hover{border:none;}"
        )
        self.play_again_button.setVisible(False)  # Initially hidden

        self.setLayout(self.layout)

        self.load_question()

    def load_question(self):
        if self.current_question_index < len(questions):
            question_data = questions[self.current_question_index]
            self.question_label.setText(question_data['question'])

            options = question_data['options']
            for i in range(4):
                self.option_buttons[i].setText(options[i])
                self.option_buttons[i].setEnabled(True)

            self.answer_button.setEnabled(False)
        else:
            self.show_result()

    def check_answer(self):
        sender = self.sender()
        selected_answer = sender.text()
        correct_answer = questions[self.current_question_index]['answer']

        if selected_answer == correct_answer:
            self.score += 5

        for button in self.option_buttons:
            button.setEnabled(False)

        self.answer_button.setEnabled(True)

    def next_question(self):
        self.current_question_index += 1

        for button in self.option_buttons:
            button.setEnabled(True)

        if self.current_question_index < len(questions):
            self.load_question()
        else:
            self.show_result()

    def show_result(self):
        result_message = f'You answered {self.score} out of {len(questions) * 5} questions correctly.'
        QMessageBox.information(self, 'Trivia Game Result', result_message, QMessageBox.Ok)
        self.play_again_button.setVisible(True)

    def play_again(self):
        self.current_question_index = 0
        self.score = 0
        self.load_question()
        self.play_again_button.setVisible(False)

class HomePage(QWidget):
    def __init__(self, width=600, height=500):
        super().__init__()
        self.width = width
        self.height = height
        self.initUI()
        
        # Set window icon
        app_icon = QIcon("app_icon.ico")  # Replace with your icon file path
        self.setWindowIcon(app_icon)

        # Set background color and style
        self.setStyleSheet('background: #4D5FE7; color: white;')

    def initUI(self):
        self.setWindowTitle('TriviaFrenzy')
        self.resize(self.width, self.height)

        self.layout = QVBoxLayout()

        self.title_label = QLabel('Welcome to TriviaFrenzy')
        self.layout.addWidget(self.title_label)
        self.title_label.setStyleSheet(
            "font-size: 20px; margin: 0 auto; padding: 10px 24px; text-align: center;"
        )

        self.start_button = QPushButton('Start Game')
        self.start_button.clicked.connect(self.start_game)
        self.layout.addWidget(self.start_button)
        self.start_button.setStyleSheet(
            "*{background: #A1C7D3;" +
            "color: white;" +
            "border: 2px solid '#000000';" +
            "border-radius: 15px;" +
            "font-size: 18px;" +
            "margin: 0 auto;" +
            "padding: 10px 24px}" +
            "*:hover{border:none;}"
        )

        # Center-align the contents in the layout
        self.layout.setAlignment(QtCore.Qt.AlignCenter)

        self.setLayout(self.layout)

    def start_game(self):
        self.trivia_game = TriviaGame()
        self.trivia_game.show()
        self.close()

def main():
    app = QApplication(sys.argv)
    home_page = HomePage()
    home_page.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
