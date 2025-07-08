from dotenv import load_dotenv
from fastapi import FastAPI

app = FastAPI(
    title="Logistic App",
    description="backend untuk aplikasi logistik barang (pencatatan, pelacakan, dan pengelolaan)",
    version="1.0.0"
)

#default
@app.get("/")
async def health_check():
    return {"status": "ok"}
