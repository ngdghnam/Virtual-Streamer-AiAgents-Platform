from typing import Optional
import json

# Option 1: Inherit from dict and properly initialize it
class HttpResponse(dict):
    def __init__(self, message: str, statusCode: int, data: Optional[dict] = None):
        # Initialize the dict with the response data
        super().__init__({
            'message': message,
            'statusCode': statusCode,
            'data': data
        })
        # Also store as instance attributes for easy access
        self.message = message
        self.statusCode = statusCode
        self.data = data
    
    def __str__(self):
        return f"message='{self.message}', statusCode={self.statusCode}, data={self.data}"
    
    def to_json(self):
        """Convert to JSON string"""
        return json.dumps(self)
    
httpResponse = HttpResponse("success", 122).to_json()
print(httpResponse)