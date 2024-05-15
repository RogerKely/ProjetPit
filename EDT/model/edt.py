from model.connexion import Connexion

class Edt:
  def __init__(
          self,
          matiere = 0,
          salle = 0,
          classe = 0,
          date = "",
          hDebut = "",
          hFin = ""
  ):
    self.co  =Connexion.connecter()
    self._matiere = matiere
    self._salle = salle
    self._classe = classe
    self._date = date
    self._hDebut = hDebut
    self._hFin = hFin
  def _get_matiere(self):
    return self._matiere
  def _get_salle(self):
    return self._salle
  def _get_classe(self):
    return self._classe
  def _get_hDebut(self):
    return self._hDebut
  def _get_date(self):
    return self._date
  def _get_hFin(self):
    return self._hFin
  def _set_matiere(self,matiere):
    self._matiere = matiere
  def _set_salle(self,salle):
    self._salle = salle
  def _set_classe(self,classe):
    self._classe = classe
  def _set_date(self,date):
    self._date = date
  def _set_hDebut(self,hDebut):
    self._hDebut = hDebut
  def _set_hFin(self,hFin):
    self._hFin = hFin

  matiere = property(_get_matiere, _set_matiere)
  salle = property(_get_salle, _set_salle)
  classe = property(_get_classe, _set_classe)
  date = property(_get_date, _set_date)
  hDebut = property(_get_hDebut, _set_hDebut)
  hFin = property(_get_hFin, _set_hFin)
  def create(self):
    curseur = self.co.cursor()
    chaine = "INSERT INTO edt VALUES (null, %s, %s, %s, %s, %s, %s)"
    valeurs = (self.matiere, self.salle, self.classe, self.date, self.hDebut, self.hFin)
    curseur.execute(chaine, valeurs)
    self.co.commit()
  def read(self):
    curseur = self.co.cursor()
    chaine = ("SELECT matiere.intitule,salle.code,classe.intitule,edt.date, edt.hDebut,edt.hFin "
              "FROM edt "
              "LEFT JOIN matiere on edt.id_matiere = matiere.id_matiere "
              "LEFT JOIN salle on edt.id_salle = salle.id_salle "
              "LEFT JOIN classe on edt.id_classe = classe.id_classe")
    curseur.execute(chaine)
    resultat = curseur.fetchall()
    return resultat

