use admin

db.createUser({
    user: "admin",
    pwd: "a1.b2.c3*",
    roles: [ { role: "userAdminAnyDatabase", db: "admin" } ] }
)

use mydb

db.createUser({
    user: "user",
    pwd: "user**",
    roles: [ { role: "readWrite", db: "mydb" }]}
)

