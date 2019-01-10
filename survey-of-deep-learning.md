---
description: >-
  Yann LeCun, Yoshua Bengio & Geoffrey Hinton
  https://www.nature.com/articles/nature14539
---

# Survey of Deep Learning

## **Deep Learning**

Humans have always tried to make tools that are better, faster and more efficient for some tasks. The rise of machine learning in past some years have a great implication in the human achievements. Machine learning is efficient in some areas while on other it cannot promise much. They were limited by the ability to perform on the natural data. Hand-engineered features are required for many tasks for it to perform better.

Pre-requisite: 

 Deep learning is a class of computational model that can learn the representations of the data in their natural form. Deep learning employs neural networks to base the decisions. They are composed of the multiple processing neural layers which are better at extracting different abstract information from the data. Deep learning discovers the intricate structures in the data through an algorithm called “back propagation”. There are different architectures of neural network depending on the type of problem it’s trying to solve. Deep learning is making major advances in solving problems that were deemed very tough by artificial intelligence community. It can analyze the videos, images and generate artwork. Natural Language processing is another area where deep learning algorithms are used widely. They are being used in many domains like science, business and government.

**The basic philosophy of deep learning is that with enough layers** that consistently represent data more abstractly any non-linear models can be computed. Neural networks can act as any logical functions like OR, AND, NAND gates. Deep-learning methods are representation-learning methods with multiple levels of representation, obtained by composing simple but non-linear modules that each transform the representation at one level \(starting with the raw input\) into a representation at a higher, slightly more abstract level. For example, suppose in the theatre near your place, they are showing a new movie. You love romantic movies. You want to go but are unsure is the movie worth it. So, you weight it with following three questions:

a\)     Is the movie romantic?

b\)    Is the weather good enough?

c\)     Is it cheap?

You just acted like a neural network. Those three questions are like different layers in the neural network. You can go to theatre if the movie is romantic even the weather is bad. This means you are giving more weight to first question. Neural Network learn the representation of the data by tuning and updating the weights.

Neural Networks can be used as learning algorithms. Instead of manually updating the weights we can update the weights based on what we want to learn about. For example, we want to learn how is the price of M&M’s increase whenever there is mild climate. We can collect the data of the actual sales and the mild weather. Now, we pass the climate data and try to approximate the price value by increasing or decreasing the internal parameters and weights. Our machine will give us some price, we can compare it with actual price and see the error. We can collect such errors and plot it and find a function such that we can find the what could be the minimum error and choose the weight and parameters of neural layers when we predicted the price. This is a classic way of learning called supervised learning. Neural networks are suitable for supervised learning. The above-mentioned way of learning is perfectly valid but it imposes a major hurdle, what if the dataset is bigger than human can compute. The answer is use a computer. What if the dataset is bigger for the machine too?

The answer lies in taking a group of datasets which machine can compute error for and try to do the same for different small samples and average their errors. It is the way modern neural networks compute errors on a big dataset. It is called Stochastic gradient descent. The computing of gradients is done using a “back propagation rule”, which is simply a chain rule of derivative of output error function with respect to the weights of different layers. This algorithm gives network a sense of how does the error change with respect of weights and bias of neural layers. We can do this way of approximating with the simple one layer neural network but complex problems like image recognitions or diagnosing diseases requires more complex neural network architectures.

 A neural network architecture is composed of several layers of neural network. The left most neural layer is called input layer while the right most layer is called output layer. The layer in between these two layers is called hidden layers. One can have as many as hidden layers as the problems wants. Since the layers of networks can be as deep as one want it’s called deep neural networks. The design of input and output layer is straightforward but the design of hidden layers have different kinds of arts in it. The simplest design is called feedforward neural network architecture. If the design contains loops, extra logical gates. These types of neural network are called recurrent neural networks. Recurrent neural networks are used on sequence data like time series analysis, sentences. There is other type of neural networks that have different architectures. Like a recurrent neural network have loops inside it, the convolutional networks have convolutions inside it. Convolutions are the mathematical operations like multiplications and addition of all those multiplications. It computes a function from two different functions. A multiplication is a child convolution which forgets the past and does whatever given to it but the convolution remembers the functions and give different result next time.

These different architectures of neural networks are good on different domains of problems. In future, these architectures are only going to be more sophisticated and better at tasks that require focus, memory, beliefs and attentions. Researchers are trying to adapt the neural network that are better at paying attention to specific tasks. Deep learning algorithms are building a ladder that can take us to Artificial general intelligence as better as humans. Artificial Intelligence will come through systems that combine representation learning with complex reasoning.

Citations



