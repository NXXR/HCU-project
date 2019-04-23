# [Taskonomy: Disentangling Task Transfer Learning](https://arxiv.org/abs/1804.08328)
*by A. Zamir, A. Sax, W. Shen, L. Guibas, J. Malik, and S. Savarese*

##### Introduction
- finding complex f: X→Y, when many x∈X, y∈Y are given as training data in fully supervised learning is usally very successful
- isolated training of tasks or comprehensive perception system often a lot of minute work, as every task has to be learned individually
    - this ignores their relationships and leads to massive labeled data requirements
    - model aware of the relationships demands less supervision, less computation, and it behaves in more predictable ways
    - relationships are non-trivial and complicated to find
- feed-forward network, each layer successively forms more abstract representations of the input, containing the information for mapping the input to the output
    - representations can be useful for multiple outputs (tasks) if tasks are related
    
=> affinity matrix among tasks based on ability to be derived from representation of different task
- solving tasks  with far less data compared to individual training
    - avoids imposing prior assumptions on task space