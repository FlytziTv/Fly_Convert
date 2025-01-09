from PIL import Image
import os

def convert_webp_to_png(input_folder, output_folder):
    # Vérifier si le dossier de sortie existe, sinon le créer
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Parcourir les fichiers du dossier d'entrée
    for filename in os.listdir(input_folder):
        if filename.endswith('.webp'):
            # Chemin complet des fichiers d'entrée et de sortie
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename.replace('.webp', '.png'))
            
            try:
                # Ouvrir le fichier WebP et le convertir en PNG
                with Image.open(input_path) as img:
                    img = img.convert('RGBA')  # S'assurer d'un canal alpha si nécessaire
                    img.save(output_path, 'PNG')
                print(f"Converti: {input_path} -> {output_path}")
            except Exception as e:
                print(f"Erreur lors de la conversion de {filename}: {e}")

# Spécifiez les dossiers d'entrée et de sortie
input_folder = 'chemin/vers/dossier/webp'
output_folder = 'chemin/vers/dossier/png'

convert_webp_to_png(input_folder, output_folder)
