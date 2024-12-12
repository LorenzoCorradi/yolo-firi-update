import os
import random
import shutil

def create_test_split(train_dir, test_dir, split_ratio=0.15):
    """
    Crea un set di test spostando una frazione di immagini e le relative etichette da train a test.

    :param train_dir: Percorso alla cartella train (che contiene images e labels).
    :param test_dir: Percorso alla cartella test (che contiene images e labels).
    :param split_ratio: Percentuale di immagini da spostare per il test (es. 0.15 per il 15%).
    """
    # Percorsi delle immagini e delle etichette
    train_images_dir = os.path.join(train_dir, "images")
    train_labels_dir = os.path.join(train_dir, "labels")
    test_images_dir = os.path.join(test_dir, "images")
    test_labels_dir = os.path.join(test_dir, "labels")

    # Crea le directory di test se non esistono
    os.makedirs(test_images_dir, exist_ok=True)
    os.makedirs(test_labels_dir, exist_ok=True)

    # Ottieni tutte le immagini
    image_files = [f for f in os.listdir(train_images_dir) if f.endswith(('.jpg', '.png'))]

    # Determina il numero di immagini da spostare
    num_test_files = int(len(image_files) * split_ratio)

    # Seleziona casualmente le immagini per il test
    test_files = random.sample(image_files, num_test_files)

    # Sposta le immagini e i file di etichetta corrispondenti
    for image_file in test_files:
        # Nome base senza estensione
        base_name = os.path.splitext(image_file)[0]

        # Percorsi delle immagini e delle etichette
        image_src = os.path.join(train_images_dir, image_file)
        label_src = os.path.join(train_labels_dir, base_name + ".txt")
        image_dest = os.path.join(test_images_dir, image_file)
        label_dest = os.path.join(test_labels_dir, base_name + ".txt")

        # Sposta i file
        shutil.move(image_src, image_dest)
        if os.path.exists(label_src):  # Verifica che il file di etichetta esista
            shutil.move(label_src, label_dest)

    print(f"Set di test creato: {num_test_files} immagini spostate.")

# Percorsi delle cartelle
train_dir = "train"
test_dir = "test"

# Creazione del set di test con il 15% delle immagini
create_test_split(train_dir, test_dir, split_ratio=0.15)
