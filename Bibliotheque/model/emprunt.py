from model.connexion import Connexion

class Emprunt:
  def __init__(self, membre=0, livre=0):
    self.co = Connexion.connecter()
    self._membre = membre
    self._livre = livre
  def _set_livre(self,livre):
    self._livre = livre
  def _set_membre(self,membre):
    self._membre = membre
  def _get_livre(self):
    return self._livre
  def _get_membre(self):
    return self._membre

  livre = property(_get_livre, _set_livre)
  membre = property(_get_membre, _set_membre)

  def create(self):
    curseur = self.co.cursor()
    chaine = "INSERT INTO emprunts VALUES (null, %s, %s,default)"
    valeurs = (self.membre, self.livre)
    curseur.execute(chaine, valeurs)
    self.co.commit()
  def read(self):
    curseur = self.co.cursor()
    chaine = "SELECT * FROM emprunts"
    curseur.execute(chaine)
    resultat = curseur.fetchall()
    return resultat