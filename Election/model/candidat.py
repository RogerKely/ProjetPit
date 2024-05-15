from model.connexion import Connexion
class Candidat:
  def __init__(self,id = 0,nom=0):
    self._nom = nom
    self._id = id
    self._con = Connexion.connecter()
  def _get_nom(self):
    return self._nom
  def _set_nom(self,nom):
    self._nom = nom
  def _get_id(self):
    return self._id
  def _set_id(self,id):
    self._id = id
  nom = property(_get_nom, _set_nom)
  id = property(_get_id, _set_id)
  def compteurCandidat(self):
    curseur = self._con.cursor()
    chaine = "SELECT COUNT(*),nom_candidat FROM listeVote GROUP BY listeVote.id_candidat ORDER BY listeVote.id_candidat"
    curseur.execute(chaine)
    result = curseur.fetchall()
    return result
  def read(self):
    curseur = self._con.cursor()
    chaine = "SELECT * FROM candidat"
    curseur.execute(chaine)
    result = curseur.fetchall()
    return result
  def add(self):
    curseur = self._con.cursor()
    chaine = "INSERT INTO listeVote VALUES (null,%s, %s)"
    valeur = (self.id,self.nom)
    curseur.execute(chaine,valeur)
    self._con.commit()