
import random
import streamlit as st

# 웹앱 제목
st.title("🍱 오늘의 점심 메뉴 추천")
st.write("오늘 점심은 뭘 먹을까요? 버튼을 눌러 메뉴를 추천받아 보세요!")

# 점심 메뉴 목록
menu_list = [
    "🍚 김치볶음밥",
    "🍜 짜장면",
    "🍝 파스타",
    "🍛 카레라이스",
    "🍔 햄버거",
    "🍕 피자",
    "🍣 초밥",
    "🍲 순두부찌개",
    "🥘 부대찌개",
    "🍗 치킨",
    "🌮 타코",
    "🥗 샐러드",
    "🍖 제육볶음",
    "🍜 돈코츠 라멘",
    "🥪 샌드위치"
]

# 메뉴 추천 버튼
if st.button("🎲 오늘의 점심 메뉴 추천받기"):
    # 랜덤으로 메뉴 선택
    today_menu = random.choice(menu_list)

    # 추천 결과 출력
    st.success("오늘의 점심 메뉴는!")
    st.header(today_menu)
    st.balloons()

# 안내 문구
st.write("---")
st.caption("맛있는 점심 식사 하세요! 😊")
