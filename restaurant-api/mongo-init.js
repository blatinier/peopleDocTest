db.createUser(
    {
        user: "restaurant",
        pwd: "strong_dev_password",
        roles: [
            {
                role: "readWrite",
                db: "restaurant_backend"
            }
        ]
    }
);
