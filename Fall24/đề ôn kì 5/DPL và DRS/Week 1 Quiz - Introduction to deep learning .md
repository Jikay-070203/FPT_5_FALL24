## Week 1 Quiz - Introduction to deep learning

### 1. Which of the following best describes the role of AI in the expression "an AI-powered society"?

- [x] **AI is an essential ingredient in realizing tasks, in industry and in personal life.**
      📌 In an AI powered society AI plays a fundamental role to complete most tasks, in industry and personal life.

### 2. Which of the following play a major role to achieve a very high level of performance with Deep Learning algorithms?

<!-- - [ ] Deep learning has resulted in significant improvements in important applications such as online advertising, speech recognition, and image recognition.
- [ ] Better designed features to use. -->

- [x] **Large models.**
- [x] **Large amounts of data.**
      📌 Some of the most successful Deep Learning algorithms make use of very large datasets for training.

### 3. Recall this diagram of iterating over different ML ideas. Which of the statements below are true? (Check all that apply.)

![image](https://user-images.githubusercontent.com/55765292/173260545-6cb50c32-b90c-4ec6-ae7d-df4e94b5f6c6.png)

- [x] **Improvements in the GPU/CPU hardware enable the discorvery of better Deep Learning algorithms.**
      📌 By speeding up the iterative process, better hardware allows researchers to discover better algorithms.
- [x] **Better algorithms can speed up the iterative process by reducing the necessary computation time.**
      📌 Recall how the introduction of the ReLU activation function helped resuce the time needed to train a model
- [x] **Being able to try out ideas quickly allows deep learning engineers to iterate more quickly.**
- [x] **Faster computation can help speed up how long a team takes to iterate to a good idea.**
- [x] **Experiments finish faster, producing better ideas through increased iteration tempo.**
      📌 The experiments help to test ideas, by getting the feedback from the experiments new variations can be tested can be tested and the results might indicate new directions to explore.
- [x] **Some algorithms are specifically designed to run experiments faster**
      📌 Some algorithms look specifically to improve the time needed to run an experiment and thus enable us to produce better models.

### 4. When experienced deep learning engineers work on a new problem, they can usually use insight from previous problems to train a good model on the first try, without needing to iterate multiple times through different models. True/False?

- [x] **False**
      📌 Finding the characteristics of model is key to having good performance. Although experience can help, it requires multiple iterations to build a good model.

```

```

### 5. Which one of these plots represents a ReLU activation function?

![image](https://user-images.githubusercontent.com/55765292/173262212-6426657a-cd2b-44ce-b58d-15448027b428.png)

```
📌 this is the ReLU activation function, the most used in neural networks.
```

### 6. Features of animals, such as weight, height, and color, are used for classification between cats, dogs, or others. This is an example of "structured" data, because they are represented as arrays in a computer. True/False?

- [x] **True**

```
📌 The data can be represented by columns of data. This is an example of structed data, unlike images of the animal.
```

- [ ] False

### 7. A demographic dataset with statistics on different cities' population, GDP per capita, and economic growth is an example of “unstructured” data because it contains data coming from different sources. True/False?

- [x] **False**
      📌 A demographic dataset with statistics on different cities' population, GDP per capita, and economic growth is an example of "structured" data in contrast to image, audio or text datasets.

### 8. Why is an RNN (Recurrent Neural Network) used for machine translation, say translating English to French? (Check all that apply.)

- [x] **It can be trained as a supervised learing problem**
      📌 We can train it on many pairs of sentences x (English) and y (French).
- [x] **It is applicable when the input/output is a sequence (e.g. a sequence of words.)**
      📌 An RNN can map from a sequence of english words to a sequence of french words.

### 9. In this diagram which we hand-drew in the lecture, what do the horizontal axis (x-axis) and vertical axis (y-axis) represent?

![image](https://user-images.githubusercontent.com/55765292/173261185-507beea7-d91a-4319-9eb0-8605ec2ffb9a.png)

- [x] **x-axis is the amount of data, y-axis (vertical axis) is the performance of the algorithm.**

### 10. Assuming the trends described in the previous question's figure are accurate (and hoping you got the axis labels right), which of the following are true? (Check all that apply.)

![image](https://user-images.githubusercontent.com/55765292/173262590-80993397-ddfb-4657-8cc7-eec66e230f91.png)

- [x] \*\*Increasing the size of a neural network generally does not hurt an algorithm's performance, and it may help signific
      📌 After a certain size, traditional learning algorithms don't improve their performance.

- [x] **Increasing the training set size of a traditional learning algorithm stops helping to improve the performance after a certain size.**
- [x] \*\*Suppose the information given in the diagram is accurate. We can deduce that when using large training sets, for a mod//////

### 11. Which of the following are reasons that didn't allow Deep Learning to be developed during the '80s?

- [x] **Interesting applications such as image recognition require large amounts of data that were not available.**

```
📌 Many resources used today to train Deep Learning projects come from the fact that our society digitizes almost everythin, creating a large dataset to train Deep Learning models.
```

- [x] **Limited computational power.**

```
📌 Deep Learning methods need a lot of computational power, and only recently the use of GPUs has accelerated the experimentation with Deep Learning.
```

- [ ] People were afraid of a machine rebellion.
- [ ] The theoretical tools didn't exist during the 80's.

### 12. Neural networks are good at figuring out function relating an input $x$ to an output $y$ given enough examples. True/False?

- [x] **True**

```
📌 Exactly, with neural networks, we don't need to "design" features by ourselves. The neural network figures out the necessary relations given enough data.
```

- [ ] False

### 13. Which of the following depicts a Sigmoid activation function?

![image](https://user-images.githubusercontent.com/55765292/173263549-eed235d6-a48b-4a32-9376-cc681ad3b120.png)

```
📌 This is the sigmoid activation function; this function was changed for the ReLU activation function helping with the training of NN.
```

### 14. Images for cat recognition is an example of “structured” data, because it is represented as a structured array in a computer. True/False?

- [x] **False**
      📌 Images for cat recognition are example of "unstructured" data.

### 15. What does the analogy “AI is the new electricity” refer to?

- [x] **Similar to electricity starting about 100 years ago, AI is transforming multiple industries.**
      📌 AI is transforming many fields from the car industry to agriculture to supply-chanin...

### 16. When building a neural network to predict housing price from features like size, the number of bedrooms, zip code, and wealth, it is necessary to come up with other features in between input and output like family size and school quality. True/False?

- [ ] True
- [x] **False**

```
📌 Recall that when training a neural network, only the input and output for several examples are given.
```

### 17. Which of the following are examples of structured data? Choose all that apply.

- [x] **A dataset with zip code, income, and name of a person.**
- [ ] A dataset with short poems.
- [x] **A dataset of weight, age, the sugar, level in the blood, and arterial pressure.**
- [ ] A set of audio recordings of a person saying a single word.

### 18. Which of these are reasons for Deep Learning recently taking off? (Check the three options that apply.)

- [x] **We have access to a lot more computational power.**
      📌 The develpoment of hardware, perhaps especially GPU computing, has significantly improved deep learning algorithms' performance.
- [x] **Deep learning has resulted in significant improvements in important applications such as online advertising, speech recognition, and image recognition.**
- [x] **We have access to a lot more data.**
      📌 The digitalization of our society has played a huge role in this.

### 19. Which of the following are some aspects in which AI has transformed business?

- [ ] Creating an AI-powered society.
- [ ] Eliminating the need for health care services.
- [x] **Web searching and advertisement.**

```
📌 AI has helped to make a fit between services or results and consumers or queries.
```

- [ ] AI has not been able to transform businesses.

### 20. RNNs (Recurrent Neural Networks) are good for data with a temporal component. True/False?

- [x] **True**
- [ ] False

```
📌 RNN are good to work with sequences, and the elements of the sequence can be sorted by a temporal component.
```

### 21. Which of the following are examples of unstructured data? Choose all that apply.

- [ ] Text describing size and number of pages of books.
- [x] **Sound files for speech recognition.**

```
📌 Audio is an example of "unstructured" data.
```

- **[x] Images for bird recognition.**

```
📌 Images are an example of "unstructured" data.
```

- [ ] Information about elephants'weight, height, age, and the number of offspring.
