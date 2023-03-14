import sys
from model.db_users import *
from view.login import *
from view.ventana_dos_login import*
import time 

class MiApp(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow() 
		self.ui.setupUi(self)
		# delete bar
		self.setWindowFlag(Qt.FramelessWindowHint)
		# transparent
		self.setAttribute(Qt.WA_TranslucentBackground)

		self.ui.bt_ingresar.clicked.connect(self.iniciar_sesion)

	def iniciar_sesion(self):
		self.ui.contrasena_incorrecta.setText('')
		self.ui.usuario_incorrecto.setText('')
		users_entry = self.ui.users.text()
		password_entry = self.ui.password.text()

		if users_entry == '' and password_entry == '': 
			self.ui.usuario_incorrecto.setText('Tipear Usuario')
			self.ui.contrasena_incorrecta.setText('Tipear Usuario')

		elif users_entry not in list_user:
			self.ui.usuario_incorrecto.setText('Tipear Usuario Válido')
			self.ui.contrasena_incorrecta.setText('Tipear Usuario Válido')

		elif users_entry in list_user and password_entry != dict_user[users_entry]:
			self.ui.usuario_incorrecto.setText('')
			self.ui.contrasena_incorrecta.setText('Tipear Contraseña Válida')
	
		elif users_entry in list_user and password_entry == dict_user[users_entry]:
			for i in range(0,99):
				time.sleep(0.02)
				self.ui.progressBar.setValue(i)
				self.ui.cargando.setText('Cargando...')

			self.hide()
			self.ventana = Ventana_dos()
			self.ventana.show()
		else:
			self.ui.contrasena_incorrecta.setText(' Error ')
			self.ui.usuario_incorrecto.setText(' Error ')


class Ventana_dos(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ventana = Ui_VentanaDos() 
		self.ventana.setupUi(self)

if __name__ == "__main__":
     app = QApplication(sys.argv)
     mi_app = MiApp()
     mi_app.show()
     sys.exit(app.exec_())	