import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QGridLayout,QMessageBox, QLabel, QPushButton,QLineEdit, QSpinBox,QComboBox,QHBoxLayout
from PyQt5 import uic
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from Test import *

class ventana_principal(QDialog):
    #método constructor de la clase
    def __init__(self):
        #iniciar objeto QDialog
        QDialog.__init__(self)
        #cargar la configuración del archivo .ui en el objeto
        uic.loadUi("principal.ui", self)
        
        self.city = Ciudad()
        self.departamentop=Departamento()
        self.marcaveh=Marca_vehiculo()
        self.modeloveh=Modelo_vehiculo()
       
        #self.btinsertar.clicked.connect(self.ciudad)
        #self.ventana_principal.setWindowTitle('BDTráfico')
        self.btSalir.clicked.connect(self.cancelar)
        #-----Combobox------------------------
        layout=QHBoxLayout()
        self.listadb=QComboBox()
        self.listadb.addItems(["Marca vehículo","Modelo vehículo", "vehículo","Agente","Persona","Infraccion","Ciudad","Departamento","Lugar de infracción"])
        layout.addWidget(self.listadb)
        self.setLayout(layout)
        self.listadb.currentIndexChanged.connect(self.SeleccionComboBox)
        self.btinsertar.clicked.connect(self.ir)
        self.var_aux = 0
    	
    def closeEvent(self,event):
      reply =QMessageBox.question(self, "Mensaje", "Seguro quiere salir", QMessageBox.Yes, QMessageBox.No)
   
      if reply == QMessageBox.Yes:
       event.accept()
      else: 
        event.ignore() 
	   
    def ciudad(self):
        self.city.exec_()
        
    def departamento(self):
        self.departamentop.exec_()
        
    def marcaV(self):
        self.marcaveh.exec_()
        
    def modeloV(self):
        self.modeloveh.exec_()
        
    
        
    def cancelar(self):
         self.close() #cierra la ventana
         
    #--- se crea la funcion que conecta listadb con el boton insertar-------
         
    def SeleccionComboBox(self,index):
        self.var_aux=index
        print (index)
            
    def ir(self):
           
           if self.var_aux == 6:
               self.ciudad()
           if self.var_aux == 7:
               self.departamento()
           if self.var_aux == 0:
               self.marcaV()
           if self.var_aux == 1:
               self.modeloV()
           
            
            
            
            
 

class Ciudad(QDialog):
     def __init__(self):
         QDialog.__init__(self)
         self.setWindowTitle("Ciudades") #Titulo
         self.resize(400,400) #Tamano inicial ventana
         self.setMinimumSize(400,400) #Tamano minimo
         uic.loadUi("ciudad.ui", self)
         #-------------Establecer conexion base de datos---------------
         self.trafico=QSqlDatabase.addDatabase('QMYSQL')
         self.trafico.setHostName("127.0.0.1")
         self.trafico.setDatabaseName("trafico")
         self.trafico.setUserName("root")
         self.trafico.setPassword("password")
         
         #--------Conectar botones------
         self.btninsertar.clicked.connect(self.insertar)
         self.btncancelar.clicked.connect(self.cancelar)
          

     def insertar(self):
         estado=self.trafico.open()
         if estado==False:
             QMessageBox.warning(self,"No se pudo abrir la base de datos", self.trafico.lastError().text(),QMessageBox.Discard) #se guardan los errores que saca
         else:
             id_ciudad=self.id_ciudad_persona.text()
             Nombre_ciudad=self.Nombre_ciudad_persona.text()
             sql_ciudad="INSERT INTO Ciudad(id_ciudad_persona,Nombre_ciudad_persona) VALUES(:id_ciudad_persona,:Nombre_ciudad_persona)"
             consulta_ciudad=QSqlQuery()
             consulta_ciudad.prepare(sql_ciudad)
             consulta_ciudad.bindValue(":id_ciudad_persona",id_ciudad)
             consulta_ciudad.bindValue(":Nombre_ciudad_persona",Nombre_ciudad)
             estado= consulta_ciudad.exec_()
             if estado==False:
                 QMessageBox.warning(self,"No se pudo realizar la consulta", self.trafico.lastError().text(),QMessageBox.Discard) #se guardan los errores que saca
             else:
                 QMessageBox.information(self," Correcto", " Se han insertado los datos correctamente !",QMessageBox.Discard)
             self.trafico.close()# se cierra la base de datos  



     def cancelar(self):
         self.close() #cierra la ventana
#---------------------------------------------------------------Nueva clase para la tabla Departamento--------------------------------------------------------
class Departamento(QDialog):
     def __init__(self):
         QDialog.__init__(self)
         self.setWindowTitle("Departamentos") #Titulo
         self.resize(400,400) #Tamano inicial ventana
         self.setMinimumSize(400,400) #Tamano minimo
         uic.loadUi("departamento.ui", self)
         #-------------Establecer conexion base de datos---------------
         self.traficoDep=QSqlDatabase.addDatabase('QMYSQL')
         self.traficoDep.setHostName("127.0.0.1")
         self.traficoDep.setDatabaseName("trafico")
         self.traficoDep.setUserName("root")
         self.traficoDep.setPassword("password")
         
         #--------Conectar botones------
         self.bttinsertar.clicked.connect(self.insertarD)
         self.bttcancelar.clicked.connect(self.cancelarD)
          

     def insertarD(self):
         estadoDep=self.traficoDep.open()
         if estadoDep==False:
             QMessageBox.warning(self,"No se pudo abrir la base de datos", self.traficoDep.lastError().text(),QMessageBox.Discard) #se guardan los errores que saca
         else:
             id_Departamento=self.id_departamento_persona.text()
             Nombre_departamento=self.Nombre_departamento_persona.text()
             sql_departamento="INSERT INTO Departamento(id_departamento_persona,Nombre_departamento_persona) VALUES(:id_departamento_persona,:Nombre_departamento_persona)"
             consulta_departamento=QSqlQuery()
             consulta_departamento.prepare(sql_departamento)
             consulta_departamento.bindValue(":id_departamento_persona",id_Departamento)
             consulta_departamento.bindValue(":Nombre_departamento_persona",Nombre_departamento)
             estado= consulta_departamento.exec_()
             if estadoDep==False:
                 QMessageBox.warning(self,"No se pudo realizar la consulta", self.traficoDep.lastError().text(),QMessageBox.Discard) #se guardan los errores que saca
             else:
                 QMessageBox.information(self," Correcto", " Se han insertado los datos correctamente !",QMessageBox.Discard)
             self.traficoDep.close()# se cierra la base de datos  



     def cancelarD(self):
         self.close() #cierra la ventana         
#---------------------------------------------------------------Nueva clase para la tabla Marca Vehiculo---------------------------------------------------------
               
class Marca_vehiculo(QDialog):
     def __init__(self):
         QDialog.__init__(self)
         self.setWindowTitle("Marca de vehiculos") #Titulo
         self.resize(400,400) #Tamano inicial ventana
         self.setMinimumSize(400,400) #Tamano minimo
         uic.loadUi("marca_vehiculo.ui", self)
         #-------------Establecer conexion base de datos---------------
         self.t=QSqlDatabase.addDatabase('QMYSQL')
         self.t.setHostName("127.0.0.1")
         self.t.setDatabaseName("trafico")
         self.t.setUserName("root")
         self.t.setPassword("password")
         
         #--------Conectar botones------
         self.btnadd.clicked.connect(self.insert)
         self.btncancel.clicked.connect(self.cancel)
          

     def insert(self):
         e=self.t.open()
         if e==False:
             QMessageBox.warning(self,"No se pudo abrir la base de datos", self.t.lastError().text(),QMessageBox.Discard) #se guardan los errores que saca
         else:
             id_marcaVeh=self.id_marcavehiculo.text()
             Nombre_marcaVeh=self.Nombre_marcavehiculo.text()
             Dir_marcaVeh=self.Direccion_marcavehiculo.text()
             sql_marca_vehiculo="INSERT INTO Marca_vehiculo(id_marcavehiculo,Nombre_marcavehiculo, Direccion_marcavehiculo) VALUES(:id_marcavehiculo,:Nombre_marcavehiculo, :Direccion_marcavehiculo)"
             consulta_marcaVeh=QSqlQuery()
             consulta_marcaVeh.prepare(sql_marca_vehiculo)
             consulta_marcaVeh.bindValue(":id_marcavehiculo",id_marcaVeh)
             consulta_marcaVeh.bindValue(":Nombre_marcavehiculo",Nombre_marcaVeh)
             consulta_marcaVeh.bindValue(":Direccion_marcavehiculo",Dir_marcaVeh)
             
             e= consulta_marcaVeh.exec_()
             if e==False:
                 QMessageBox.warning(self,"No se pudo realizar la consulta", self.t.lastError().text(),QMessageBox.Discard) #se guardan los errores que saca
             else:
                 QMessageBox.information(self," Correcto", " Se han insertado los datos correctamente !",QMessageBox.Discard)
             self.t.close()# se cierra la base de datos  



     def cancel(self):
         self.close() #cierra la ventana
                            
#------------------------------- Nueva clase para la tabla Modelo vehiculo-------------------------------------------------------------------------
class Modelo_vehiculo(QDialog):
     def __init__(self):
         QDialog.__init__(self)
         self.setWindowTitle("Modelo de vehiculos") #Titulo
         self.resize(400,400) #Tamano inicial ventana
         self.setMinimumSize(400,400) #Tamano minimo
         uic.loadUi("modelo_vehiculo.ui", self)
         #-------------Establecer conexion base de datos---------------
         self.traficom=QSqlDatabase.addDatabase('QMYSQL')
         self.traficom.setHostName("127.0.0.1")
         self.traficom.setDatabaseName("trafico")
         self.traficom.setUserName("root")
         self.traficom.setPassword("password")
         
         #--------Conectar botones------
         self.btoninsertar.clicked.connect(self.insertarm)
         self.btoncancelar.clicked.connect(self.cancelm)
          

     def insertarm(self):
         emodelo=self.traficom.open()
         if emodelo==False:
             QMessageBox.warning(self,"No se pudo abrir la base de datos", self.traficom.lastError().text(),QMessageBox.Discard) #se guardan los errores que saca
         else:
             id_modeloVeh=self.id_modelo_vehiculo.text()
             Nombre_modeloVeh=self.Nombre_modelo_vehiculo.text()
             Cantidad_modeloVeh=self.Cantidad_vehiculo.text()
             Potencia_modeloVeh=self.potencia_vehiculo.text()
             id_marcaVeh=self.id_marcavehiculo.text()
             sql_modelo_vehiculo="INSERT INTO Modelo_vehiculo(id_modelo_vehiculo,Nombre_modelo_vehiculo, Cantidad_vehiculo,potencia_vehiculo,id_marcavehiculo) VALUES(:id_modelo_vehiculo,:Nombre_modelo_vehiculo, :Cantidad_vehiculo,:potencia_vehiculo,:id_marcavehiculo)"
             consulta_modeloVeh=QSqlQuery()
             consulta_modeloVeh.prepare(sql_modelo_vehiculo)
             consulta_modeloVeh.bindValue(":id_modelo_vehiculo",id_modeloVeh)
             consulta_modeloVeh.bindValue(":Nombre_modelo_vehiculo",Nombre_modeloVeh)
             consulta_modeloVeh.bindValue(":Cantidad_vehiculo",Cantidad_modeloVeh)
             consulta_modeloVeh.bindValue(":potencia_vehiculo",Potencia_modeloVeh)
             consulta_modeloVeh.bindValue(":id_marcavehiculo",id_marcaVeh)
             
             emodelo= consulta_modeloVeh.exec_()
             if emodelo==False:
                 QMessageBox.warning(self,"No se pudo realizar la consulta", self.traficom.lastError().text(),QMessageBox.Discard) #se guardan los errores que saca
             else:
                 QMessageBox.information(self," Correcto", " Se han insertado los datos correctamente !",QMessageBox.Discard)
             self.traficom.close()# se cierra la base de datos  



     def cancelm(self):
         self.close() #cierra la ventana
         

         

app=QApplication(sys.argv)
ventana=ventana_principal()
ventana.show()
ventana.setWindowTitle('Bienvenido')
#ciudad=Ciudad()
#ciudad.show()
app.exec_()

