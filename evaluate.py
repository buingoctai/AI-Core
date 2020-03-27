import os
import sys


def writeInputedUser(data,fileName):
    input_user = data

    if not (os.path.isdir('data_evaluate_cnn')):
        os.mkdir('data_evaluate_cnn')
    f = open('data_evaluate_cnn/Data.findRestaurantsByCity', 'w+')
    f.write(input_user+'.')
    f.close()

    f = open('data_evaluate_cnn/Data.greet', 'w+')
    f.write(input_user+'.')
    f.close()

    f = open('data_evaluate_cnn/Data.bye', 'w+')
    f.write(input_user+'.')
    f.close()

    f = open('data_evaluate_cnn/Data.affirmative', 'w+')
    f.write(input_user+'.')
    f.close()

    f = open('data_evaluate_cnn/Data.negative', 'w+')
    f.write(input_user+'.')
    f.close()

    os.system(
        'python to_eval.py --eval_train --checkpoint_dir="./run_cnn/model/checkpoints/" --outputFileName='+fileName)
