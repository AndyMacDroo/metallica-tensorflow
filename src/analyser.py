
import tflearn as tfl
from src.audio.batch_reader import collate_and_convert_audio_in_directory

# Hyperparameters
learning_rate = 0.0001
SAMPLE_RATE = 8000.0
AUDIO_MS = 1000.0
AUDIO_CHANNELS = 2

def configure_network(AUDIO_SHAPE):
    net = tfl.input_data([None, AUDIO_SHAPE, AUDIO_CHANNELS])
    net = tfl.lstm(net, 100, dropout=0.8)
    net = tfl.fully_connected(net, 2, activation='softmax')
    net = tfl.regression(net, optimizer='adam', learning_rate=learning_rate, loss='categorical_crossentropy')
    return net

def main():
    audio_search_directory = "/home/andrew/Downloads/Data"
    batch_audio = collate_and_convert_audio_in_directory(audio_search_directory, SAMPLE_RATE, AUDIO_MS)
    X, Y = batch_audio.get_audio_and_encoded_category()
    train_x, train_y = X, Y
    test_x, test_y = X, Y
    net = configure_network(int(SAMPLE_RATE * (AUDIO_MS / 1000)))
    training_iters = 300000
    model = tfl.DNN(net, tensorboard_verbose=0)
    _y = None
    while training_iters > 0:
        model.fit(train_x, train_y, n_epoch=2, validation_set=(test_x, test_y), show_metric=True, batch_size=200)
        _y = model.predict(X)
        print(_y)
        training_iters = training_iters -1
    model.save('tflearn.sentiment.model')
    print(_y)


if __name__ == "__main__": main()