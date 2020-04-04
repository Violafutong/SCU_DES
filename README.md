# DES不同模式下python实现

1. ## 文件说明 

   > - ctf.py存放算法常量如ip置换矩阵等
   > - des.py des算法部件模块
   > - readandwrite.py 控制密钥，明文，密文，iv文件读写
   > - mian.py主体文件
   > - recording.txt 测试结果保存
   > - des_key.txt 存放密钥
   > - des_iv.txt 存放iv
   > - des_plain.txt 存放明文
   > - des_Cipher.txt  存放show()结果

   

   ## 2.功能实现：

   >1. 对简单明文在ECB，CBC，CFB，OFB进行DES加密；
   >2. 生成随机固定大小文件并对文件内容进行加密；
   >3. 测试不同模式50MB的文件反复加解密50次所用时间；

   

   

   ## 3.引用说明：

   >1.生成随机固定大小文件摘自网络
   >
   >2.ctf静态数据文件数据摘自网络