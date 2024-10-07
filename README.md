# Bi-GRU-Deception-Detection-EEG
Bi-GRU Based Deception Detection Using EEG Signals

Deception detection is a critical challenge in fields such as security, psychology, and
 forensic investigations. It plays a crucial role in upholding ethical ethical integrity
 in society and preventing national security risks. This study presents a novel
 approach for deception detection using electroencephalogram (EEG) data, leveraging
 a Bidirectional Gated Recurrent Unit (Bi-GRU) neural network to classify truthful
 and deceptive responses. We utilized a comprehensive
 dataset of EEG recordings designed for casual deception. Preprocessing involved
 data cleaning, bandpass filtering, and segmentation to generate representative and
 relevant training samples. To enhance model performance, we balanced samples
 across the two classes, and to increase generalization and robustness, we augmented
 data by introducing Gaussian noise. The proposed Bi-GRU architecture encompasses
 three BiGRU layers, each designed to capture complex temporal dependencies within
 the EEG signals. These recurrent layers are interspersed with dropout layers to
 prevent overfitting by randomly deactivating a fraction of neurons during training,
 and are followed by multiple dense layers to reduce the dimensionality of the learned
 features and refine the model’s predictions. Training was done using 5-fold cross
validation, with early stopping to prevent overfitting and ensure optimal convergence.
 Our Bi-GRU based approach achieved an accuracy of 97% in distinguishing between
 truthful and deceptive EEG signals. Additionally, the model demonstrated high
 precision, recall, and F1-scores, indicating reliable performance across both classes.
 These results underscore the effectiveness and robustness of our study, that not
 only advances the state-of-the-art in EEG based deception detection, but also opens
 avenues for further research into more sophisticated neural architectures and real-time
 application scenarios.
