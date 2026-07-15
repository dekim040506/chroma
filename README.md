# Chroma Vector Database Practice

## 프로젝트 소개

ChromaDB에 문서를 저장하고 검색하는 방법을 연습하는 프로젝트입니다.
저장된 문서를 HTML 보고서로 내보내거나 Streamlit 웹 화면에서 확인할 수 있습니다.

## 파일 설명

- `10_chroma_basic_test.py`: 컬렉션 생성, 테스트 문서 저장 및 의미 검색
- `20_view.py`: 저장된 문서를 HTML 보고서로 내보내기
- `21_chroma_viewer.py`: Streamlit에서 문서 조회 및 의미 검색
- `requirements.txt`: 실행에 필요한 Python 패키지 목록

## 필요한 프로그램

- Python 3
- Python 가상환경 모듈(`venv`)
- 인터넷 연결(패키지 및 최초 임베딩 모델 다운로드에 필요)

Python 설치 여부를 확인합니다.

```bash
python --version
```

Ubuntu에서 가상환경을 만들 수 없다는 오류가 나오면 다음 패키지를 설치합니다.

```bash
sudo apt update
sudo apt install python3-venv
```

## 설치 방법

### 1. 프로젝트 폴더로 이동

```bash
cd /home/kca/myprojects/100_chroma
pwd
ls
```

### 2. 가상환경 생성

```bash
python -m venv .venv
```

### 3. 가상환경 활성화

```bash
source .venv/bin/activate
```

활성화되면 터미널 앞에 보통 `(.venv)`가 표시됩니다. 다음 명령으로 현재
가상환경의 Python을 사용하는지 확인할 수 있습니다.

```bash
which python
```

### 4. 패키지 설치

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

설치되는 주요 패키지는 다음과 같습니다.

- `chromadb`: 벡터 데이터베이스
- `pandas`: 조회 결과와 HTML 표 생성
- `streamlit`: 웹 기반 ChromaDB 뷰어

설치 결과를 확인합니다.

```bash
python -c "import chromadb, pandas, streamlit; print('패키지 준비 완료')"
```

## 실행 순서

### 1. 테스트 데이터 생성 및 검색

```bash
python 10_chroma_basic_test.py
```

처음 실행하면 프로젝트 안에 `chroma_db/` 폴더가 생성되고 테스트 문서 3개가
저장됩니다. 최초 의미 검색 시 임베딩 모델을 내려받느라 시간이 걸릴 수 있습니다.

현재 스크립트는 고정된 문서 ID를 `add()`하므로, 같은 DB에 다시 실행하면 이미
존재하는 ID에 관한 경고나 오류가 발생할 수 있습니다.

### 2. HTML 보고서 생성

```bash
python 20_view.py
```

프로젝트 폴더에 다음 형식의 파일이 생성됩니다.

```text
chroma_export_my_first_collection_날짜시간.html
```

생성된 파일을 확인합니다.

```bash
ls chroma_export_*.html
```

### 3. Streamlit 뷰어 실행

```bash
streamlit run 21_chroma_viewer.py
```

터미널에 표시되는 `http://localhost:8501` 주소를 웹 브라우저에서 엽니다.
서버를 종료하려면 실행 중인 터미널에서 `Ctrl+C`를 누릅니다.

## 작업 종료

가상환경을 종료합니다.

```bash
deactivate
```

다음에 다시 작업할 때는 프로젝트 폴더에서 가상환경만 다시 활성화하면 됩니다.

```bash
cd /home/kca/myprojects/100_chroma
source .venv/bin/activate
```

## 데이터와 생성 파일

- ChromaDB 데이터: `chroma_db/`
- HTML 보고서: `chroma_export_*.html`
- Python 가상환경: `.venv/`

위 파일과 폴더는 `.gitignore`에 등록되어 Git에 포함되지 않습니다.
