import pickle  

# 假设你的 pkl 文件名为 'data.pkl'  
with open('./infogcn_head_6/best_score.pkl', 'rb') as f:  
    data = pickle.load(f)  

print("Keys in the dictionary:")  
print(list(data.keys()))  

print("\nValues in the dictionary:")  
for key, value in data.items():  
    print(f"{key}: {type(value)}")  
    print(value.shape)    
    
    
# import pickle  

# # 指定 pkl 文件的路径  
# pkl_file_path = 'test_label_B.pkl'  

# # 读取 pkl 文件  
# with open(pkl_file_path, 'rb') as f:  
#     data = pickle.load(f)  

# # 输出数据的 shape  
# print(f"The shape of the data is: {data.shape}")

# # 输出数据的数据类型  
# print(f"The data type of the data is: {data.dtype}") 
