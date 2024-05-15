from model.connexion import Connexion

class Classe:
  def __init__(
          self,
          intitule ="",
  ):
    self.co = Connexion.connecter()
    self._intitule = intitule

  def _get_intitule(self):
    return self._intitule
  def _set_intitule(self,intitule):
    self._intitule = intitule
  intitule = property(_get_intitule, _set_intitule)
  def create(self):
    curseur = self.co.cursor()
    chaine = "INSERT INTO classe VALUES (null, %s)"
    valeurs = (self._intitule,)
    curseur.execute(chaine, valeurs)
    self.co.commit()
  def read(self):
    curseur = self.co.cursor()
    chaine = "SELECT * FROM classe"
    curseur.execute(chaine)
    resultat = curseur.fetchall()
    return resultat
