## simple notes to get started

- front end in react using next.js (for typescript) and tailwind css
- backend using python and fastapi
- both will be run from a single docker container with fastAPI serving the static react SPA

### structure ###

mvp-app/
├── frontend/                    # Next.js app (React SPA)
│   ├── components/
│   ├── pages/
│   ├── public/
│   ├── styles/
│   ├── package.json
│   └── ...
├── backend/                     # FastAPI app
│   ├── app/
│   │   ├── api/
│   │   ├── static/              # Static site files from Next.js export
│   │   └── main.py
│   ├── requirements.txt
├── Dockerfile                   # Combines frontend + backend
├── .gitignore
└── README.md


### frontend ###

- initialise
npx create-next-app@latest frontend --typescript
cd frontend

- Install Tailwind CSS + build tools
npm install -D tailwindcss postcss autoprefixer

- this breaks and you have to create and edit
npx tailwindcss init -p

- fix
npm install -D @tailwindcss/postcss
and edit postcss.config.js
export default {
  plugins: {
    "@tailwindcss/postcss": {},
    autoprefixer: {},
  },
}


- to run front end in dev more npm run dev


### backend ###

- setup venev
cd backend
python -m venv venv
source venv/bin/activate  # or .\\venv\\Scripts\\activate on Windows
pip install fastapi uvicorn
pip freeze > requirements.txt


uvicorn main:app --reload --port 8000



### Docker ###
docker build -t mvp:latest .
docker run -p 8080:8080 mmvp:latest

docker build --no-chache -t mvp .
docker run -p 8080:8080 mvp



gcloud auth login
gcloud config set project mvp-app-459119


gcloud builds submit --tag us-central1-docker.pkg.dev/mvp-app-459119/my-repo/mvp .



docker build -t gcr.io/mvp-app-459119/mvp .
docker push gcr.io/mvp-app-459119/mvp

gcloud run deploy mvp \
  --image gcr.io/mvp-app-459119/mvp \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated


gcloud builds submit --tag us-central1-docker.pkg.dev/mvp-app-459119/my-repo/mvp .

gcloud run deploy mvp-app --image us-central1-docker.pkg.dev/mvp-app-459119/my-repo/mvp --platform managed --region us-central1 --allow-unauthenticated

deploy service

gcloud run domain-mappings create --service mvp-app --region us-central1 --domain mvp.dilly.cloud