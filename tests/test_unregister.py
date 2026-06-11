def test_unregister_success(client):
    """Test successful unregistration from activity"""
    # Arrange
    activity = "Chess Club"
    email = "michael@mergington.edu"  # Already registered
    
    # Act
    response = client.delete(f"/activities/{activity}/unregister?email={email}")
    
    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Removed {email} from {activity}"
    
    # Verify participant was removed
    activities_response = client.get("/activities")
    assert email not in activities_response.json()[activity]["participants"]


def test_unregister_multiple_participants(client):
    """Test unregistering one participant from activity with multiple"""
    # Arrange
    activity = "Chess Club"
    email_to_remove = "michael@mergington.edu"
    email_to_keep = "daniel@mergington.edu"
    
    # Act
    response = client.delete(f"/activities/{activity}/unregister?email={email_to_remove}")
    
    # Assert
    assert response.status_code == 200
    
    activities_response = client.get("/activities")
    participants = activities_response.json()[activity]["participants"]
    assert email_to_remove not in participants
    assert email_to_keep in participants


def test_unregister_student_not_registered(client):
    """Test unregistration of non-registered student"""
    # Arrange
    activity = "Chess Club"
    email = "notregistered@mergington.edu"
    
    # Act
    response = client.delete(f"/activities/{activity}/unregister?email={email}")
    
    # Assert
    assert response.status_code == 400
    assert "not registered" in response.json()["detail"]


def test_unregister_activity_not_found(client):
    """Test unregistration from non-existent activity"""
    # Arrange
    activity = "Nonexistent Club"
    email = "student@mergington.edu"
    
    # Act
    response = client.delete(f"/activities/{activity}/unregister?email={email}")
    
    # Assert
    assert response.status_code == 404
    assert "Activity not found" in response.json()["detail"]


def test_unregister_response_format(client):
    """Test that unregister response has correct format"""
    # Arrange
    activity = "Programming Class"
    email = "emma@mergington.edu"
    
    # Act
    response = client.delete(f"/activities/{activity}/unregister?email={email}")
    data = response.json()
    
    # Assert
    assert "message" in data
    assert isinstance(data["message"], str)
    assert "Removed" in data["message"]
