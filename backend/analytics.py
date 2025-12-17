from backend.db import get_connections

def top_skills(limit = 10):
    conn = get_connections()
    cursor = conn.cursor()

    query = """
    SELECT skills, COUNT(*) as count
    from jobs
    WHERE skills IS NOT NULL AND skills != ""
    GROUP BY skills
    ORDER BY count DESC
    limit %s
    """

    cursor.execute(query, (limit,))
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return [{"skills":row[0], "count":row[1]} for row in data]

def jobs_by_location(limit = 10):
    conn = get_connections()
    cursor = conn.cursor()
    query = """
    SELECT location, COUNT(*) as total_jobs
    FROM jobs
    GROUP BY location
    ORDER BY total_jobs DESC
    LIMIT %s
    """
    cursor.execute(query, (limit,))
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return [{"location":row[0], "count":row[1]} for row in data]

def hiring_companies(limit=10):
    conn = get_connections()
    cursor = conn.cursor()

    query = """
    SELECT company, COUNT(*) AS count
    FROM jobs
    GROUP BY company
    ORDER BY count DESC
    limit %s
    """
    cursor.execute(query, (limit,))
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return [{"company":row[0], "count":row[1]} for row in data]

def get_jobs(page = 1, limit = 10, role=None, location = None, skill= None):
    offset = (page-1)*limit
    conn = get_connections()
    cursor = conn.cursor(dictionary=True)

    base_query = " SELECT * FROM jobs WHERE 1=1"
    params = []

    if role:
        base_query += " AND title LIKE %s"
        params.append(f"%{role}%")
    if location:
        base_query += " AND location LIKE %s"
        params.append(f"%{location}%")
    if skill:
        base_query += " AND skills LIKE %s"
        params.append(f"%{skill}%")

    base_query += " ORDER BY scraped_at DESC LIMIT %s OFFSET %s"
    params.extend([limit, offset])

    cursor.execute(base_query, tuple(params))
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result