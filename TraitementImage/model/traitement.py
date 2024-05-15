from PIL import Image
class Traitement:
  def __init__(self, nom, nomParDefaut):
    self.img = Image.open(nom)
    self.nom = nomParDefaut
    print(nomParDefaut)
  def Rouge(self):
    (largeur, hauteur) = self.img.size
    img_vaovao = Image.new("RGB", (largeur, hauteur))
    print(self.img.getpixel((0, 0)))
    for i in range(largeur):
      for j in range(hauteur):
        (r, v, b) = self.img.getpixel((i, j))
        img_vaovao.putpixel((i, j), ( 255 - r , 0 , 0))
    img_vaovao.save(f"{self.nom}_ROUGE.jpg", "JPEG")
    img_vaovao.show()
  def Vert(self):
    (largeur, hauteur) = self.img.size
    img_vaovao = Image.new("RGB", (largeur, hauteur))
    for i in range(largeur):
      for j in range(hauteur):
        (r, v, b) = self.img.getpixel((i, j))
        img_vaovao.putpixel((i, j), (0, 255-v, 0))
    img_vaovao.save(f"{self.nom}_VERT.jpg", "JPEG")
    img_vaovao.show()

  def Bleu(self):
    (largeur, hauteur) = self.img.size
    img_vaovao = Image.new("RGB", (largeur, hauteur))
    for i in range(largeur):
      for j in range(hauteur):
        (r, v, b) = self.img.getpixel((i, j))
        img_vaovao.putpixel((i, j), ( 0, 0, 255-b))
    img_vaovao.save(f"{self.nom}_BLEU.jpg", "JPEG")
  def NB(self):
    (largeur, hauteur) = self.img.size
    img_vaovao = Image.new("RGB", (largeur, hauteur))
    for i in range(largeur):
      for j in range(hauteur):
        (r, v, b) = self.img.getpixel((i, j))
        m = (r + v + b) // 3
        img_vaovao.putpixel((i, j), (m, m, m))
    img_vaovao.save(f"{self.nom}_NOIR_ET_BLANC.jpg", "JPEG")
    img_vaovao.show()
  def Jaune(self):
    (largeur, hauteur) = self.img.size
    img_vaovao = Image.new("RGB", (largeur, hauteur))
    for i in range(largeur):
      for j in range(hauteur):
        (r, v, b) = self.img.getpixel((i, j))
        img_vaovao.putpixel((i, j), (125 - r, 125- v , b))
    img_vaovao.save(f"{self.nom}_JAUNE.jpg", "JPEG")
    img_vaovao.show()