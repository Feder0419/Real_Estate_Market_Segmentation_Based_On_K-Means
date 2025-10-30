from sklearn.metrics.cluster import normalized_mutual_info_score
import pandas as pd
# 假设partition1和partition2是两个分区方法的结果，形式为样点到类别（分区）的映射
data = pd.read_csv("C:\\Users\\tengd\\Desktop\\b.csv")

partition1 = data["Krigin"]
partition2 = data["DB4201T_ID"]

nmi =  normalized_mutual_info_score(partition1, partition2)

print(nmi)