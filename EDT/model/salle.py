from model.connexion import Connexion
class Salle:
  def __init__(
          self,
          code = "",
          etage = 0
  ):
    self.co = Connexion.connecter()
    self._code = code
    self._etage = etage
  def _get_code(self):
    return self._code
  def _get_etage(self):
    return self._etage
  def _set_code(self,code):
    self._code = code
  def _set_etage(self,etage):
    self._etage = etage
  code = property(_get_code, _set_code)
  etage = property(_get_etage, _set_etage)
  def create(self):
    curseur = self.co.cursor()
    chaine = "INSERT INTO salle VALUES (null, %s, %s)"
    valeurs = (self.code, self.etage)
    curseur.execute(chaine, valeurs)
    self.co.commit()
  def read(self):
    curseur = self.co.cursor()
    chaine = "SELECT * FROM salle"
    curseur.execute(chaine)
    resultat = curseur.fetchall()
    return resultat