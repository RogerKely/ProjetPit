#! /usr/bin/python3


import mysql.connector as m
class Connexion:
  bdd = m.connect (
    host = "127.0.0.1",
    user = "root",
    passwd = "",
    database = "examen_python_edt"
  )
  def connecter(cls):
    return Connexion.bdd
  connecter = classmethod(connecter)