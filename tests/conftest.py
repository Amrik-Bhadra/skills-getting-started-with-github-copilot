import copy
import pytest
from fastapi.testclient import TestClient
from src.app import app, activities


@pytest.fixture
def client():
    """Create a TestClient for the FastAPI app"""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset activities to initial state before each test"""
    # Store original state
    original = {
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
        },
        "Programming Class": {
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
        },
        "Gym Class": {
            "description": "Physical education and sports activities",
            "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
            "max_participants": 30,
            "participants": ["john@mergington.edu", "olivia@mergington.edu"]
        },
        "Basketball Team": {
            "description": "Team-based basketball practices and games",
            "schedule": "Mondays and Thursdays, 4:00 PM - 5:30 PM",
            "max_participants": 15,
            "participants": ["aaron@mergington.edu", "lisa@mergington.edu"]
        },
        "Swimming Club": {
            "description": "Improve swimming skills and participate in meets",
            "schedule": "Tuesdays and Fridays, 3:45 PM - 5:00 PM",
            "max_participants": 18,
            "participants": ["natalie@mergington.edu", "ryan@mergington.edu"]
        },
        "Art Club": {
            "description": "Explore drawing, painting, and mixed media art projects",
            "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
            "max_participants": 20,
            "participants": ["sophia@mergington.edu", "isabella@mergington.edu"]
        },
        "Drama Society": {
            "description": "Rehearse and perform plays, musicals, and improv exercises",
            "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
            "max_participants": 25,
            "participants": ["maria@mergington.edu", "james@mergington.edu"]
        },
        "Science Olympiad": {
            "description": "Prepare for science competitions and work on STEM challenges",
            "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
            "max_participants": 20,
            "participants": ["oliver@mergington.edu", "mia@mergington.edu"]
        },
        "Debate Team": {
            "description": "Develop argumentative skills and compete in debate tournaments",
            "schedule": "Fridays, 4:00 PM - 5:30 PM",
            "max_participants": 16,
            "participants": ["jack@mergington.edu", "lily@mergington.edu"]
        }
    }
    
    # Clear current activities and restore original state
    activities.clear()
    activities.update(copy.deepcopy(original))
    
    yield
    
    # Reset after test
    activities.clear()
    activities.update(copy.deepcopy(original))
