from app import App as app

@app.get("/")
def main():
    return {
        "status": True,
        "resCode": 200,
        "message": "Hello, how are you?"
    }