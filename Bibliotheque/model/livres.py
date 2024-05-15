from model.connexion import *

class Livres:
  def __init__(
          self,
          titre = "",
          categorie =""
  ):
    self.co = Connexion.connecter()
    self._titre = titre
    self._categorie = categorie
  def _set_titre(self,titre):
    self._titre = titre
  def _set_categorie(self,categorie):
    self._categorie = categorie
  def _get_titre(self):
    return self._titre
  def _get_categorie(self):
    return self._categorie
  titre = property(_get_titre, _set_titre)
  categorie = property(_get_categorie, _set_categorie)

  def create(self):
    curseur = self.co.cursor()
    chaine = "INSERT INTO livres VALUES (null, %s, %s,default)"
    valeurs = (self.titre, self.categorie)
    curseur.execute(chaine, valeurs)
    self.co.commit()
  def read(self):
    curseur = self.co.cursor()
    chaine = "SELECT * FROM livres"
    curseur.execute(chaine)
    resultat = curseur.fetchall()
    return resultat
