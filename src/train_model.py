
import tflearn as tfl
from src.audio.batch_reader import collate_and_convert_audio_in_directory

# Hyperparameters
learning_rate = 0.0001
SAMPLE_RATE = 3000.0
AUDIO_MS = 1000.0
AUDIO_CHANNELS = 2

def configure_network(AUDIO_SHAPE):
    network = tfl.input_data([None, AUDIO_SHAPE, AUDIO_CHANNELS])
    network = tfl.lstm(network, 30, dropout=0.8)
    network = tfl.fully_connected(network, 2, activation='softmax')
    network = tfl.regression(network, optimizer='adam', learning_rate=learning_rate, loss='categorical_crossentropy')
    return network


def split_list(a_list):
    half = len(a_list)/2
    return a_list[:half], a_list[half:]


def main():
    audio_search_directory = input("Please input a directory where you audio files can be found: ")
    batch_audio = collate_and_convert_audio_in_directory(audio_search_directory, SAMPLE_RATE, AUDIO_MS, AUDIO_CHANNELS)
    X, Y = batch_audio.get_audio_and_encoded_category()
    train_x, test_x = split_list(X)
    train_y, test_y = split_list(Y)
    neural_network = configure_network(int(SAMPLE_RATE * (AUDIO_MS / 1000)))
    training_iterations = 100
    model = tfl.DNN(neural_network, tensorboard_verbose=3)
    _y = None
    while training_iterations > 0:
        model.fit(train_x, train_y, n_epoch=1, validation_set=(test_x, test_y), show_metric=True, batch_size=10)
        _y = model.predict(X)
        print(_y)
        print "Training iteration: {0}".format(training_iterations)
        training_iterations = training_iterations -1
    model.save('metallica.rem.model')

if __name__ == "__main__": main()