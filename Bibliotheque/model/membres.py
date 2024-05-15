from model.connexion import *

class Membre:
  def __init__(
          self,
          id_membre = 0,
          nom_membre = "",
          date_naissance = "",
          abonnement = "",
          contact = 0
  ):
    self.co = Connexion.connecter()
    self._id_membre = id_membre
    self._nom_membre = nom_membre
    self._date_naissance = date_naissance
    self._abonnement = abonnement
    self._contact = contact

  def _get_id_membre(self):
    return self._id_membre
  def _get_nom_membre(self):
    return self._nom_membre
  def _get_date_naissance(self):
    return self._date_naissance
  def _get_abonnement(self):
    return self._abonnement
  def _get_contact(self):
    return self._contact
  def _set_id_membre(self,id):
    self._id_membre = id
  def _set_nom_membre(self, nom):
    self._nom_membre = nom
  def _set_date_naissance(self,date):
    self._date_naissance = date
  def _set_abonnement(self, abonnement):
    self._abonnement = abonnement
  def _set_contact(self, contact):
    self._contact = contact

  def create(self):
    curseur = self.co.cursor()
    chaine = "INSERT INTO membres VALUES (null, %s, %s, %s, %s ,default)"
    valeurs = (self._nom_membre, self._date_naissance, self._abonnement, self._contact)
    curseur.execute(chaine, valeurs)
    self.co.commit()
  def read(self):
    curseur = self.co.cursor()
    chaine = "SELECT * FROM membres"
    curseur.execute(chaine)
    resultat = curseur.fetchall()
    return resultat