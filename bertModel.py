import numpy as np
import pandas as pd
import ktrain
from ktrain import text

data_train = pd.read_csv('datasets/finalCleanTrainingDataset.csv', dtype = str)
data_test = pd.read_csv('datasets/finalTestingDataset.csv', dtype = str)

(X_train, y_train), (X_test, y_test), preprocess = text.texts_from_df(train_df = data_train,
                    text_column = 'GameDescription',
                    label_columns = 'Review',
                    val_df = data_test,
                    maxlen = 400,
                    preprocess_mode = 'bert')

# prints out total rows of training data
X_train[0].shape

model = text.text_classifier(name='bert',
                             train_data = (X_train, y_train),
                             preproc = preprocess)

# get learning rate
learner = ktrain.get_learner(model = model,
                             train_data = (X_train, y_train),
                             val_data = (X_test, y_test),
                             batch_size = 6)

# optimal learning rate for this model is 2e-5
learner.fit_onecycle(lr = 2e-5, epochs = 1)

predictor = ktrain.get_predictor(learner.model, preprocess)

# sample test data
data = ['Phoenix Wright: Ace Attorney is a visual novel adventure game where the player takes the role of Phoenix Wright, a rookie defense attorney, and attempts to defend their clients in five cases. These cases are played in a specific order. After finishing them, the player can re-play them in any order.']

# prints out prediction of sample data
prediction = predictor.predict(data)
print(prediction)
