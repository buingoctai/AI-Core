import os
import sys


def writeInputedUser(data, fileName):
    input_user = data

    if not (os.path.isdir('data_evaluate_cnn')):
        os.mkdir('data_evaluate_cnn')
    f = open('data_evaluate_cnn/Data{}.findRestaurantsByCity'.format(fileName), 'w+')
    f.write(input_user+'.')
    f.close()

    f = open('data_evaluate_cnn/Data{}.greet'.format(fileName), 'w+')
    f.write(input_user+'.')
    f.close()

    f = open('data_evaluate_cnn/Data{}.bye'.format(fileName), 'w+')
    f.write(input_user+'.')
    f.close()

    f = open('data_evaluate_cnn/Data{}.affirmative'.format(fileName), 'w+')
    f.write(input_user+'.')
    f.close()

    f = open('data_evaluate_cnn/Data{}.negative'.format(fileName), 'w+')
    f.write(input_user+'.')
    f.close()

    os.system(
        'python to_eval.py --eval_train --checkpoint_dir="./run_cnn/model/checkpoints/" --outputFileName='+fileName)
