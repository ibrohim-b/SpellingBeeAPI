#kill previous process
pkill SpellingBeeBot
#Activate venv
source .venv/bin/activate
#Install dependencies
python3 -m pip install --upgrade pip
if  [ -f requirements.txt ]; then pip install -r /home/python-projects/SpellingBeeTelegramBot/requirements.txt; fi
#Launch main:app with nohup
nohup "$(uvicorn main:app --host 159.223.180.158 --port 8000 >/dev/null 2>&1 &)"