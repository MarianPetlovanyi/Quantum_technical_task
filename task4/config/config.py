import os
# define the base path to the *original* input dataset and then use
# the base path to derive the image and annotations directories
ORIG_BASE_PATH = "soils"
ORIG_IMAGES = os.path.sep.join([ORIG_BASE_PATH, "images"])
ORIG_ANNOTS = os.path.sep.join([ORIG_BASE_PATH, "erosion"])

BASE_PATH = "dataset"
POSITVE_PATH = os.path.sep.join([BASE_PATH, "positive"])
NEGATIVE_PATH = os.path.sep.join([BASE_PATH, "negative"])

MAX_PROPOSALS = 2000
MAX_PROPOSALS_INFER = 200

MAX_POSITIVE = 30
MAX_NEGATIVE = 10


INPUT_DIMS = (224, 224)
# define the path to the output model and label binarizer
MODEL_PATH = "erosion_detector.h5"
ENCODER_PATH = "label_encoder.pickle"
# define the minimum probability required for a positive prediction
# (used to filter out false-positive predictions)
MIN_PROBA = 0.99