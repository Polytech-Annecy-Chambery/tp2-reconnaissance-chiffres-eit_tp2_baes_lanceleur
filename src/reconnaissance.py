from image import Image


def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image, liste_modeles, S):
    image_binarisee = image.binarisation(S)
    image_localisation = image_binarisee.localisation()
    simil = 0
    indice_simil = 0
    for i in range(0,9):
        image_resize = image_localisation.resize(liste_modeles[i].H,liste_modeles[i].W)
        if image_resize.similitude(liste_modeles[i]) > simil:
            indice_simil = i
        simil = image_resize.similitude(liste_modeles[i])
    return indice_simil

