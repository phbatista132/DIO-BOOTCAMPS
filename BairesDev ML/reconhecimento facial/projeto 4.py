import cv2
from deepface import DeepFace

img = cv2.imread("imagem_evento.jpg")


detected_faces = DeepFace.extract_faces(img_path="imagem_evento.jpg", enforce_detection=False)


nomes = ["Adam Sandler", "Chris Rock"]


for i, face in enumerate(detected_faces):
    x, y, w, h = face["facial_area"].values()
    nome = nomes[i] if i < len(nomes) else "Desconhecido"


    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(img, nome, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

cv2.imshow("Rostos Rotulados", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
