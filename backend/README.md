# Ody

# mac에서 poetry 설치 명령어 (터미널에 입력)

curl -sSL https://install.python-poetry.org | python3 -

# window(powershell)에서 poetry 설치

(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -

### poetry 설치 확인

poetry --version

### 깃 클론 후 터미널에 아래 명령어 입력으로 필요 패키지 설치하기

poetry install

### 장고가 가상환경에 설치되었기 때문에 가상환경에 들어가서 작업해야 함

poetry shell

