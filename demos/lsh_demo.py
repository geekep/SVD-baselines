# -*- coding: UTF-8 -*-
# !/user/bin/python3

import os
import sys
import random

import numpy as np

parentddir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parentddir)

from approach.lsh import LSHAlgo

from utils.util import *
from utils.args import opt
from utils.logger import logger
from utils.calc_hamming_ranking import calc_hamming_ranking

__DIM = 4096


def main():
    # basic setting
    random.seed(opt['seed'])
    np.random.seed(opt['seed'])

    # create approach
    lsh = LSHAlgo(__DIM)
    logger.info('creating lsh method done')

    # load features
    featurepath = os.path.join(opt['featurepath'], 'videos-features.h5')
    features, mean_feature = load_features(featurepath)

    # generate binary codes
    codes = lsh.generate_codes(features, mean_feature=mean_feature)
    logger.info('generating codes done')

    # load groundtruth and unlabeled-keys
    gnds = load_groundtruth('test_groundtruth')
    unlabeled_keys = get_video_id('unlabeled-data')
    logger.info('loading gnds and unlabeled keys done. #query: {}'.format(len(gnds)))

    # calculate map
    map = calc_hamming_ranking(codes, unlabeled_keys, gnds)
    logger.info('map: {:.4f}'.format(map))

    logger.info('all done')

if __name__ == "__main__":
    assert opt['approach'] == 'lsh'
    main()


'''bash
python demos/lsh_demo.py --dataname svd --approach lsh
'''
