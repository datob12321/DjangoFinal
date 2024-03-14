import json
from .models import Language


class Question:
    def __init__(self, question_text, answers: dict, correct_answer):
        self.question_text = question_text
        self.answers = answers
        self.correct_answer = correct_answer


questions = ['What is the French word for "hello"?', 'How do you say "thank you" in French?',
             'What does "au revoir" mean in English?', 'What is the correct plural form of "chat" (cat) in French?',
             'How would you ask someone "How are you?" in French?', 'What is the French word for "book"?',
             ' How do you say "I will go to Paris next week" in French?', 'What is the French word for "friend"?',
             'Which expression means "to go for a hike"?', 'What does "se débrouiller" mean?']

probable_answers = [
    {'a': 'Bonjour', 'b': 'Au revoir', 'c': 'Merci', 'd': 'Oui'},
    {'a': 'Bonjour', 'b': 'Merci', 'c': 'Oui', 'd': 'Non'},
    {'a': 'Goodbye', 'b': 'Hello', 'c': 'Thank ', 'd': 'Yes'},
    {'a': 'Chate', 'b': 'Chats', 'c': 'Chatte', 'd': 'Chatses'},
    {'a': "Comment tu t'appelles ?", 'b': "Où habites-tu ?", 'c': "Comment ça va ?", 'd': "Quel âge as-tu ?"},
    {'a': 'Livre', 'b': 'Baguette', 'c': 'Pomme', 'd': 'Chien'},
    {'a': 'Je vais à Paris la semaine dernière', 'b': 'Je vais à Paris la semaine prochaine', 'c': 'Je suis allé à Paris hier', 'd': 'Je suis allé à Paris hier'},
    {'a': 'Amour', 'b': 'Frère', 'c': 'Ami', 'd': 'Soeur'},
    {'a': "Faire de la randonnée", 'b': "Faire du vélo", 'c': "Faire du ski", 'd': "Faire du shopping"},
    {'a': 'To struggle', 'b': 'To succeed', 'c': 'To swim', 'd': 'To study'}]


correct_answers = ['a', 'b', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'a']

all_questions = []



french = Language.objects.get(name='French')
# print(french.name)


print(len(questions))