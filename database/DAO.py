from database.DB_connect import DBConnect
from model.country import  Country

class DAO():
    def getNodes(self, year):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary = True)
        res = []

        query = """select distinct(state1no), state1ab,c.StateNme
                    from country c, contiguity
                    where state1no = c.CCode and year <= %s
                            """

        cursor.execute(query, (year, ))

        for row in cursor:
            res.append(Country(row['StateNme'], row['state1ab'], row['state1no']))

        cursor.close()
        conn.close()
        return res

    def getEdges(self, year):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        res = []

        query = """select distinct state1no, state2no
                    from contiguity
                    where year<=%s and state1no <state2no and conttype = 1
                                   """

        cursor.execute(query, (year, ))

        for row in cursor:
            res.append((row["state1no"], row["state2no"]))

        cursor.close()
        conn.close()
        return res

    def getEdges2006(self):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        res = []

        query = """select distinct state1no, state2no
                    from contiguity2006
                    where state1no <state2no and conttype = 1
                                   """

        cursor.execute(query)

        for row in cursor:
            res.append((row["state1no"], row["state2no"]))

        cursor.close()
        conn.close()
        return res

    def getStati(self):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        res = []

        query = """select distinct StateNme
                            from country
                """

        cursor.execute(query)

        for row in cursor:
            res.append(row['StateNme'])

        cursor.close()
        conn.close()
        return res

