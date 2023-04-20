import psycopg2


class DataModel:
    def __init__(self, db_url):
        self.connection = None
        self.db_url = db_url
        try:
            self.connection = psycopg2.connect(db_url)
            print("Successfully connected to the database")
        except Exception as e:
            print(e)

    def read(self, id):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT * FROM predictions WHERE enrollee_id = {id}")
        result = cursor.fetchone()
        cursor.close()
        return result

    def read_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM predictions")
        results = cursor.fetchall()
        cursor.close()
        return results

    def write(self, features, prediction):
        cursor = self.connection.cursor()
        insert_query = f"INSERT INTO predictions (enrollee_id, city, city_development_index, gender, relevent_experience, enrolled_university, education_level, major_discipline, experience, company_size, prediction, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW())"
        cursor.execute(insert_query, (*features, prediction))
        self.connection.commit()
        cursor.close()

    def remove(self, id):
        cursor = self.connection.cursor()
        delete_query = f"DELETE FROM predictions WHERE enrollee_id = {id}"
        cursor.execute(delete_query)
        self.connection.commit()
        cursor.close()


if __name__ == '__main__':
    db_url = "postgresql://postgres:1234@localhost:5432/Hr_Job_Change"
    connection = DataModel(db_url)