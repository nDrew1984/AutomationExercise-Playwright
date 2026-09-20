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
};
