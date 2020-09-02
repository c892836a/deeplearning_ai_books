**Coursera深度學習教學中文筆記**

課程概述

https://mooc.study.163.com/university/deeplearning_ai#/c

[**筆記線上閱讀**](http://www.ai-start.com/dl2017)

這些課程專為已有一定基礎（基本的程式知識，熟悉**Python**、對機器學習有基本了解），想要嘗試進入人工智慧領域的計算機專業人士準備。介紹顯示：“深度學習是科技業最熱門的技能之一，本課程將幫你掌握深度學習。”

在這5堂課中，學生將可以學習到深度學習的基礎，學會構建神經網路，並用在包括吳恩達本人在內的多位業界頂尖專家指導下創建自己的機器學習項目。**Deep Learning Specialization**對卷積神經網路 (**CNN**)、遞迴神經網路 (**RNN**)、長短期記憶 (**LSTM**) 等深度學習常用的網路結構、工具和知識都有涉及。

課程中也會有很多實操項目，幫助學生更好地應用自己學到的深度學習技術，解決真實世界問題。這些項目將涵蓋醫療、自動駕駛、和自然語言處理等時髦領域，以及音樂生成等等。**Coursera**上有一些特定方向和知識的資料，但一直沒有比較全面、深入淺出的深度學習課程——《深度學習專業》的推出補上了這一空缺。

課程的語言是**Python**，使用的框架是**Google**開源的**TensorFlow**。最吸引人之處在於，課程導師就是吳恩達本人，兩名助教均來自斯坦福計算機系。完成課程所需時間根據不同的學習進度，大約需要3-4個月左右。學生結課後，**Coursera**將授予他們**Deep Learning Specialization**結業證書。

“我們將幫助你掌握深度學習，理解如何應用深度學習，在人工智慧業界開啟你的職業生涯。”吳恩達在課程頁面中提到。

本人黃海廣博士，以前寫過吳恩達老師的機器學習個人筆記。目前我正在組織團隊整理中文筆記，由熱心的朋友無償幫忙製作整理，並持續更新。我們的團隊的工作致力於**AI**在國內的推廣，不會損害**Coursera**以及吳恩達老師的商業利益。

本人水平有限，如有公式、算法錯誤，請及時指出，發郵件給我。

**筆記是根據影片和字幕寫的，沒有技術含量，只需要專注和嚴謹。**

黃海廣

[我的知乎](https://www.zhihu.com/people/fengdu78/activities)

機器學習qq群：1003271085（我們有10個群，加過一個就不需要加了）

微信公眾號：機器學習初學者 ![gongzhong](images/gongzhong.jpg)
知識星球：黃博的機器學習圈子![xingqiu](images/zhishixingqiu1.jpg)

**注意：github下載太慢的話，關注我的公眾號：“機器學習初學者”，回復“github鏡像”即可下載本倉庫的鏡像文件，整個倉庫壓縮成一個iso。**

[我的知乎](https://www.zhihu.com/people/fengdu78/)

**主要編寫人員**：黃海廣、林興木（第四所有底稿，第五課第一二週，第三週前三節）、祝彥森:（第三課所有底稿）、賀志堯（第五課第三週底稿）、覃立波、王翔、胡瀚文、 余笑、 鄭浩、李懷松、 朱越鵬、陳偉賀、 曹越、 路皓翔、邱牧宸、 唐天澤、 張浩、 陳志豪、 游忍、 澤霖、沈偉臣、 賈紅順、 時超、 陳哲、趙一帆、 胡瀟楊、段希、於沖、張鑫倩

**參與編輯人員**：黃海廣、陳康凱、石晴路、鍾博彥、向偉、嚴鳳龍、劉成 、賀志堯、段希、陳瑤、林家泳、王翔、 謝士晨、蔣鵬

2018-04-14

**本課程影片教學地址：**<https://mooc.study.163.com/university/deeplearning_ai#/c>

**有同學提供了一個離線影片的下載**：連結：https://pan.baidu.com/s/1ciq3qHo0lgoD3MLRwfeqnA 密碼：0kim

（該影片從www.deeplearning.ai 網站下載，因眾所周知的原因，國內用戶觀看某些線上影片非常不容易，故一些學者一起製作了離線影片，旨在方便國內用戶個人學習使用，請勿用於商業用途。影片內嵌中英文字幕，推薦使用**potplayer**播放。版權屬於吳恩達老師所有，若在線影片軌暢，請到官方網站觀看。）

[筆記網站(適合手機閱讀)](http://www.ai-start.com)

吳恩達老師的機器學習課程筆記和影片：https://github.com/fengdu78/Coursera-ML-AndrewNg-Notes

**此文件免費，請不要用於商業用途，可以自由傳播。**

**贈人玫瑰，手有餘香！**

haiguang2000@qq.com

**轉載請註明出處**：https://github.com/fengdu78/deeplearning_ai_books

**機器學習qq群：1003271085（我們有10個群，加過一個就不需要加了，若滿員這個群會有提示新群號）** 

# 深度學習筆記目錄

## 第一門課 神經網路和深度學習(Neural Networks and Deep Learning)

第一週：深度學習引言(Introduction to Deep Learning) 

1.1 歡迎(Welcome)

1.2 什麼是神經網路？(What is a Neural Network) 

1.3 神經網路的監督學習(Supervised Learning with Neural Networks) 

1.4 為什麼神經網路會流行？(Why is Deep Learning taking off?) 

1.5 關於本課程(About this Course) 

1.6 課程資源(Course Resources) 

1.7 Geoffery Hinton 專訪(Geoffery Hinton interview) 

第二週：神經網路的程式基礎(Basics of Neural Network programming) 

2.1 二分類(Binary Classification) 

2.2 邏輯回歸(Logistic Regression) 

2.3 邏輯回歸的代價函數（Logistic Regression Cost Function） 

2.4 梯度下降（Gradient Descent） 

2.5 導數（Derivatives）

2.6 更多的導數例子（More Derivative Examples） 

2.7 計算圖（Computation Graph）

2.8 計算圖導數（Derivatives with a Computation Graph） 

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

第三週：淺層神經網路(Shallow neural networks)

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

第四周：深層神經網路(Deep Neural Networks)

4.1 深層神經網路（Deep L-layer neural network） 

4.2 前向傳播和反向傳播（Forward and backward propagation） 

4.3 深層網路中的前向和反向傳播（Forward propagation in a Deep Network）

4.4 核對矩陣的維數（Getting your matrix dimensions right） 

4.5 為什麼使用深層表示？（Why deep representations?）

4.6 搭建神經網路塊（Building blocks of deep neural networks）

4.7 參數VS超參數（Parameters vs Hyperparameters） 

4.8 深度學習和大腦的關聯性（What does this have to do with the brain?）

## 第二門課 改善深層神經網路：超參數除錯、正則化以及最佳化(Improving Deep Neural Networks:Hyperparameter tuning, Regularization and Optimization)

第一週：深度學習的實用層面(Practical aspects of Deep Learning) 

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

1.11 神經網路的權重初始化（Weight Initialization for Deep NetworksVanishing /Exploding gradients） 

1.12 梯度的數值逼近（Numerical approximation of gradients）

1.13 梯度檢驗（Gradient checking）

1.14 梯度檢驗應用的注意事項（Gradient Checking Implementation Notes） 

第二週：最佳化算法 (Optimization algorithms) 

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

第三週超參數除錯，batch正則化和程序框架（Hyperparameter tuning, Batch Normalization and Programming Frameworks)

3.1 除錯處理（Tuning process） 

3.2 為超參數選擇和適合範圍（Using an appropriate scale to pick hyperparameters）

3.3 超參數訓練的實踐：Pandas vs. Caviar（Hyperparameters tuning in practice: Pandas vs. Caviar）

3.4 網路中的正則化啟動函數（Normalizing activations in a network） 

3.5 將 Batch Norm擬合進神經網路（Fitting Batch Norm into a neural network）

3.6 為什麼Batch Norm奏效？（Why does Batch Norm work?）

3.7 測試時的Batch Norm（Batch Norm at test time）

3.8 Softmax 回歸（Softmax Regression）

3.9 訓練一個Softmax 分類器（Training a softmax classifier） 

3.10 深度學習框架（Deep learning frameworks） 

3.11 TensorFlow（TensorFlow） 

## 第三門課 結構化機器學習項目 (Structuring Machine Learning Projects)

第一週：機器學習策略（1）(ML Strategy (1))

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

第二週：機器學習策略（2）(ML Strategy (2))

2.1 誤差分析 (Carrying out error analysis) 

2.2 清除標註錯誤的數據(Cleaning up incorrectly labeled data) 

2.3 快速搭建你的第一個系統，並進行疊代(Build your first system quickly, then iterate) 

2.4 在不同的分布上的訓練集和測試集 (Training and testing on different distributions) 

2.5 數據分布不匹配的偏差與方差分析 (Bias and Variance with mismatched data distributions) 

2.6 處理數據不匹配問題(Addressing data mismatch) 

2.7 遷移學習 (Transfer learning) 

2.8 多任務學習(Multi-task learning) 

2.9 什麼是端到端的深度學習？ (What is end-to-end deep learning?) 

2.10 是否使用端到端的深度學習方法 (Whether to use end-to-end deep learning) 

## 第四門課 卷積神經網路（Convolutional Neural Networks）

第一週 卷積神經網路(Foundations of Convolutional Neural Networks)

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

第二週 深度卷積網路：實例探究(Deep convolutional models: case studies)

2.1 為什麼要進行實例探究？（Why look at case studies?）

2.2 經典網路（Classic networks）

2.3 殘差網路（Residual Networks (ResNets)）

2.4 殘差網路為什麼有用？（Why ResNets work?）	

2.5 網路中的網路以及 1×1 卷積（Network in Network and 1×1 convolutions）

2.6 谷歌 Inception 網路簡介（Inception network motivation）	

2.7 Inception 網路（Inception network）	

2.8 使用開源的實現方案（Using open-source implementations）	

2.9 遷移學習（Transfer Learning）	

2.10 數據擴充（Data augmentation）	

2.11 計算機視覺現狀（The state of computer vision）	

第三週 目標檢測（Object detection）

3.1 目標定位（Object localization）

3.2 特徵點檢測（Landmark detection）

3.3 目標檢測（Object detection）

3.4 卷積的滑動窗口實現（Convolutional implementation of sliding windows）

3.5 Bounding Box預測（Bounding box predictions）

3.6 交並比（Intersection over union）

3.7 非極大值抑制（Non-max suppression）

3.8 Anchor Boxes

3.9 YOLO 算法（Putting it together: YOLO algorithm）

3.10 候選區域（選修）（Region proposals (Optional)）

第四周 特殊應用：人臉識別和神經風格轉換（Special applications: Face recognition &Neural style transfer）

4.1 什麼是人臉識別？(What is face recognition?)

4.2 One-Shot學習（One-shot learning）

4.3 Siamese 網路（Siamese network）

4.4 Triplet 損失（Triplet 損失）

4.5 臉部驗證與二分類（Face verification and binary classification）

4.6 什麼是神經風格轉換？（What is neural style transfer?）

4.7 什麼是深度卷積網路？（What are deep ConvNets learning?）

4.8 代價函數（Cost function）

4.9 內容代價函數（Content cost function）

4.10 風格代價函數（Style cost function）

4.11 一維到三維推廣（1D and 3D generalizations of models）

# 第五門課 序列模型(Sequence Models)

第一週 循環序列模型（Recurrent Neural Networks）
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

第二週 自然語言處理與詞嵌入（Natural Language Processing and Word Embeddings）

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

第三週 序列模型和注意力機制（Sequence models & Attention mechanism）

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

人工智慧大師訪談

吳恩達採訪 Geoffery Hinton

吳恩達採訪 Ian Goodfellow

吳恩達採訪 Ruslan Salakhutdinov

吳恩達採訪 Yoshua Bengio

吳恩達採訪 林元慶

吳恩達採訪 Pieter Abbeel	

吳恩達採訪 Andrej Karpathy

附件

深度學習符號指南（原課程翻譯）



