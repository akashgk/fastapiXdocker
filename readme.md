# Steps to run the project (Mac)

## steps to run Fast Api on local.

1. create a virtual env`python3 -m venv myenv`. `myenv` will be the name of the virtual env.
2. Activate the virtual env `source myenv/bin/activate`.
3. Install the dependencies from `requirements.txt` using `pip install -r requirements.txt`
4. run `uvicorn main:app --reload`.
5. Open browser and open url: `http://127.0.0.1:8000`.
6. Open url: `http://127.0.0.1:8000/docs` for swagger docs or `http://127.0.0.1:8000/redoc` for redoc docs.
7. Make changes and the app will reload itself.
8. run `deactivate` to stop the virtual env.

## Running on docker

- run the command `docker compose up --build`
