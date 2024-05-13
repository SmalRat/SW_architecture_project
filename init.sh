#!/usr/bin/env bash
docker compose up -d
sleep 5
docker exec -it mongo1 mongosh --eval '
rs.initiate({
    _id: "rs0",
    members: [
        {_id: 0, host: "mongo1:27017", priority: 1},
        {_id: 1, host: "mongo2:27017", priority: 0},
        {_id: 2, host: "mongo3:27017", priority: 0}
    ]
});
'
sleep 5
