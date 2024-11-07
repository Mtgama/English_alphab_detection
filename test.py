from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing import image


model = load_model('./model_20_epochs.h5')


class_labels = {i:str(i) for i in range(10)}  
class_labels.update({i + 10: chr(97 + i) for i in range(26)})

imgPath = './test.png'
img = image.load_img(imgPath, target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)  
img_array /= 255.0  

predictions = model.predict(img_array)
predicted_class = np.argmax(predictions, axis=1)[0]
predicted_class_name = class_labels.get(predicted_class, "Unknown")


print(f"Predicted class: {predicted_class_name}")
