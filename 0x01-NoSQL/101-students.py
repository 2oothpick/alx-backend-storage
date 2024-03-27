#!/usr/bin/env python3
"""
Task 14. Top students
"""


def top_students(mongo_collection):
    """
    shows top students
    """
    return mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])
