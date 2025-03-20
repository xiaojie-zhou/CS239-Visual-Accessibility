# Try it out
# Hosted and Deployed
## 👉 [ColorSense](https://xiaojie-zhou.github.io/ColorSense/)
### for the source code of the deployed version, see the [render](https://github.com/xiaojie-zhou/CS239-Visual-Accessibility/tree/render) branch
# Local Development 

## Using Docker (recommended)

```bash
docker compose up
```

## Or, Manual Installation
Open **two** terminals for backend and frontend
## Backend
Assuming python 3.12 is already installed

Use virtual environment
### Installation

```
cd Prototype/backend
python3.12 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

### Running
```
python app.py
```
Ideally, the backend should be running on http://localhost:5001 

*may take a while for the first time*
#### Unless error, skip to the frontend section to run the frontend.

If there is an error, make sure you are using the venv environment by checking python and flask paths:
```
which python
which flask
which pip
```
The output should be the path to the .venv folder. 

If it points to anaconda or system python/flask, you can activate the environment by running:
```
conda deactivate
```
## Frontend
Assuming [Node.js](https://nodejs.org/en) is installed, also using virtual environment

### Installation

**Create a .env file in the frontend folder with the following content:**
VITE_API_URL=http://127.0.0.1:5001

Then run:
```
cd Prototype/frontend
python3.12 -m venv .venv
. .venv/bin/activate
npm install
```

### Running
```
npm run dev
```
