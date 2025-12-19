from fastapi import FastAPI

app = FastAPI(
    title="La Semilla Dorada API",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

#Para ejecutar la aplicación, use el siguiente comando:
# uvicorn app.main:app --reload