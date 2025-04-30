from app import App
from helper import Helper

if __name__ ==  "__main__":
    app = App()
    while True:
        print ("\n" + "." * 40)
        m = input("> ")
        if m.lower() == "exit":
            break

        message = {
            "success": True,
            "source_id": app.user.entity_id,
            "destination_id": app.user.assistant_entity_id,
            "message": [m],
            "timestamp": Helper.get_timestamp()
        }

        response = app.entities_context.send_message(message)
        print ("\n" + "-" * 20 + "\n Talos \n" + "-" * 20)
        if response["success"]:                
            print("\n".join(response["message"]))
        else:
            print(response)
        print ("-" * 20)