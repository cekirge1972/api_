from fastapi import FastAPI

app = FastAPI()
val = None

@app.get("/status")
async def check():
    return {"val": val}

@app.get("/start")
async def start():
    global val
    val = True
    return {"Answer": f"Command Sent!"}

@app.get("/reset")
async def reset():
    global val
    val = None
    return {"Answer": f"Value is now {val}"}

@app.get("/stop")
async def reset():
    global val
    val = False
    return {"Answer": f"Value is now {val}"}

if __name__ == "__main__":
    import uvicorn
    
    # Run the FastAPI app using Uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000,reload=True)
