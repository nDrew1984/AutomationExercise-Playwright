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