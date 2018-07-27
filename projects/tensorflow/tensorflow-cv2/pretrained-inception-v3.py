from __future__ import print_function

import os
import cv2
import timeit
import numpy as np
import tensorflow as tf

camera = cv2.VideoCapture(0)


## CANDY
GRAPH 	= "/Users/mattthompson/Desktop/development/code/raspberrypi/projects/tensorflow/tensorflow-for-poets-2/tf_files/retrained_candy_graph.pb"
LABELS = "/Users/mattthompson/Desktop/development/code/raspberrypi/projects/tensorflow/tensorflow-for-poets-2/tf_files/retrained_candy_labels.txt"

## INCEPTION V3
#LABELS 	= "/Users/mattthompson/Downloads/inception_v3_2016_08_28_frozen.pb/imagenet_slim_labels.txt"
#GRAPH 	= "/Users/mattthompson/Downloads/inception_v3_2016_08_28_frozen.pb/inception_v3_2016_08_28_frozen.pb"


# Loads label file, strips off carriage return
label_lines = [line.rstrip() for line in tf.gfile.GFile(LABELS)]

def grabVideoFeed():
    grabbed, frame = camera.read()
    return frame if grabbed else None

def initialSetup():
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
    start_time = timeit.default_timer()

    # This takes 2-5 seconds to run
    # Unpersists graph from file
    with tf.gfile.FastGFile(GRAPH, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        tf.import_graph_def(graph_def, name='')

    print('Took %s seconds to unpersist the graph' % (timeit.default_timer() - start_time))

initialSetup()

with tf.Session() as sess:
    start_time = timeit.default_timer()

    # Feed the image_data as input to the graph and get first prediction
    softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

    print('Took %s seconds to feed data to graph' % (timeit.default_timer() - start_time))

    while True:
        frame = grabVideoFeed()

        if frame is None:
            raise SystemError('Issue grabbing the frame')

        frame = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_CUBIC)

        # adhere to TS graph input structure
        numpy_frame = np.asarray(frame)
        numpy_frame = cv2.normalize(numpy_frame.astype('float'), None, -0.5, .5, cv2.NORM_MINMAX)
        numpy_final = np.expand_dims(numpy_frame, axis=0)

        start_time = timeit.default_timer()

        # This takes 2-5 seconds as well
        #predictions = sess.run(softmax_tensor, {'Mul:0': numpy_final})
        predictions = sess.run(softmax_tensor, {'input:0': numpy_final})

        #print('Took %s seconds to perform prediction' % (timeit.default_timer() - start_time))

        start_time = timeit.default_timer()

        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

        #print('Took %s seconds to sort the predictions' % (timeit.default_timer() - start_time))
        lab 	= False
        pred 	= False
        for node_id in top_k:
            human_string = label_lines[node_id]
            score = predictions[0][node_id]
            if not pred:
            	pred = score
            if not lab:
            	lab = human_string
            print('%s (score = %.5f)' % (human_string, score))


        msg 	= str(lab) + ": " + str(pred) + "%"
        cv2.putText(frame, msg, (10, 50),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)

        cv2.imshow('Main', frame)

        print('********* Session Ended *********')

        if cv2.waitKey(1) & 0xFF == ord('q'):
            sess.close()
            break

camera.release()
cv2.destroyAllWindows()
