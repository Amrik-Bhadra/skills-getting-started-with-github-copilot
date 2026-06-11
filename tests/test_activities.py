def test_get_all_activities(client):
    """Test retrieving all activities"""
    # Arrange
    expected_activities = [
        "Chess Club",
        "Programming Class",
        "Gym Class",
        "Basketball Team",
        "Swimming Club",
        "Art Club",
        "Drama Society",
        "Science Olympiad",
        "Debate Team"
    ]
    
    # Act
    response = client.get("/activities")
    data = response.json()
    
    # Assert
    assert response.status_code == 200
    assert set(data.keys()) == set(expected_activities)


def test_activity_contains_required_fields(client):
    """Test that each activity contains required fields"""
    # Arrange & Act
    response = client.get("/activities")
    data = response.json()
    
    # Assert
    activity = data["Chess Club"]
    assert "description" in activity
    assert "schedule" in activity
    assert "max_participants" in activity
    assert "participants" in activity


def test_activities_contain_participant_details(client):
    """Test that activities include participant information"""
    # Arrange & Act
    response = client.get("/activities")
    data = response.json()
    
    # Assert
    assert "michael@mergington.edu" in data["Chess Club"]["participants"]
    assert "daniel@mergington.edu" in data["Chess Club"]["participants"]
    assert len(data["Chess Club"]["participants"]) == 2


def test_activity_max_participants(client):
    """Test that max_participants is correctly returned"""
    # Arrange & Act
    response = client.get("/activities")
    data = response.json()
    
    # Assert
    assert data["Chess Club"]["max_participants"] == 12
    assert data["Programming Class"]["max_participants"] == 20
    assert data["Gym Class"]["max_participants"] == 30
