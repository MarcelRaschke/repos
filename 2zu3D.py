import numpy as np
from PIL import Image
import trimesh

def image_to_3d_model(image_path, depth_map_path=None, extrusion_depth=1.0, smoothing_iterations=10):
  """Wandelt ein 2D-Bild in ein 3D-Modell um."""

  try:
      img = Image.open(image_path).convert('L')  # Graustufenbild laden
      img_array = np.array(img) / 255.0  # Normalisieren auf 0-1
  except FileNotFoundError:
      return "Bilddatei nicht gefunden."

  if depth_map_path:
      try:
          depth_img = Image.open(depth_map_path).convert('L')
          depth_array = np.array(depth_img) / 255.0
          z_values = depth_array * extrusion_depth  # Tiefenkarte anwenden
      except FileNotFoundError:
          return "Tiefenkartendatei nicht gefunden."
  else:
      z_values = img_array * extrusion_depth # Helligkeit als Tiefe verwenden

  rows, cols = img_array.shape
  vertices = []
  faces = []

  for y in range(rows):
      for x in range(cols):
          vertices.append([x, y, z_values[y, x]])

  for y in range(rows - 1):
      for x in range(cols - 1):
          v1 = y * cols + x
          v2 = y * cols + x + 1
          v3 = (y + 1) * cols + x + 1
          v4 = (y + 1) * cols + x

          faces.extend([[v1, v2, v3], [v1, v3, v4]])

  mesh = trimesh.Trimesh(vertices=vertices, faces=faces, process=False)

  if smoothing_iterations > 0:
      mesh = mesh.smoothed(iterations=smoothing_iterations) # Modell glätten

  return mesh

# Beispielanwendung
image_path = "pfad/zum/bild.jpg"
depth_map_path = "pfad/zur/tiefenkarte.jpg" # Optional

model = image_to_3d_model(image_path, depth_map_path)

if isinstance(model, trimesh.Trimesh):
  model.export("3d_model.stl") # Als STL-Datei speichern
  print("3D-Modell wurde erstellt und gespeichert als 3d_model.stl")
else:
  print(model) # Fehler ausgeben