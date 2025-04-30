from app import App
from sanic import Sanic
from sanic import response

app = App()
sanic = Sanic("AssistantAPI")

@sanic.get("/")
async def index(request):
    return response.json({"status": "ok"})

@sanic.post("/send_message")
async def send_message(request):
    message = request.json
    if not message:
        return response.json({"error": "No message provided"}, status=400)

    response_message = app.entities_context.send_message(message)
    return response.json(response_message)

if __name__ == "__main__":
    sanic.run(host="0.0.0.0", port=8000, debug=False)