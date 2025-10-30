# import os,sys
# os.chdir(sys.path[0])
# sys.path.append(os.getcwd())

import rasterio
import numpy as np

#保存带坐标的地图的函数
def raster_write(output_file, data, count, crs, transform):  #（路径，矩阵数据，波段数，坐标系统，仿射关系）
    writer = rasterio.open(output_file, mode='w+', driver='GTiff', height=data.shape[-2], width=data.shape[-1],
                           count=count, dtype=np.float32, crs=crs, transform=transform)
    for i in range(1, count + 1):
        writer.write(data[i-1], i)
    writer.close()

with rasterio.open('KMeanMat_5E05.tif') as dataset:
    data = dataset.read() # 栅格数据
    transform = dataset.transform #仿射关系
    crs = dataset.crs #坐标系统
    count = dataset.count #波段数

#读取灰度图
img = data[0]
#data[0] = processed matrix

#保存示例
raster_write('result.tif', data, 1, crs, transform)

# 检查读取有没有成功用的
# band, rows, cols = data.shape
# print(data.shape)
# #(波段，行，列)

# print(rowdata[13300][10260])
# #行，列
