def test_root_redirect(client):
    """Test that root path redirects to index.html"""
    # Arrange & Act
    response = client.get("/", follow_redirects=True)
    
    # Assert
    assert response.status_code == 200


def test_root_redirect_location(client):
    """Test that root path redirects to correct location"""
    # Arrange & Act
    response = client.get("/", follow_redirects=False)
    
    # Assert
    assert response.status_code == 307
    assert "/static/index.html" in response.headers.get("location", "")
