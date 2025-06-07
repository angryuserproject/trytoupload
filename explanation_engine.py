"""
Модуль для генерации персонализированных объяснений результатов теста
"""
from questions import QUESTIONS

def generate_profession_explanation(profession_name, user_answers, profession_score, max_score):
    """
    Генерирует персонализированное объяснение почему профессия подходит пользователю
    
    Args:
        profession_name: название профессии
        user_answers: ответы пользователя
        profession_score: набранные баллы за профессию
        max_score: максимальный балл среди всех профессий
    
    Returns:
        str: персонализированное объяснение
    """
    relevant_answers = []
    
    # Анализируем ответы пользователя и находим релевантные для данной профессии
    for question_key, answer_index in user_answers.items():
        question_num = int(question_key.split('_')[1])
        question_data = QUESTIONS[question_num - 1]
        selected_answer = question_data['answers'][answer_index]
        
        # Если в ответе есть баллы для этой профессии
        if profession_name in selected_answer['scores']:
            score = selected_answer['scores'][profession_name]
            if score > 0:  # Только положительные баллы
                relevant_answers.append({
                    'question': question_data['question'],
                    'answer': selected_answer['text'],
                    'score': score,
                    'question_num': question_num
                })
    
    # Сортируем по убыванию баллов
    relevant_answers.sort(key=lambda x: x['score'], reverse=True)
    
    # Генерируем объяснение
    explanation_parts = []
    
    if relevant_answers:
        explanation_parts.append(f"Эта профессия подходит вам на {(profession_score/max_score)*100:.1f}% на основе следующих ваших предпочтений:")
        
        # Берем топ-3 наиболее релевантных ответа
        for i, answer_data in enumerate(relevant_answers[:3], 1):
            explanation_parts.append(f"• {answer_data['answer']} (вопрос {answer_data['question_num']})")
    
    return "\n".join(explanation_parts)

def analyze_answer_patterns(user_answers):
    """
    Анализирует паттерны в ответах пользователя для общего профиля
    
    Args:
        user_answers: ответы пользователя
    
    Returns:
        dict: анализ паттернов
    """
    patterns = {
        'creative_orientation': 0,
        'technical_depth': 0,
        'people_focus': 0,
        'analytical_thinking': 0,
        'system_thinking': 0,
        'innovation_focus': 0
    }
    
    # Ключевые слова для каждого паттерна
    pattern_keywords = {
        'creative_orientation': ['креативность', 'творческий', 'дизайн', 'интерфейс', 'визуальн'],
        'technical_depth': ['технический', 'глубина', 'алгоритм', 'архитектура', 'система'],
        'people_focus': ['пользователи', 'команда', 'клиенты', 'контакт', 'взаимодействие'],
        'analytical_thinking': ['анализ', 'данные', 'исследование', 'метрики', 'статистика'],
        'system_thinking': ['система', 'процесс', 'инфраструктура', 'стабильность', 'надежность'],
        'innovation_focus': ['новые технологии', 'тренды', 'инновации', 'обучение', 'развитие']
    }
    
    # Анализируем каждый ответ
    for question_key, answer_index in user_answers.items():
        question_num = int(question_key.split('_')[1])
        question_data = QUESTIONS[question_num - 1]
        selected_answer = question_data['answers'][answer_index]
        answer_text = selected_answer['text'].lower()
        
        # Проверяем наличие ключевых слов
        for pattern, keywords in pattern_keywords.items():
            for keyword in keywords:
                if keyword in answer_text:
                    patterns[pattern] += 1
                    break
    
    return patterns

def get_personality_insights(user_answers):
    """
    Возвращает инсайты о личности пользователя на основе ответов
    
    Args:
        user_answers: ответы пользователя
    
    Returns:
        list: список инсайтов
    """
    patterns = analyze_answer_patterns(user_answers)
    insights = []
    
    # Определяем доминирующие черты
    max_pattern = max(patterns.items(), key=lambda x: x[1])
    
    if max_pattern[0] == 'creative_orientation' and max_pattern[1] > 2:
        insights.append("У вас выражена креативная направленность - вы цените красоту, дизайн и пользовательский опыт")
    
    if max_pattern[0] == 'technical_depth' and max_pattern[1] > 2:
        insights.append("Вы предпочитаете глубокое техническое погружение и решение сложных алгоритмических задач")
    
    if max_pattern[0] == 'people_focus' and max_pattern[1] > 2:
        insights.append("Вам важно взаимодействие с людьми и влияние на пользователей")
    
    if max_pattern[0] == 'analytical_thinking' and max_pattern[1] > 2:
        insights.append("У вас сильно развито аналитическое мышление и склонность к работе с данными")
    
    if max_pattern[0] == 'system_thinking' and max_pattern[1] > 2:
        insights.append("Вы мыслите системно и цените стабильность, надежность процессов")
    
    if max_pattern[0] == 'innovation_focus' and max_pattern[1] > 2:
        insights.append("Вас привлекают новые технологии и постоянное профессиональное развитие")
    
    return insights if insights else ["Ваш профиль сбалансирован по разным направлениям"]