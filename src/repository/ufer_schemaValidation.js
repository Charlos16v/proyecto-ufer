db.createCollection("ufer_services", {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            required: [ "name", "description", "price", ],
            properties: {
                name: {
                    bsonType: "string",
                    description: "must be a string and is required",
                },
                description: {
                    bsonType: "string",
                    description: "must be a string and is required",
                },
                price: {
                    bsonType: "int",
                    description: "must be an integer and is required",
                },
            }
        }
    }
})