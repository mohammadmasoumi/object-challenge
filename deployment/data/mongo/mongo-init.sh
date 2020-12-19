mongo <<EOF
   use admin;
   db.auth("root", "1234");
   use challenge;
   db.createUser(
      {
        user: "challenge",
        pwd: "challenge",
        roles: [
           { role: "dbOwner", db: "challenge" }
        ]
      }
   );
EOF
