from DBManager import DBManager

db_manager = DBManager("kakut.db")
db_manager.create_tables()
#db_manager.add_quiz(2, #"Гнида Євген Главович", #"Unknown details!404")
#print(db_manager.get_quiz())

db_manager.add_que(1, 2, "Летять два попугая, перший - зелений, другий - на південь. Скільки буде коштувати кг сухих яблук, якщо відрізати кусок льону.")
print(db_manager.get_que(1))

db_manager.add_opt(3, 1, "Вчора")
print(db_manager.get_options(1))