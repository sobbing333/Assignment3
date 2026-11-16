-- Creates the students table used by the app

-- Create students table
CREATE TABLE students (
    -- Student ID
    -- Automatic and Incrementing
    student_id SERIAL PRIMARY KEY,

    -- Students first name
    -- Required
    first_name TEXT NOT NULL,

    -- Students last name
    -- Required
    last_name TEXT NOT NULL,

    -- Students contact email
    -- Required and Unique
    email TEXT NOT NULL UNIQUE,

    -- Enrolment date of student
    -- Optional
    enrollment_date DATE
);
