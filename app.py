import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from professions import PROFESSIONS
from questions import QUESTIONS
from test_logic import calculate_results, get_top_recommendations
from explanation_engine import generate_profession_explanation, get_personality_insights

def main():
    st.set_page_config(
        page_title="IT Профориентация - Тест для определения IT-профессии",
        page_icon="💻",
        layout="wide"
    )
    
    st.title("🚀 Система определения подходящей IT-профессии")
    st.markdown("---")
    
    # Инициализация состояния сессии
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    if 'answers' not in st.session_state:
        st.session_state.answers = {}
    if 'test_completed' not in st.session_state:
        st.session_state.test_completed = False
    if 'show_results' not in st.session_state:
        st.session_state.show_results = False
    
    # Начальная страница
    if st.session_state.current_question == 0 and not st.session_state.test_completed:
        show_welcome_page()
    
    # Прохождение теста
    elif st.session_state.current_question > 0 and not st.session_state.test_completed:
        show_question_page()
    
    # Показ результатов
    elif st.session_state.show_results:
        show_results_page()

def show_welcome_page():
    st.markdown("### Добро пожаловать в систему профориентации!")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        **Этот тест поможет вам определить наиболее подходящую IT-профессию на основе ваших интересов и склонностей.**
        
        📋 **Как это работает:**
        - Вам будет предложено 25 вопросов
        - На каждый вопрос выберите наиболее подходящий для вас ответ
        - Система проанализирует ваши ответы и покажет топ-3 наиболее подходящих профессии
        - Вы получите подробное описание каждой рекомендованной специальности
        
        ⏱️ **Время прохождения:** 5-10 минут
        
        🎯 **Доступные профессии:** 25 актуальных IT-специальностей
        """)
    
    with col2:
        st.info(f"""
        **Статистика:**
        
        📊 Вопросов: 25
        
        💼 Профессий: {len(PROFESSIONS)}
        
        🏆 Рекомендаций: Топ-3
        """)
    
    st.markdown("---")
    
    if st.button("🚀 Начать тест", type="primary", use_container_width=True):
        st.session_state.current_question = 1
        st.rerun()

def show_question_page():
    question_num = st.session_state.current_question
    question_data = QUESTIONS[question_num - 1]
    
    # Прогресс-бар
    progress = question_num / len(QUESTIONS)
    st.progress(progress)
    
    # Информация о прогрессе
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(f"**Вопрос {question_num} из {len(QUESTIONS)}**")
    
    st.markdown("---")
    
    # Вопрос
    st.markdown(f"### {question_data['question']}")
    
    # Варианты ответов
    answer_key = f"question_{question_num}"
    
    # Получаем сохраненный ответ, если есть
    current_answer = st.session_state.answers.get(answer_key, None)
    
    # Отображаем варианты ответов
    selected_answer = st.radio(
        "Выберите наиболее подходящий для вас вариант:",
        options=list(range(len(question_data['answers']))),
        format_func=lambda x: question_data['answers'][x]['text'],
        index=current_answer if current_answer is not None else 0,
        key=f"radio_{question_num}"
    )
    
    st.markdown("---")
    
    # Кнопки навигации
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        if question_num > 1:
            if st.button("⬅️ Предыдущий", use_container_width=True):
                st.session_state.answers[answer_key] = selected_answer
                st.session_state.current_question -= 1
                st.rerun()
    
    with col2:
        st.markdown(f"<div style='text-align: center; padding: 8px;'>{question_num}/{len(QUESTIONS)}</div>", unsafe_allow_html=True)
    
    with col3:
        if question_num < len(QUESTIONS):
            if st.button("Далее ➡️", type="primary", use_container_width=True):
                st.session_state.answers[answer_key] = selected_answer
                st.session_state.current_question += 1
                st.rerun()
        else:
            if st.button("🏁 Завершить тест", type="primary", use_container_width=True):
                st.session_state.answers[answer_key] = selected_answer
                st.session_state.test_completed = True
                st.session_state.show_results = True
                st.rerun()

def show_results_page():
    st.markdown("# 🎉 Результаты теста")
    st.markdown("---")
    
    # Подсчет результатов
    results = calculate_results(st.session_state.answers)
    top_recommendations = get_top_recommendations(results, top_n=3)
    max_score = max(results.values()) if results else 1
    
    # Персональные инсайты
    personality_insights = get_personality_insights(st.session_state.answers)
    
    if personality_insights:
        st.markdown("### 💡 Ваш профессиональный профиль:")
        for insight in personality_insights:
            st.info(f"✨ {insight}")
        st.markdown("---")
    
    # Диаграмма всех результатов
    st.markdown("### 📊 Диаграмма соответствия всех профессий")
    
    # Подготовка данных для диаграммы
    max_possible_score = 24 * 5  # 24 вопроса * 5 максимальных баллов
    all_results = []
    for profession, score in results.items():
        percentage = (score / max_possible_score) * 100 if max_possible_score > 0 else 0
        all_results.append({
            'Профессия': profession,
            'Соответствие (%)': percentage,
            'Баллы': score,
            'Категория': PROFESSIONS[profession]['category']
        })
    
    # Сортировка по убыванию процентов
    all_results.sort(key=lambda x: x['Соответствие (%)'], reverse=True)
    
    # Создание интерактивной диаграммы
    df_chart = pd.DataFrame(all_results)
    
    # Горизонтальная столбчатая диаграмма всех профессий
    fig = px.bar(df_chart, 
                 y='Профессия', 
                 x='Соответствие (%)',
                 color='Категория',
                 title='Соответствие по всем IT-профессиям (%)',
                 orientation='h',
                 height=max(600, len(df_chart) * 25))  # Динамическая высота
    
    fig.update_layout(
        yaxis={'categoryorder': 'total ascending'},
        xaxis={'range': [0, 100], 'title': 'Процент соответствия (%)'},
        showlegend=True,
        font=dict(size=11),
        margin=dict(l=200, r=50, t=50, b=50)  # Больше места слева для названий профессий
    )
    
    # Форматирование подписей данных как целые проценты
    fig.update_traces(
        texttemplate='%{x:.0f}%',
        textposition='outside'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    st.markdown("### 🏆 Топ-3 наиболее подходящих профессии:")
    st.markdown("")
    
    # Отображение детальных результатов топ-3
    for i, (profession, score, percentage) in enumerate(top_recommendations, 1):
        with st.expander(f"{i}. {profession} - {percentage:.1f}% соответствие", expanded=(i==1)):
            
            # Прогресс-бар для показа процента соответствия
            st.progress(percentage / 100)
            st.markdown(f"**Соответствие: {percentage:.1f}%**")
            
            # Описание профессии
            profession_info = PROFESSIONS[profession]
            
            # Персонализированное объяснение
            explanation = generate_profession_explanation(profession, st.session_state.answers, score, max_possible_score)
            if explanation:
                st.markdown("**Почему эта профессия вам подходит:**")
                st.success(explanation)
            
            col1, col2 = st.columns([3, 2])
            
            with col1:
                st.markdown(f"**Описание:** {profession_info['description']}")
                st.markdown(f"**Основные навыки:** {', '.join(profession_info['skills'][:7])}")
                if len(profession_info['skills']) > 7:
                    st.markdown(f"**Дополнительные навыки:** {', '.join(profession_info['skills'][7:])}")
            
            with col2:
                info_text = f"""
                **Категория:** {profession_info['category']}
                
                **Уровень входа:** {profession_info['entry_level']}
                """
                
                if 'salary_range' in profession_info:
                    info_text += f"\n\n**Зарплата:** {profession_info['salary_range']}"
                
                if 'job_market' in profession_info:
                    info_text += f"\n\n**Рынок труда:** {profession_info['job_market']}"
                
                st.info(info_text)
                
                # Карьерный рост
                if 'career_path' in profession_info:
                    st.markdown("**🚀 Карьерный рост:**")
                    for level in profession_info['career_path']:
                        st.markdown(f"• {level}")
    
    # Дополнительная информация
    st.markdown("### 📊 Дополнительная информация")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 💡 Рекомендации по развитию:")
        for i, (profession, _, _) in enumerate(top_recommendations, 1):
            profession_info = PROFESSIONS[profession]
            st.markdown(f"**{i}. {profession}:**")
            for tip in profession_info['learning_tips']:
                st.markdown(f"• {tip}")
            st.markdown("")
    
    with col2:
        st.markdown("#### 🔗 Полезные ресурсы:")
        seen_resources = set()
        for profession, _, _ in top_recommendations:
            profession_info = PROFESSIONS[profession]
            for resource in profession_info['resources']:
                if resource not in seen_resources:
                    st.markdown(f"• {resource}")
                    seen_resources.add(resource)
    
    st.markdown("---")
    
    # Кнопки действий
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        if st.button("🔄 Пройти тест заново", use_container_width=True):
            # Сброс состояния
            st.session_state.current_question = 0
            st.session_state.answers = {}
            st.session_state.test_completed = False
            st.session_state.show_results = False
            st.rerun()
    
    with col2:
        if st.button("📊 Показать все результаты", use_container_width=True):
            show_detailed_results(results)
    
    with col3:
        st.download_button(
            label="📥 Скачать результаты",
            data=generate_results_text(top_recommendations),
            file_name="it_career_test_results.txt",
            mime="text/plain",
            use_container_width=True
        )

def show_detailed_results(results):
    st.markdown("### 📈 Подробные результаты по всем профессиям")
    
    # Сортировка результатов по убыванию
    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
    
    # Создание таблицы результатов
    import pandas as pd
    
    df_data = []
    max_possible_score = 24 * 5  # 24 вопроса * 5 максимальных баллов
    
    for profession, score in sorted_results:
        percentage = (score / max_possible_score) * 100
        category = PROFESSIONS[profession]['category']
        df_data.append({
            'Профессия': profession,
            'Баллы': score,
            'Соответствие (%)': f'{percentage:.1f}%',
            'Категория': category
        })
    
    df = pd.DataFrame(df_data)
    st.dataframe(df, use_container_width=True)

def generate_results_text(recommendations):
    text = "РЕЗУЛЬТАТЫ ТЕСТА НА ОПРЕДЕЛЕНИЕ IT-ПРОФЕССИИ\n"
    text += "=" * 50 + "\n\n"
    
    text += "ТОП-3 РЕКОМЕНДОВАННЫХ ПРОФЕССИИ:\n\n"
    
    for i, (profession, score, percentage) in enumerate(recommendations, 1):
        text += f"{i}. {profession}\n"
        text += f"   Соответствие: {percentage:.1f}%\n"
        text += f"   Описание: {PROFESSIONS[profession]['description']}\n"
        text += f"   Навыки: {', '.join(PROFESSIONS[profession]['skills'])}\n\n"
    
    return text

if __name__ == "__main__":
    main()
