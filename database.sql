CREATE DATABASE election_system;
USE election_system;

-- Voter Table
CREATE TABLE voter_info (
    voter_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(50),
    password VARCHAR(50)
);

-- Candidate Table
CREATE TABLE candidate_info (
    candidate_id INT AUTO_INCREMENT PRIMARY KEY,
    candidate_name VARCHAR(50)
);

-- Vote Table
CREATE TABLE vote_records (
    vote_id INT AUTO_INCREMENT PRIMARY KEY,
    voter_id INT,
    candidate_id INT,
    FOREIGN KEY (voter_id) REFERENCES voter_info(voter_id),
    FOREIGN KEY (candidate_id) REFERENCES candidate_info(candidate_id)
);

-- Insert Candidates
INSERT INTO candidate_info(candidate_name) 
VALUES ('Ram'), ('Sham'), ('Tukaram');

SELECT * FROM voter_info;

SELECT * FROM vote_records;

SELECT c.candidate_name, COUNT(v.vote_id)
FROM candidate_info c
LEFT JOIN vote_records v ON c.candidate_id = v.candidate_id
GROUP BY c.candidate_id;
