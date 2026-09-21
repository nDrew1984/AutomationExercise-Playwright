PRODUCTS_LIST_SCHEMA = {
    "type": "object",
    "properties": {
        "responseCode": {"type": "number"},
        "products": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["id", "name", "price", "brand"]
            }
        }
    },
    "required": ["responseCode", "products"]
}

BRANDS_LIST_SCHEMA = {
    "type": "object",
    "properties": {
        "responseCode": {"type": "number"},
        "brands": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["id", "brand"]
            }
        }
    },
    "required": ["responseCode", "brands"]
}

RESPONSE_CODE_MESSAGE_SCHEMA = {
    "type": "object",
    "properties": {
        "responseCode": {"type": "number"},
        "message": {"type": "string"}
    },
    "required": ["responseCode", "message"]
}

READ_ACCOUNT_SCHEMA = {
    "type": "object",
    "properties": {
        "responseCode": {"type": "number"},
        "user": {
            "type": "object",
            "required": [
                "id", 
                "name", 
                "email", 
                "title", 
                "birth_day", 
                "birth_month", 
                "birth_year", 
                "first_name", 
                "last_name", 
                "company", 
                "address1", 
                "address2", 
                "country", 
                "state", 
                "city", 
                "zipcode"
            ]  
        }
    },
    "required": ["responseCode", "user"]
}

UPDATED_ACCOUNT_SCHEMA = {
    "type": "object",
    "properties": {
        "responseCode": {"type": "number"},
        "message": {"type": "string"}
    },
    "required": ["responseCode", "message"]
}
