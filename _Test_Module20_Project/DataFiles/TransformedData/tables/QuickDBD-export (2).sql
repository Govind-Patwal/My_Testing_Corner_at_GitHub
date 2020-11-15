-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "Hotel_Review" (
    "Review" varchar   NOT NULL,
    "Reviewer_Sentiment" varcahr   NOT NULL,
    CONSTRAINT "pk_Hotel_Review" PRIMARY KEY (
        "Review"
     )
);

