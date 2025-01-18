import streamlit as st

def get_saju_and_study_method(mbti):
    mbti_data = {
        'INTP': ('사주: 지혜롭고 분석적인 성향, 논리적 사고', '학습방법: 이론적인 학습과 분석적인 접근이 효과적'),
        'INTJ': ('사주: 전략적이고 계획적인 성향', '학습방법: 효율적이고 목표 지향적인 학습 방법이 유효'),
        'INFJ': ('사주: 직관적이고 창의적인 성향', '학습방법: 창의적이고 개념 중심 학습'),
        'INFP': ('사주: 이상주의적이고 감성적인 성향', '학습방법: 자기 주도적이고 감성적 접근이 좋은 학습 방법'),
        
        'ENTP': ('사주: 창의적이고 혁신적인 성향', '학습방법: 창의적이고 비판적인 사고를 통한 문제 해결법 학습'),
        'ENTJ': ('사주: 지도력과 전략적인 성향', '학습방법: 목표 지향적이고 논리적인 학습 방법이 효과적'),
        'ENFJ': ('사주: 사람 중심적이고 동정적인 성향', '학습방법: 사회적이고 협력적인 학습 방식이 유효'),
        'ENFP': ('사주: 열정적이고 자유로운 성향', '학습방법: 탐구적이고 창의적인 접근이 좋은 학습 방법'),
        
        'ISTP': ('사주: 실용적이고 직관적인 성향', '학습방법: 실습과 경험을 통한 학습이 유효'),
        'ISTJ': ('사주: 신중하고 책임감 있는 성향', '학습방법: 체계적이고 규칙적인 학습 방식이 효과적'),
        'ISFP': ('사주: 예술적이고 감성적인 성향', '학습방법: 창의적이고 직관적인 접근이 효과적'),
        'ISFJ': ('사주: 조용하고 배려 깊은 성향', '학습방법: 규칙적이고 체계적인 학습이 유효'),
        
        'ESTP': ('사주: 모험적이고 현실적인 성향', '학습방법: 실험적이고 활동적인 학습 방법이 효과적'),
        'ESTJ': ('사주: 결정적이고 조직적인 성향', '학습방법: 목표 지향적이고 계획적인 학습 방법이 유효'),
        'ESFP': ('사주: 사교적이고 열정적인 성향', '학습방법: 경험적이고 활동적인 학습 방법이 효과적'),
        'ESFJ': ('사주: 협력적이고 배려심 많은 성향', '학습방법: 사람 중심적이고 협력적인 학습 방식이 유효'),
    }

    return mbti_data.get(mbti, ('알 수 없는 MBTI', '적절한 학습 방법을 제공할 수 없습니다.'))

def main():
    st.markdown("""
    <style>
    body {
        background-image: url('https://www.w3schools.com/w3images/forestbridge.jpg');
        background-size: cover;
        color: white;
    }
    h1 {
        color: #FFD700;
        font-size: 40px;
        font-family: 'Courier New', Courier, monospace;
        text-align: center;
    }
    h2 {
        color: #00FF00;
    }
    .stTextInput>div>div>input {
        background-color: #222222;
        color: white;
        border: 2px solid #FFD700;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.title("MBTI 기반 사주 및 학습 방법")
    
    # 사용자에게 MBTI 입력받기
    mbti = st.text_input("당신의 MBTI를 입력하세요 (예: INTP): ")
    
    if mbti:
        saju, study_method = get_saju_and_study_method(mbti.upper())
        st.write(f"사주: {saju}")
        st.write(f"추천 학습 방법: {study_method}")
    
if __name__ == "__main__":
    main()
