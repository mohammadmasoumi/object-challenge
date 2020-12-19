echo setup.sh time now: `date +"%T" `

mongo --host localhost:270217 <<EOF
    use admin;
   db.auth("root","1234");
   use challenge;
   db.createUser(
      {
        user: "challenge",
        pwd: "challenge",
        roles: [
           { role: "dbOwner", db: "data_server" }
        ]
      }
   );
EOF
