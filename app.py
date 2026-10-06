import sqlite3

base = "centro.db"

def conectar():
    return sqlite3.connect(base)

def crear_tablas():
    conn = conectar()
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS cursos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            duracion TEXT NOT NULL,
            precio REAL NOT NULL
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS alumnos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            ci TEXT NOT NULL,
            curso_id INTEGER,
            FOREIGN KEY (curso_id) REFERENCES cursos(id)
        )
    """)

    conn.commit()
    conn.close()
    print("Tablas creadas")

def agregar_curso(nombre, tiempo, costo):
    conn = conectar()
    c = conn.cursor()
    c.execute("INSERT INTO cursos VALUES (NULL, ?, ?, ?)", (nombre, tiempo, costo))
    conn.commit()
    conn.close()
    print("Curso agregado:", nombre)

def agregar_alumno(nombre, ci, curso):
    conn = conectar()
    c = conn.cursor()
    c.execute("INSERT INTO alumnos VALUES (NULL, ?, ?, ?)", (nombre, ci, curso))
    conn.commit()
    conn.close()
    print("Alumno agregado:", nombre)

def ver_cursos():
    conn = conectar()
    c = conn.cursor()
    c.execute("SELECT * FROM cursos")
    lista = c.fetchall()
    conn.close()
    print("\n--- Cursos Disponibles ---")
    for fila in lista:
        print(fila[0], "-", fila[1], "-", fila[2], "- Bs", fila[3])
    return lista

def ver_alumnos():
    conn = conectar()
    c = conn.cursor()
    c.execute("""
        SELECT a.nombre, a.ci, c.nombre
        FROM alumnos a LEFT JOIN cursos c ON a.curso_id = c.id
    """)
    lista = c.fetchall()
    conn.close()
    print("\n--- Lista de Alumnos ---")
    for fila in lista:
        print(fila[0], "- CI:", fila[1], "- Curso:", fila[2])
    return lista

if __name__ == "__main__":
    print("=== Centro de Capacitacion ===")
    
    crear_tablas()

    agregar_curso("Python Basico", "2 meses", 650)
    agregar_curso("Ingles", "4 meses", 800)
    agregar_curso("Diseno", "1.5 meses", 500)

    agregar_alumno("Vidal Ovidio Quispe", "98765432", 1)
    agregar_alumno("Ana Flores", "11223344", 2)

    ver_cursos()
    ver_alumnos()

    print("\nTodo listo")