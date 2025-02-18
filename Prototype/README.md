# Installation
for macOS/linux

process for windows should be similar 
## Backend
Assuming python is already installed

Use virtual environment if you want to

cd into the backend folder

install requirements.txt

```
cd backend
python3.12 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

## Frontend
Assuming Node.js is installed

cd into the frontend folder

install packages and dependencies

```
cd frontend
python3.12 -m venv .venv
. .venv/bin/activate
npm install
```

# Start Using
Start two terminals 

## Backend

```
cd backend
# . .venv/bin/activate
flask --app app run
```

## Frontend

```
cd frontend
# . .venv/bin/activate
npm run dev
```

