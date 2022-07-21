import sqlite3


conexao = sqlite3.connect('atlas.sqlite')
c = conexao.cursor()

c.execute('''ALTER TABLE users ALTER id PRIMARY KEY, AUTOINCREMENT

''')
#c.execute(" INSERT INTO usuarios (nome, user, password, email) VALUES ('teste', 'teste', '1234', 'magno@atlas.com')")
# c.execute('''UPDATE users SET user = 'colab' WHERE id = 1''')
# c.execute('''UPDATE users SET password = 'colab' WHERE id = 1''')
# c.execute('''UPDATE users SET rank = 0 WHERE id = 1''')
# c.execute('''UPDATE users SET email = 'colab@atlas.io' WHERE id = 1''')
# c.execute('''UPDATE users SET cargo = 'colab' WHERE id = 1''')
# c.execute('''UPDATE users SET active = 0 WHERE id = 1''')
conexao.commit()
conexao.close()