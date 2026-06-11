def test_signup_for_activity_success(client):
    """Test successful signup for an activity"""
    # Arrange
    activity = "Programming Class"
    email = "newstudent@mergington.edu"
    
    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")
    
    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up {email} for {activity}"
    
    # Verify participant was added
    activities_response = client.get("/activities")
    assert email in activities_response.json()[activity]["participants"]


def test_signup_multiple_students(client):
    """Test that multiple students can sign up for same activity"""
    # Arrange
    activity = "Gym Class"
    email1 = "student1@mergington.edu"
    email2 = "student2@mergington.edu"
    
    # Act
    response1 = client.post(f"/activities/{activity}/signup?email={email1}")
    response2 = client.post(f"/activities/{activity}/signup?email={email2}")
    
    # Assert
    assert response1.status_code == 200
    assert response2.status_code == 200
    
    activities_response = client.get("/activities")
    participants = activities_response.json()[activity]["participants"]
    assert email1 in participants
    assert email2 in participants


def test_signup_duplicate_registration(client):
    """Test that duplicate signup returns error"""
    # Arrange
    activity = "Chess Club"
    email = "michael@mergington.edu"  # Already registered
    
    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")
    
    # Assert
    assert response.status_code == 400
    assert "Already signed up" in response.json()["detail"]


def test_signup_activity_not_found(client):
    """Test signup for non-existent activity"""
    # Arrange
    activity = "Nonexistent Club"
    email = "student@mergington.edu"
    
    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")
    
    # Assert
    assert response.status_code == 404
    assert "Activity not found" in response.json()["detail"]


def test_signup_response_format(client):
    """Test that signup response has correct format"""
    # Arrange
    activity = "Art Club"
    email = "testuser@mergington.edu"
    
    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")
    data = response.json()
    
    # Assert
    assert "message" in data
    assert isinstance(data["message"], str)
