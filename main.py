##Cell 1: Install + Connect
!pip install mysql-connector-python

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",   # your MySQL password
    database="election_system"
)

cursor = db.cursor()
print("Connected to MySQL")


##Cell 2: Register Multiple Voters
n = int(input("Enter number of voters: "))

voter_ids = []

for i in range(n):
    print(f"\nVoter {i+1}")
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    password = input("Enter Password: ")

    cursor.execute(
        "INSERT INTO voter_info(name,email,password) VALUES (%s,%s,%s)",
        (name, email, password)
    )
    db.commit()

    voter_ids.append(cursor.lastrowid)
    print("Voter Registered")

print("\nAll voters registered!\n")


##Cell 3: Show Candidates
cursor.execute("SELECT * FROM candidate_info")
candidates = cursor.fetchall()

print("Candidates:")
for c in candidates:
    print(f"{c[0]} : {c[1]}")


##Cell 4: Voting
for vid in voter_ids:
    print(f"\nVoter ID {vid} voting:")

    choice = int(input("Enter Candidate ID: "))

    # Check if already voted
    cursor.execute("SELECT * FROM vote_records WHERE voter_id=%s", (vid,))
    if cursor.fetchone():
        print("Already voted!")
    else:
        cursor.execute(
            "INSERT INTO vote_records(voter_id,candidate_id) VALUES (%s,%s)",
            (vid, choice)
        )
        db.commit()

        print("Vote Cast")

  
##Cell 5: Show Results
      cursor.execute("""
SELECT c.candidate_name, COUNT(v.vote_id)
FROM candidate_info c
LEFT JOIN vote_records v ON c.candidate_id = v.candidate_id
GROUP BY c.candidate_id
""")

results = cursor.fetchall()

print("\n Election Results:")
for r in results:
    print(f"{r[0]} : {r[1]} votes")

db.close()
