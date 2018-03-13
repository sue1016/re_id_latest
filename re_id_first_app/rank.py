import scipy.io as si
import os
import sys
import numpy as np


def rank_save(img_dir):
    # print(os.path.isfile('static/mat/pytorch_result.mat'))
    print(sys.path[0])
    base = 're_id_first_app/static/image/Market-1501-v15.09.15'
    gallery_dir = os.path.join(base, 'bounding_box_test')
    query_dir = os.path.join(base, 'query')
    result = si.loadmat('re_id_first_app/static/mat/pytorch_result.mat')
    query_feature = result['query_f']
    gallery_feature = result['gallery_f']
    # test_img='1483_c3s3_061578_00.jpg'
    # img_dir = input("Input the dir of your image:")
    print(os.path.join(query_dir, img_dir))
    if os.path.exists(os.path.join(query_dir, img_dir)):
        print("jpg file exists")
        curdir = os.listdir(query_dir)
        curdir.sort()
        pos = curdir.index(img_dir)
        print('jpg file position: ', pos)
        # print("position"+ pos)
        score = np.dot(gallery_feature, query_feature[pos])
        index = np.argsort(score)
        index = index[::-1]
        best_index = []
        result_dir = os.listdir(gallery_dir)
        result_dir.sort()
        gallery_imgs = result_dir
        for i in range(10):
            best_index.append(gallery_imgs[index[i + 1]])
        f = open("matching_info.txt", 'w')
        for i in range(10):
            f.write(best_index[i] + ' ')
        f.close()
    else:
        print("Dir does not exist")

    #
    # img_source = cv2.imread(os.path.join(query_dir,img_dir),0)
    # imshow('source',img_source)
    # img_match = cv2.imread(best_index, 0)
    # imshow('best_matching', img_match)
    # cv2.waitKey(0)