# Mindscape

🧠 MindScape: 감정 & 성격 기반 자기성찰 AI 시스템
RAG + LLM + MCP 기반 심리 자기성찰 파트너
버전: v0.1
작성일: 2025.06.01

✅ 1. 프로젝트 개요
MindScape는 사용자의 감정 일기, 고민, 습관 등을 바탕으로

사용자의 성격을 파악하고

매일의 감정 상태를 분석하며

자기성찰을 위한 지속적 피드백과 루틴을 제공하는
LLM 기반의 감정-성격 통합 자기이해 시스템이다.

✅ 2. 핵심 목표
목표	설명
🎯 자기성찰 유도	감정과 성격 기반 피드백 제공
🧬 성격 프로파일링	Big Five 등 심리 이론 기반 사용자 성향 도출
📓 감정 일기 해석	감정 추출 및 구조적 피드백 제공
🔁 성장 루틴 제공	감정 조절·자기개발 루틴 추천
🔍 인용/이론 연계	RAG를 통해 신뢰성 있는 심리학 지식 기반 확보

✅ 3. 사용자 시나리오
성격 테스트 or 초반 대화 → 성격 프로파일 구축

감정 일기 or 고민 입력

LLM이 MCP 방식으로 감정 분석 + 성격 기반 해석 + 개선 제안

사용자는 추천 루틴/명언/자기성찰 질문을 수신

(선택) 사용자는 감정 히스토리, 통계, 루틴 실행 여부를 기록

✅ 4. 시스템 구성도

┌────────────┐
│ User Input │ ← 감정일기, 고민, 생각
└────┬───────┘
     ↓
┌────────────┐
│ Preprocess │ ← 감정 키워드 추출, 간단 필터링
└────┬───────┘
     ↓
┌─────────────┐      ┌──────────────┐
│     RAG     │◄────►│ 심리학 DB/API │← 자기계발 글귀, Big5 해설, 심리 논문
└────┬────────┘      └──────────────┘
     ↓
┌─────────────────────────────┐
│ LLM + MCP Prompt Template    │
│ 1. 감정 분석                 │
│ 2. 성격 기반 해석           │
│ 3. 성장 루틴 및 질문 생성   │
└────────┬────────────────────┘
         ↓
┌───────────────────────┐
│ Structured Response UI │ ← 피드백 + 요약 + 추천  
└───────────────────────┘

✅ 5. MCP Prompt 설계 예시

[Instruction]
당신은 따뜻한 심리상담가입니다. 사용자의 감정과 성격을 분석하고, 공감과 함께 실질적인 피드백을 주세요.

[Context]
{RAG 검색 결과: 감정조절 방법, 유사 사례, 성격 이론 등}

[User Input]
"요즘 회피적인 제 성격 때문에 친구와의 대화를 피하게 돼요. 대인관계가 어렵게 느껴져요."

[Constraints]
1. 감정 요약  
2. 성격 특성과 연결된 해석  
3. 추천 루틴 or 오늘의 질문  
4. 공감 어조 유지, 600자 내외  

✅ 6. 기술 스택
항목	도구/라이브러리
백엔드	Python (FastAPI)
LLM	OpenAI GPT-4 / Claude 3 / Mistral
RAG	LangChain + FAISS / Chroma
프롬프트 관리	LangChain PromptTemplate / LCEL
프론트엔드	Streamlit / Gradio
DB	SQLite (초기), PostgreSQL (확장 시)
감정 사전	NRC, EmoLex, LIWC 등 활용 가능

✅ 7. 주요 데이터 출처
Kaggle: Emotion Dataset / Personality Data

심리학 위키 / 상담 사례집 (웹 크롤링 가능)

명언/철학 인용 API (Stoicism, Buddhism 등)

국내 정신건강 자료 (마인드포스트, EBS 다큐 등)

✅ 8. 기능 우선순위 로드맵
단계	기능	설명
v1	성격 입력 + 감정 일기 분석	핵심 기능 구성
v2	RAG 연동 + 성장 루틴 추천	실질 피드백 강화
v3	감정 히스토리 차트 + 루틴 기록	사용자 경험 보강
v4	나만의 성격 변화 리포트	지속 사용 유도
v5	음성 입력 / 모바일 대응	실사용성 강화

✅ 9. 잠재 활용/응용 분야
청소년/대학생용 감정·자기이해 앱

정신건강 상담 전 자가 성찰 도구

감정일기 + 성격 기반 피드백 노트

심리학 교육용 인터랙티브 툴

✅ 10. 기대 효과
🧭 정체성과 감정의 통합적 자기이해

🌿 일상 속 자기성찰 루틴 형성

📚 심리학 대중화 + LLM 실용화 융합 사례


📁 최종 프로젝트 폴더 구조: mindscape/

mindscape/  
│  
├── backend/                        # Django 백엔드  
│   ├── mindscape/                  # Django 프로젝트 설정 (settings.py 등)  
│   │   ├── __init__.py  
│   │   ├── settings.py             # MySQL, OpenAI 등 설정  
│   │   ├── urls.py  
│   │   └── wsgi.py  
│   │  
│   ├── core/                       # 공통 모듈 (유틸, 인증 등)  
│   ├── users/                      # 사용자 인증 및 프로파일 앱  
│   ├── diary/                      # 감정 일기/분석 관련 앱  
│   ├── recommendation/            # 루틴 추천 관련 앱  
│   ├── rag/                        # RAG + 벡터DB 관리용 앱  
│   └── manage.py  
│  
├── frontend/                       # Streamlit 프론트엔드  
│   ├── pages/                      # 다중 페이지 구성 시  
│   ├── components/                 # 카드, 그래프, 입력 UI 등 모듈화  
│   ├── assets/                     # 이미지, 스타일, JS 등 정적 파일  
│   └── app.py                      # 메인 실행 파일  
│  
├── rag_service/                    # 벡터DB 및 LLM 호출 분리 모듈  
│   ├── loader/                     # 문서 로드 및 임베딩 스크립트  
│   ├── retriever/                  # 유사도 검색 기능  
│   └── prompts/                    # MCP 프롬프트 템플릿 관리  
│  
├── data/                           # 수집한 원시 데이터셋  
│   ├── raw/                        # 크롤링 원본  
│   ├── processed/                  # 전처리 완료 파일  
│   └── embeddings/                # 임베딩 결과 저장  
│  
├── scripts/                        # 초기화 스크립트, 배치 작업 등  
│   └── load_data.py                # 초기 데이터셋 등록용 등  
│  
├── .env                            # 환경변수(API 키, DB 비번 등)  
├── requirements.txt               # 전체 패키지 의존성 관리  
├── README.md  
└── docker-compose.yml             # (옵션) 서비스 배포용 설정  

🧩 폴더별 설명 요약  
폴더	역할  
backend/	Django 기반 REST API 서버  
frontend/	Streamlit 기반 웹 UI  
rag_service/	문서 임베딩, RAG 검색, LLM 프롬프트 처리  
data/	데이터셋 관리, 벡터화 이전/이후 포함  
scripts/	초기 로딩, 배치 처리 등 자동화  
.env	OPENAI_API_KEY, MYSQL_URL, LANGCHAIN_TRACING 등  