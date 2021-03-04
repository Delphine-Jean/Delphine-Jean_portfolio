import pytest 

def test():
 
    # Arrange
    def add(a,b):
        return a + b
    
    # Act
    result = add(1,1)
    # Assert
    assert result == [2]