from model.connexion import Connexion

class Prof:
  def __init__(
          self,
          id = 0,
          nom = "",
          adresse = "",
          contact = "",
          specialiter = ""
  ):
    self.co = Connexion.connecter()
    self._id_prof = id
    self._nom = nom
    self._adresse = adresse
    self._specialiter = specialiter
    self._contact = contact
  def _get_id_prof(self):
    return self._id_prof
  def _get_nom(self):
    return self._nom
  def _get_adresse(self):
    return self._adresse
  def _get_specialiter(self):
    return self._specialiter
  def _get_contact(self):
    return self._contact
  def _set_id_prof(self,id):
    self._id_prof = id
  def _set_nom(self, nom):
    self._nom = nom
  def _set_adresse(self,date):
    self._adresse = date
  def _set_specialiter(self, specialiter):
    self._specialiter = specialiter
  def _set_contact(self, contact):
    self._contact = contact

  contact = property(_get_contact, _set_contact)
  adresse = property(_get_adresse, _set_adresse)
  nom = property(_get_nom, _set_nom)
  specialiter = property(_get_specialiter, _set_specialiter)

  def create(self):
    curseur = self.co.cursor()
    chaine = "INSERT INTO prof VALUES (null, %s, %s, %s, %s)"
    valeurs = (self._nom, self._adresse, self._contact, self._specialiter)
    curseur.execute(chaine, valeurs)
    self.co.commit()
  def read(self):
    curseur = self.co.cursor()
    chaine = "SELECT * FROM prof"
    curseur.execute(chaine)
    resultat = curseur.fetchall()
    return resultat