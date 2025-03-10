# Get Started
### Open two terminals for frontend and backend
for macOS/linux

process for windows should be similar 
## Backend
Assuming python 3.12 is already installed

Use virtual environment
### Installation
makefile is provided for easy installation:

```make backend```
or
```
cd backend
python3.12 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

flask --app app run
```

## Frontend
Assuming [Node.js](https://nodejs.org/en) is installed

cd into the frontend folder

install packages and dependencies

```
cd frontend
python3.12 -m venv .venv
. .venv/bin/activate
npm install
```

## Running
```
npm run dev
```
