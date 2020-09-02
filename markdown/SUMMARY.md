# 深度學習筆記目錄

## 第一門課 神經網路和深度學習(Neural Networks and Deep Learning) 

[第一週：深度學習引言(Introduction to Deep Learning) ](lesson1-week1.md)

1.1 歡迎(Welcome)

1.2 什麼是神經網路？(What is a Neural Network) 

1.3 神經網路的監督學習(Supervised Learning with Neural Networks) 

1.4 為什麼神經網路會流行？(Why is Deep Learning taking off?) 

1.5 關於本課程(About this Course) 

1.6 課程資源(Course Resources) 

1.7 Geoffery Hinton 專訪(Geoffery Hinton interview) 

[第二週：神經網路的程式基礎(Basics of Neural Network programming) ](lesson1-week2.md)

2.1 二分類(Binary Classification) 

2.2 邏輯回歸(Logistic Regression) 

2.3 邏輯回歸的代價函數（Logistic Regression Cost Function） 

2.4 梯度下降（Gradient Descent） 

2.5 導數（Derivatives）

2.6 更多的導數例子（More Derivative Examples） 

2.7 計算圖（Computation Graph）

2.8 使用計算圖求導數（Derivatives with a Computation Graph） 

2.9 邏輯回歸的梯度下降（Logistic Regression Gradient Descent） 

2.10 梯度下降的例子(Gradient Descent on m Examples) 

2.11 向量化(Vectorization) 

2.12 更多的向量化例子（More Examples of Vectorization）

2.13 向量化邏輯回歸(Vectorizing Logistic Regression) 

2.14 向量化邏輯回歸的梯度計算（Vectorizing Logistic Regression's Gradient）

2.15 Python中的廣播機制（Broadcasting in Python）

2.16 關於 Python與numpy向量的使用（A note on python or numpy vectors）

2.17 Jupyter/iPython Notebooks快速入門（Quick tour of Jupyter/iPython Notebooks）

2.18 邏輯回歸損失函數詳解（Explanation of logistic regression cost function）

[第三週：淺層神經網路(Shallow neural networks)](lesson1-week3.md)

3.1 神經網路概述（Neural Network Overview）

3.2 神經網路的表示（Neural Network Representation） 

3.3 計算一個神經網路的輸出（Computing a Neural Network's output）

3.4 多樣本向量化（Vectorizing across multiple examples）

3.5 向量化實現的解釋（Justification for vectorized implementation）

3.6 啟動函數（Activation functions） 

3.7 為什麼需要非線性啟動函數？（why need a nonlinear activation function?） 

3.8 啟動函數的導數（Derivatives of activation functions） 

3.9 神經網路的梯度下降（Gradient descent for neural networks） 

3.10（選修）直觀理解反向傳播（Backpropagation intuition） 

3.11 隨機初始化（Random+Initialization）

[第四周：深層神經網路(Deep Neural Networks)](lesson1-week4.md)

4.1 深層神經網路（Deep L-layer neural network） 

4.2 前向傳播和反向傳播（Forward and backward propagation） 

4.3 深層網路中的前向和反向傳播（Forward propagation in a Deep Network）

4.4 核對矩陣的維數（Getting your matrix dimensions right） 

4.5 為什麼使用深層表示？（Why deep representations?）

4.6 搭建神經網路塊（Building blocks of deep neural networks）

4.7 參數VS超參數（Parameters vs Hyperparameters） 

4.8 深度學習和大腦的關聯性（What does this have to do with the brain?）

## 第二門課 改善深層神經網路：超參數除錯、正則化以及最佳化(Improving Deep Neural Networks:Hyperparameter tuning, Regularization and Optimization)

[第一週：深度學習的實踐層面(Practical aspects of Deep Learning) ](lesson2-week1.md)

1.1 訓練，驗證，測試集（Train / Dev / Test sets） 

1.2 偏差，方差（Bias /Variance） 

1.3 機器學習基礎（Basic Recipe for Machine Learning） 

1.4 正則化（Regularization）

1.5 為什麼正則化有利於預防過擬合呢？（Why regularization reduces overfitting?）

1.6 dropout 正則化（Dropout Regularization）

1.7 理解 dropout（Understanding Dropout）

1.8 其他正則化方法（Other regularization methods）

1.9 標準化輸入（Normalizing inputs）

1.10 梯度消失/梯度爆炸（Vanishing / Exploding gradients）

1.11 神經網路的權重初始化（Weight Initialization for Deep Networks） 

1.12 梯度的數值逼近（Numerical approximation of gradients）

1.13 梯度檢驗（Gradient checking）

1.14 梯度檢驗應用的注意事項（Gradient Checking Implementation Notes） 

[第二週：最佳化算法 (Optimization algorithms) ](lesson2-week2.md)

2.1 Mini-batch 梯度下降（Mini-batch gradient descent） 

2.2 理解Mini-batch 梯度下降（Understanding Mini-batch gradient descent）

2.3 指數加權平均（Exponentially weighted averages）

2.4 理解指數加權平均（Understanding Exponentially weighted averages） 

2.5 指數加權平均的偏差修正（Bias correction in exponentially weighted averages）

2.6 momentum梯度下降（Gradient descent with momentum）

2.7 RMSprop——root mean square prop（RMSprop）

2.8 Adam最佳化算法（Adam optimization algorithm）

2.9 學習率衰減（Learning rate decay）

2.10 局部最優問題（The problem of local optima）

[第三週超參數除錯，batch正則化和程序框架（Hyperparameter tuning, Batch Normalization and Programming Frameworks)](lesson2-week3.md) 

3.1 除錯處理（Tuning process） 

3.2 為超參數選擇和適合範圍（Using an appropriate scale to pick hyperparameters）

3.3 超參數除錯實踐：Pandas vs. Caviar（Hyperparameters tuning in practice: Pandas vs. Caviar）

3.4 網路中的正則化啟動函數（Normalizing activations in a network） 

3.5 將 Batch Norm擬合進神經網路（Fitting Batch Norm into a neural network）

3.6 為什麼Batch Norm奏效？（Why does Batch Norm work?）

3.7 測試時的Batch Norm（Batch Norm at test time）

3.8 Softmax 回歸（Softmax Regression）

3.9 訓練一個Softmax 分類器（Training a softmax classifier） 

3.10 深度學習框架（Deep learning frameworks） 

3.11 TensorFlow（TensorFlow） 

## 第三門課 結構化機器學習項目 (Structuring Machine Learning Projects) 

[第一週：機器學習策略（1）(ML Strategy (1))](lesson3-week1.md) 

1.1 為什麼是ML策略？ (Why ML Strategy) 

1.2 正交化(Orthogonalization) 

1.3 單一數字評估指標(Single number evaluation metric) 

1.4 滿足和最佳化指標 (Satisficing and Optimizing metric)

1.5 訓練集、開發集、測試集的劃分(Train/dev/test distributions) 

1.6 開發集和測試集的大小 (Size of the dev and test sets) 

1.7 什麼時候改變開發集/測試集和評估指標(When to change dev/test sets and metrics) 

1.8 為什麼是人的表現 (Why human-level performance?) 

1.9 可避免偏差(Avoidable bias) 

1.10 理解人類的表現 (Understanding human-level performance) 

1.11 超過人類的表現(Surpassing human-level performance) 

1.12 改善你的模型表現 (Improving your model performance) 

[第二週：機器學習策略（2）(ML Strategy (2))](lesson3-week2.md) 

2.1 誤差分析 (Carrying out error analysis) 

2.2 清除標註錯誤的數據(Cleaning up incorrectly labeled data) 

2.3 快速搭建你的第一個系統，並進行疊代(Build your first system quickly, then iterate) 

2.4 使用來自不同分布的數據，進行訓練和測試 (Training and testing on different distributions) 

2.5 數據分布不匹配時，偏差與方差的分析 (Bias and Variance with mismatched data distributions) 

2.6 處理數據不匹配問題(Addressing data mismatch) 

2.7 遷移學習 (Transfer learning) 

2.8 多任務學習(Multi-task learning) 

2.9 什麼是端到端的深度學習？ (What is end-to-end deep learning?) 

2.10 是否使用端到端的深度學習方法 (Whether to use end-to-end deep learning) 

##第四門課 卷積神經網路（Convolutional Neural Networks）	
[第一週 卷積神經網路(Foundations of Convolutional Neural Networks)](lesson4-week1.md) 

1.1	計算機視覺（Computer vision）

1.2	邊緣檢測範例（Edge detection example）

1.3	更多邊緣檢測內容（More edge detection）

1.4	Padding	

1.5	卷積步長（Strided convolutions）	

1.6	三維卷積（Convolutions over volumes）	

1.7	單層卷積網路（One layer of a convolutional network）	

1.8	簡單卷積網路範例（A simple convolution network example）	

1.9	池化層（Pooling layers）	

1.10 卷積神經網路範例（Convolutional neural network example）

1.11 為什麼使用卷積？（Why convolutions?）

[第二週 深度卷積網路：實例探究(Deep convolutional models: case studies)](lesson4-week2.md) 
2.1 為什麼要進行實例探究？（Why look at case studies?）

2.2 經典網路（Classic networks）

2.3 殘差網路(ResNets)（Residual Networks (ResNets)）

2.4 殘差網路為什麼有用？（Why ResNets work?）	

2.5 網路中的網路以及 1×1 卷積（Network in Network and 1×1 convolutions）

2.6 谷歌 Inception 網路簡介（Inception network motivation）	

2.7 Inception 網路（Inception network）	

2.8 使用開源的實現方案（Using open-source implementations）	

2.9 遷移學習（Transfer Learning）	

2.10 數據增強（Data augmentation）	

2.11 計算機視覺現狀（The state of computer vision）	

[第三週 目標檢測（Object detection）](lesson4-week3.md)
3.1 目標定位（Object localization）

3.2 特徵點檢測（Landmark detection）

3.3 目標檢測（Object detection）

3.4 滑動窗口的卷積實現（Convolutional implementation of sliding windows）

3.5 Bounding Box預測（Bounding box predictions）

3.6 交並比（Intersection over union）

3.7 非極大值抑制（Non-max suppression）

3.8 Anchor Boxes

3.9 YOLO 算法（Putting it together: YOLO algorithm）

3.10 候選區域（選修）（Region proposals (Optional)）

[第四周 特殊應用：人臉識別和神經風格轉換（Special applications: Face recognition &Neural style transfer）](lesson4-week4.md)
4.1 什麼是人臉識別？(What is face recognition?)

4.2 One-Shot學習（One-shot learning）

4.3 Siamese 網路（Siamese network）

4.4 Triplet 損失（Triplet 損失）

4.5 人臉驗證與二分類（Face verification and binary classification）

4.6 什麼是神經風格遷移？（What is neural style transfer?）

4.7 CNN特徵可視化（What are deep ConvNets learning?）

4.8 代價函數（Cost function）

4.9 內容代價函數（Content cost function）

4.10 風格代價函數（Style cost function）

4.11 一維到三維推廣（1D and 3D generalizations of models）

# 第五門課 序列模型(Sequence Models)

[第一週 循環序列模型（Recurrent Neural Networks）](lesson5-week1.md)
1.1 為什麼選擇序列模型？（Why Sequence Models?）

1.2 數學符號（Notation）

1.3 循環神經網路模型（Recurrent Neural Network Model）

1.4 通過時間的反向傳播（Backpropagation through time）

1.5 不同類型的循環神經網路（Different types of RNNs）

1.6 語言模型和序列生成（Language model and sequence generation）

1.7 對新序列採樣（Sampling novel sequences）

1.8 循環神經網路的梯度消失（Vanishing gradients with RNNs）

1.9 GRU單元（Gated Recurrent Unit（GRU））

1.10 長短期記憶（LSTM（long short term memory）unit）

1.11 雙向循環神經網路（Bidirectional RNN）

1.12 深層循環神經網路（Deep RNNs）

[第二週 自然語言處理與詞嵌入（Natural Language Processing and Word Embeddings）](lesson5-week2.md)
2.1 詞彙表徵（Word Representation）

2.2 使用詞嵌入（Using Word Embeddings）

2.3 詞嵌入的特性（Properties of Word Embeddings）

2.4 嵌入矩陣（Embedding Matrix）

2.5 學習詞嵌入（Learning Word Embeddings）

2.6 Word2Vec

2.7 負採樣（Negative Sampling）

2.8 GloVe 詞向量（GloVe Word Vectors）

2.9 情緒分類（Sentiment Classification）

2.10 詞嵌入除偏（Debiasing Word Embeddings）

[第三週 序列模型和注意力機制（Sequence models & Attention mechanism）](lesson5-week3.md)

3.1 基礎模型（Basic Models）

3.2 選擇最可能的句子（Picking the most likely sentence）

3.3 集束搜索（Beam Search）

3.4 改進集束搜索（Refinements to Beam Search）

3.5 集束搜索的誤差分析（Error analysis in beam search）

3.6 Bleu 得分（選修）（Bleu Score (optional)）

3.7 注意力模型直觀理解（Attention Model Intuition）

3.8注意力模型（Attention Model）

3.9語音識別（Speech recognition）

3.10觸發字檢測（Trigger Word Detection）

3.11結論和致謝（Conclusion and thank you）

**附件**

[人工智慧大師訪談](interview.md)

吳恩達採訪 Geoffery Hinton

吳恩達採訪 Ian Goodfellow

吳恩達採訪 Ruslan Salakhutdinov

吳恩達採訪 Yoshua Bengio

吳恩達採訪 林元慶

吳恩達採訪 Pieter Abbeel	

吳恩達採訪 Andrej Karpathy

[深度學習符號指南（原課程翻譯）](notation.md)

[機器學習的數學基礎](notation.md)




