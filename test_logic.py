from collections import defaultdict
from questions import QUESTIONS
from professions import PROFESSIONS

def calculate_results(user_answers):
    """
    Подсчитывает баллы для каждой профессии на основе ответов пользователя
    
    Args:
        user_answers: словарь с ответами пользователя {question_key: answer_index}
    
    Returns:
        dict: словарь с баллами для каждой профессии
    """
    profession_scores = defaultdict(int)
    
    # Проходим по всем ответам пользователя
    for question_key, answer_index in user_answers.items():
        # Извлекаем номер вопроса из ключа (например, "question_1" -> 1)
        question_num = int(question_key.split('_')[1])
        question_data = QUESTIONS[question_num - 1]  # -1 потому что индексация с 0
        
        # Получаем выбранный ответ
        selected_answer = question_data['answers'][answer_index]
        
        # Добавляем баллы за этот ответ к соответствующим профессиям
        for profession, score in selected_answer['scores'].items():
            profession_scores[profession] += score
    
    return dict(profession_scores)

def get_top_recommendations(profession_scores, top_n=3):
    """
    Возвращает топ-N профессий с наибольшими баллами
    
    Args:
        profession_scores: словарь с баллами профессий
        top_n: количество топовых профессий для возврата
    
    Returns:
        list: список кортежей (профессия, баллы, процент_соответствия)
    """
    if not profession_scores:
        return []
    
    # Сортируем профессии по убыванию баллов
    sorted_professions = sorted(profession_scores.items(), key=lambda x: x[1], reverse=True)
    
    # Берем топ-N профессий
    top_professions = sorted_professions[:top_n]
    
    # Рассчитываем максимально возможный балл (24 вопроса * 5 баллов = 120)
    max_possible_score = 24 * 5
    
    # Создаем результат с процентами от максимально возможного балла
    recommendations = []
    for profession, score in top_professions:
        percentage = (score / max_possible_score) * 100 if max_possible_score > 0 else 0
        recommendations.append((profession, score, percentage))
    
    return recommendations

def get_profession_recommendations(profession_name):
    """
    Возвращает рекомендации для конкретной профессии
    
    Args:
        profession_name: название профессии
    
    Returns:
        dict: информация о профессии или None если не найдена
    """
    return PROFESSIONS.get(profession_name, None)

def analyze_user_profile(user_answers):
    """
    Анализирует профиль пользователя на основе его ответов
    
    Args:
        user_answers: словарь с ответами пользователя
    
    Returns:
        dict: анализ профиля пользователя
    """
    profession_scores = calculate_results(user_answers)
    top_recommendations = get_top_recommendations(profession_scores, top_n=5)
    
    # Анализируем категории профессий
    category_scores = defaultdict(int)
    for profession, score in profession_scores.items():
        if profession in PROFESSIONS:
            category = PROFESSIONS[profession]['category']
            category_scores[category] += score
    
    # Находим доминирующие категории
    sorted_categories = sorted(category_scores.items(), key=lambda x: x[1], reverse=True)
    
    analysis = {
        'total_professions_scored': len(profession_scores),
        'top_recommendations': top_recommendations,
        'category_preferences': sorted_categories[:3],
        'completion_rate': len(user_answers) / len(QUESTIONS) * 100
    }
    
    return analysis

def get_career_path_suggestions(top_profession):
    """
    Предлагает карьерные пути для выбранной профессии
    
    Args:
        top_profession: название топовой профессии
    
    Returns:
        dict: предложения по карьерному развитию
    """
    if top_profession not in PROFESSIONS:
        return None
    
    profession_info = PROFESSIONS[top_profession]
    
    # Определяем связанные профессии по категории
    related_professions = []
    for prof_name, prof_info in PROFESSIONS.items():
        if (prof_info['category'] == profession_info['category'] and 
            prof_name != top_profession):
            related_professions.append(prof_name)
    
    career_suggestions = {
        'current_profession': top_profession,
        'entry_level': profession_info['entry_level'],
        'related_professions': related_professions[:3],
        'growth_opportunities': [
            f"Senior {top_profession}",
            f"Lead {top_profession}",
            f"Архитектор в области {profession_info['category']}"
        ]
    }
    
    return career_suggestions
