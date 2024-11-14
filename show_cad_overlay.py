from project_3d import project_3d
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import loadmat
from PIL import Image
import os
from pprint import pprint


def show_cad_overlay(cls):
    annotation_path = f'../Annotations/{cls}_pascal/'
    image_path = f'../Images/{cls}_pascal/'
# 加载 CAD 模型
    cad_path = f'../CAD/{cls}.mat'
    object = loadmat(cad_path)
    cad = object[cls]
    listing = os.listdir(annotation_path)
    record_set = [file for file in listing if file.endswith('.mat')]
    for record_element in record_set:
        record = loadmat(f'{annotation_path}{record_element}')['record']
        filename = record["filename"][0][0][0]
        # pprint(filename)
        # break
        im = Image.open(f'{image_path}{filename}')
        plt.imshow(im)

        pprint(record["objects"][0][0])
        break
        # car_idx_set = [i for i, obj in enumerate(record.objects) if obj.class == cls]
        #
        # plt.hold(True)
        # for car_idx in car_idx_set: if record.objects[car_idx].viewpoint.distance == 0:
        #         print('No continuous viewpoint')
        #         continue
        #     vertex = cad[record.objects[car_idx].cad_index].vertices
        #     face = cad[record.objects[car_idx].cad_index].faces
        #     x2d = project_3d(vertex, record.objects[car_idx])
        #     plt.patches('vertices', x2d, 'faces', face, 'FaceColor',
        #                 'blue', 'FaceAlpha', 0.2, 'EdgeColor', 'none')
        #
        plt.axis('off')
        plt.pause(0.1)
        plt.clf()


if __name__ == "__main__":
    show_cad_overlay("car")
