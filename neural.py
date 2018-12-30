# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

data_input = []
data_result = []

with open('fifty-fifty.csv') as fp:  
   for line in fp:
	   letters = list(line.split(',')[0])
	   letter_nums = []
	   for letter in letters:
		   letter_nums.append((ord(letter) - 97) / 26)
	   result = 1 if line.split(', ')[1] == 'true\n' else 0
	   data_input.append(letter_nums)
	   data_result.append(result)

train_input = np.array(data_input)
train_result = np.array(data_result)

accuracy_over_units = [0]

for i in range(1, 50, ):
	# create model
	model = Sequential()
	model.add(Dense(i, input_dim=4, activation='relu'))
	model.add(Dense(1, activation='sigmoid'))

	model.compile(optimizer='adam', 
				loss='binary_crossentropy',
				metrics=['accuracy'])

	model.fit(train_input, train_result, epochs=100)
	print("Finished training model #" + str(i))
	accuracy_over_units.append(model.evaluate(train_input, train_result, batch_size=512)[1])

print("The size of the unit accuracy is " + str(len(accuracy_over_units)))
# change the font size on the plot so it's legible
font = {'size'   : 18}
plt.rc('font', **font)

# give our plot a title
plt.title("Accuracy over Hidden Units with One Layer")


# plot training, accuracy, and validation and label the lines
plt.plot(accuracy_over_units, label='Training')


# label the axes
plt.xlabel("Hidden Units")
plt.ylabel("Accuracy")

# show the plot
plt.show()