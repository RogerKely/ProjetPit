from model.connexion import Connexion

class Matiere:
  def __init__(
          self,
          id = 0,
          intitule = "",
          vh = 0,
          prof_id = 0,
          semestre = ""
  ):
    self.co = Connexion.connecter()
    self._id = id
    self._intitule = intitule
    self._vh = vh
    self._prof_id = prof_id
    self._semestre = semestre

  def _get_id(self):
    return self._id
  def _get_intitule(self):
    return self._intitule
  def _get_vh(self):
    return self._vh
  def _get_prof_id(self):
    return self._prof_id
  def _get_semestre(self):
    return self._semestre
  def _set_id(self,id):
    self._id = id
  def _set_intitule(self,intitule):
    self._intitule = intitule
  def _set_vh(self,vh):
    self._vh = vh
  def _set_prof_id(self,id):
    self._prof_id = id
  def _set_semestre(self,semestre):
    self._semestre = semestre

  intitule  = property(_get_intitule, _set_intitule)
  vh        = property(_get_vh, _set_vh)
  prof_id   = property(_get_prof_id, _set_prof_id)
  semestre  = property(_get_semestre, _set_semestre)

  def create(self):
    curseur = self.co.cursor()
    chaine = "INSERT INTO matiere VALUES (null, %s, %s, %s, %s)"
    valeurs = (self.intitule, self.vh, self.prof_id, self.semestre)
    curseur.execute(chaine, valeurs)
    self.co.commit()
  def read(self, all=False):
    curseur = self.co.cursor()
    if (all):
      chaine = "SELECT id_matiere,intitule, vh, matiere.id_prof,prof.nom_prof ,semestre FROM matiere LEFT JOIN prof on prof.id_prof = matiere.id_prof"
    else:
      chaine = "SELECT intitule,vh,prof.nom_prof,semestre FROM matiere LEFT JOIN prof on prof.id_prof = matiere.id_prof"
    curseur.execute(chaine)
    resultat = curseur.fetchall()
    return resultat