from django.db import connection

def resolve_all_branch(input):
    query = """
        SELECT 
            b.id AS bank_id,
            b.name AS bank_name,
            br.id AS branch_id,
            br.branch AS branch_name,
            br.ifsc AS branch_ifsc
        FROM branch_branch AS br
        JOIN banks_bank AS b ON br.bank_id = b.id
    """

    filters = []
    params = []
    if input:
        for key, value in input.items():
            if isinstance(value, list):
                placeholders = ", ".join(["%s"] * len(value))
                filters.append(f"br.{key} IN ({placeholders})")
                params.extend(value)
            else:
                filters.append(f"br.{key} = %s")
                params.append(value)

        query += " WHERE " + " AND ".join(filters)

    with connection.cursor() as cursor:
        cursor.execute(query, params)
        rows = cursor.fetchall()
    return [
        {
            "branch_id": row[2],
            "branch_name": row[3],
            "branch_ifsc": row[4],
            "bank": {
                "bank_id": row[0],
                "bank_name": row[1],
            }
        }
        for row in rows
    ]
