import tflearn as tfl
from src.audio.batch_reader import collate_audio_in_directory

# Hyperparameters
learning_rate = 0.0001

def main():
    batch_audio = collate_audio_in_directory('/home/andrew/Downloads')
    X, Y = batch_audio.get_audio_and_encoded_category()
    train_x, train_y = X, Y
    test_x, test_y = X, Y
    net = tfl.input_data([None, 20, 80])
    net = tfl.lstm(net, 128, dropout=0.8)
    net = tfl.fully_connected(net, 2, activation='softmax')
    net = tfl.regression(net, optimizer='adam', learning_rate=learning_rate, loss='categorical_crossentropy')
    training_iters = 300000
    model = tfl.DNN(net, tensorboard_verbose=0)
    while training_iters > 0:
        model.fit(train_x, train_y, n_epoch=2, validation_set=(test_x, test_y), show_metric=True, batch_size=64)
        _y = model.predict(X)
        training_iters = training_iters -1
    model.save('tflearn.lstm.model')
    print(_y)
    print(y)


if __name__ == "__main__": main()