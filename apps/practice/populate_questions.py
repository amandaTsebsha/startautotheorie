from .models import Question


def populate_questions():
    questions_data = [
        {
            "question": "Wat betekent dit verkeersbord? (Image URL here)",
            "options": ["Voorrangsweg", "Einde voorrangsweg", "Let op!", "File"],
            "answer": "Einde voorrangsweg",
            "explanation": "Dit bord geeft het einde van een voorrangsweg aan."
        },
        {
            "question": "Wat betekent een geel knipperlicht bij een verkeerslicht?",
            "options": ["Doorrijden", "Stoppen", "Voorzichtig naderen", "Snelheid verhogen"],
            "answer": "Voorzichtig naderen",
            "explanation": "Een geel knipperlicht betekent dat je voorzichtig moet naderen en voorrang moet verlenen aan andere weggebruikers."
        },

        {
            "question": "Wat zou je doen als je plotseling een stilstaande auto voor je ziet?",
            "options": ["Direct stoppen", "Langzaam voorbijrijden", "Claxonneren", "Inhalen"],
            "answer": "Direct stoppen",
            "explanation": "Bij een stilstaande auto voor je is direct stoppen de veiligste optie om botsingen te vermijden."
        },
        {
            "question": "Wat is de juiste reactie als een fietser plotseling voor je opduikt?",
            "options": ["Uitwijken", "Claxonneren", "Snel stoppen", "Langzaam naderen"],
            "answer": "Snel stoppen",
            "explanation": "Het snel stoppen voorkomt een ongeval en geeft de fietser ruimte."
        },

        # Verkeersregels (Traffic Rules)
        {
            "question": "Wat betekent een doorgetrokken streep op de weg?",
            "options": [
                "Je mag deze overschrijden",
                "Je mag deze niet overschrijden",
                "Deze geeft een inhaalstrook aan",
                "Deze geeft een parkeerstrook aan"
            ],
            "answer": "Je mag deze niet overschrijden",
            "explanation": "Een doorgetrokken streep mag je niet overschrijden om de veiligheid van het verkeer te waarborgen."
        },
        {
            "question": "Wat is de maximale snelheid op een autosnelweg in Nederland?",
            "options": ["100 km/u", "120 km/u", "130 km/u", "140 km/u"],
            "answer": "130 km/u",
            "explanation": "Op autosnelwegen is de maximale snelheid in Nederland 130 km/u, tenzij anders aangegeven."
        },

        # Verkeersinzicht (Traffic Insight)
        {
            "question": "Wat is de beste manier om files te vermijden?",
            "options": [
                "Langzaam rijden",
                "Van rijstrook wisselen",
                "Gebruik maken van navigatie-apps",
                "Altijd dezelfde route nemen"
            ],
            "answer": "Gebruik maken van navigatie-apps",
            "explanation": "Navigatie-apps kunnen actuele verkeersinformatie geven en alternatieve routes voorstellen om files te vermijden."
        },
        {
            "question": "Hoe ga je om met een situatie waarin je snel moet reageren, zoals plotseling remmen?",
            "options": ["Gas geven", "Langzaam afremmen", "Direct remmen en anticiperen", "Claxonneren"],
            "answer": "Direct remmen en anticiperen",
            "explanation": "Snelle reacties zoals remmen en anticiperen zijn essentieel in noodsituaties om een ongeval te voorkomen."
        },

        {
            "question": "Hoe kun je het beste anticiperen op het gedrag van andere bestuurders?",
            "options": [
                "Je snelheid verlagen en goed om je heen kijken",
                "Altijd inhalen",
                "Zo snel mogelijk doorrijden",
                "Je richtingaanwijzer constant gebruiken"
            ],
            "answer": "Je snelheid verlagen en goed om je heen kijken",
            "explanation": "Anticiperen vereist dat je oplettend bent en je snelheid aanpast aan de situatie."
        },
        {
            "question": "Wat is het risico van rijden te dicht op een andere auto bij slechte weersomstandigheden?",
            "options": [
                "Je hebt minder reactietijd",
                "Je spaart brandstof",
                "Je hebt meer zicht op de weg",
                "Je voorkomt dat anderen inhalen"
            ],
            "answer": "Je hebt minder reactietijd",
            "explanation": "Bij slechte weersomstandigheden is extra afstand nodig om voldoende reactietijd te hebben."
        },
        # Add more questions here...
    ]

    for question_data in questions_data:
        question, created = Question.objects.get_or_create(  # get or create to prevent duplicates
            question_text=question_data['question'],
            defaults={
                'options': question_data['options'],
                'correct_answer': question_data['answer'],
                'difficulty': question_data.get('difficulty', 1),  # Default difficulty 1
            }
        )
        if created:
            print(f"Created question: {question.question_text}")
        else:
            print(f"Question already exists: {question.question_text}")