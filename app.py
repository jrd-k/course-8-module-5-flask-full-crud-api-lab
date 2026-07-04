from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

def find_event(event_id):
    """Helper to look up an event by id. Returns the Event or None."""
    for event in events:
        if event.id == event_id:
            return event
        return None
# TODO: Task 1 - Define the Problem
# Create a new event from JSON input
@app.route("/")
def index():
    return jsonify({"message":"Welcome to the Events API"})

@app.route("/events",methods=["GET"])
def get_events():
    return jsonify([event.to_dict() for event in events]), 200

@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()
    # TODO: Task 2 - Design and Develop the Code

    # TODO: Task 3 - Implement the Loop and Process Each Element

    # TODO: Task 4 - Return and Handle Results
    pass
    if not data or "title" not in data:
        return jsonify({"error": "Missing required field: title"}), 400
    
    new_id = max((event.id for event in events), default=0) + 1
    new_event = Event(new_id, data["title"])
    events.append(new_event)

    return jsonify(new_event.to_dict()), 201

# TODO: Task 1 - Define the Problem
# Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    event = find_event(event_id)
     
    if event is None:
        return jsonify({"error":f"Event with id{event_id} not found"}), 404
    
    data =request.get_json()

    if not data or "title" not in data:
        return jsonify({"error":"Missing required field: title"}), 400
    
    event.title = data["title"]

    return jsonify(event.to_dict()), 200
    # TODO: Task 2 - Design and Develop the Code

    # TODO: Task 3 - Implement the Loop and Process Each Element

    # TODO: Task 4 - Return and Handle Results
    pass

# TODO: Task 1 - Define the Problem
# Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    # TODO: Task 2 - Design and Develop the Code

    # TODO: Task 3 - Implement the Loop and Process Each Element

    # TODO: Task 4 - Return and Handle Results
    pass

if __name__ == "__main__":
    app.run(debug=True)
