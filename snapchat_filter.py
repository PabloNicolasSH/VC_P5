import cv2
import mediapipe as mp

# Inicializamos MediaPipe para detección de rostros
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=3, min_detection_confidence=0.5)
cap = cv2.VideoCapture(0)

# Carga las imágenes PNG
dog_ears = cv2.imread("assets/dog_ears.png", -1)
dog_nose = cv2.imread("assets/dog_nose.png", -1)
dog_tongue = cv2.imread("assets/dog_tongue.png", -1)

dalmatian_ears = cv2.imread("assets/dalmatian_ears.png", -1)
dalmatian_nose = cv2.imread("assets/dalmatian_nose.png", -1)

def overlay_image(background, overlay, x, y, w, h):
    if x < 0:
        overlay = overlay[:, -x:]  # Recortamos el borde izquierdo de overlay si está fuera del marco
        w += x  # Ajustamos el ancho
        x = 0
    if y < 0:
        overlay = overlay[-y:, :]  # Recortamos el borde superior de overlay si está fuera del marco
        h += y  # Ajustamos la altura
        y = 0
    if x + w > background.shape[1]:
        w = background.shape[1] - x  # Ajustamos el ancho si está fuera del borde derecho
    if y + h > background.shape[0]:
        h = background.shape[0] - y  # Ajustamos la altura si está fuera del borde inferior

    # Verificar que w y h sean positivos
    if w <= 0 or h <= 0:
        return background  # No aplicamos el overlay si las dimensiones no son válidas

    overlay = cv2.resize(overlay, (w, h))
    alpha_overlay = overlay[:, :, 3] / 255.0
    alpha_background = 1.0 - alpha_overlay

    for c in range(3):  # Para cada canal de color (BGR)
        background[y:y + h, x:x + w, c] = (alpha_overlay * overlay[:, :, c] +
                                           alpha_background * background[y:y + h, x:x + w, c])
    return background


while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir el frame a RGB (requisito para MediaPipe)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for i, face_landmarks in enumerate(results.multi_face_landmarks):
            h, w, _ = frame.shape

            # Obtener posiciones de puntos clave para colocar los elementos
            left_eye = face_landmarks.landmark[33]  # Punto sobre el ojo izquierdo
            right_eye = face_landmarks.landmark[263]  # Punto sobre el ojo derecho
            nose = face_landmarks.landmark[1]  # Punto de la nariz
            mouth_top = face_landmarks.landmark[13]  # Punto superior de la boca
            mouth_bottom = face_landmarks.landmark[14]  # Punto inferior de la boca

            # Convertir coordenadas normalizadas a píxeles
            left_eye = (int(left_eye.x * w), int(left_eye.y * h))
            right_eye = (int(right_eye.x * w), int(right_eye.y * h))
            nose = (int(nose.x * w), int(nose.y * h))
            mouth_top = (int(mouth_top.x * w), int(mouth_top.y * h))
            mouth_bottom = (int(mouth_bottom.x * w), int(mouth_bottom.y * h))

            eye_distance = abs(right_eye[0] - left_eye[0])
            ear_width = int(eye_distance * 2.5)  # Ajuste del ancho de las orejas
            nose_width = eye_distance // 2

            if i % 2 == 0:
                ear_height = int(ear_width * dog_ears.shape[0] / dog_ears.shape[1])
                frame = overlay_image(frame, dog_ears, left_eye[0] - ear_width // 4, left_eye[1] - ear_height, ear_width,
                                      ear_height)

                nose_height = int(nose_width * dog_nose.shape[0] / dog_nose.shape[1])
                frame = overlay_image(frame, dog_nose, nose[0] - nose_width // 2, nose[1] - nose_height // 2, nose_width,
                                      nose_height)

            else:
                ear_height = int(ear_width * dalmatian_ears.shape[0] / dalmatian_ears.shape[1])
                frame = overlay_image(frame, dalmatian_ears, left_eye[0] - ear_width // 4, left_eye[1] - ear_height,
                                      ear_width, ear_height)

                nose_height = int(nose_width * dalmatian_nose.shape[0] / dalmatian_nose.shape[1])
                frame = overlay_image(frame, dalmatian_nose, nose[0] - nose_width // 2, nose[1] - nose_height // 2,
                                      nose_width,
                                      nose_height)

            # Detectar si la boca está abierta y colocar la lengua
            mouth_opening_height = abs(mouth_bottom[1] - mouth_top[1])
            mouth_open_threshold = h / 20  # Ajustar este umbral según sea necesario
            if mouth_opening_height > mouth_open_threshold:
                tongue_width = nose_width * 2
                tongue_height = int(tongue_width * dog_tongue.shape[0] / dog_tongue.shape[1])
                frame = overlay_image(frame, dog_tongue, nose[0] - tongue_width // 2, mouth_bottom[1], tongue_width,
                                      tongue_height * 2)

    cv2.imshow("Filtro Snapchat", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()