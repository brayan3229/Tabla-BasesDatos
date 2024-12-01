import sqlite3
from metricas import Estudiante

conn = sqlite3.connect('Autoconocimient.db')
c = conn.cursor()





c.execute("""CREATE TABLE IF NOT EXISTS metricas (
    metric_id INTEGER PRIMARY KEY AUTOINCREMENT,
    plan_id INTEGER,
    metric_type TEXT, -- 'financial', 'time', 'impact'
    current_value DECIMAL(10,2),
    target_value DECIMAL(10,2),
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (plan_id) REFERENCES Autoconocimient(plan_id)
)
""")


c.execute("INSERT INTO metricas VALUES ('1234','financial', 500, 1000)" )
conn.commit()

c.execute("SELECT * FROM metricas")
metricas = c.fetchall()

print(metricas)


conn.close()