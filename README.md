# Geo-Guesser

> **_What is Geoguessr?_**
Geoguessr is an online game that places you on a random street in the world. You can move around (using Google Street View), and your job is to guess what location you are in.

_**Main Idea:** Alex and I wanted to build a deep neural network model that could accurately predict the country where a picture was taken._

<img width="778" alt="Screenshot 2023-12-19 at 9 55 26 PM" src="https://github.com/alankct/Geo-Guesser/assets/86837040/fb183157-c524-4340-a8f8-01b3ea7ec55d">

> Our work in this project exposed us to the complex problems of Machine Learning and Computer Vision, and we gained valuable skills and insights into the world of data, problem complexity, and performance optimization.

## Results
**_Our work led to a systematic (and creative) development of balanced data, an accurate country predictor model, as well as a performance optimization that reduced our epoch training time from 30 minutes down to 5 minutes (which can be applied to any model that uses transfer learning)._**

## Data
Initally, our geographical data (image) distribution looked like this:

<img width="910" alt="Screenshot 2023-12-19 at 10 03 47 PM" src="https://github.com/alankct/Geo-Guesser/assets/86837040/e8432d9b-e152-4cb2-90be-beb1959a3cf7">

After appending and making changes to our dataset, filtering images from outlier countries, calling 15,000 Google Maps API requests using a coordinates dataset, using a custom (uniform vs not-uniform) balancing dataset, and mapping our distributions to the overall Google Maps distribution, our data distribution now looked like this:

<img width="898" alt="Screenshot 2023-12-19 at 10 08 50 PM" src="https://github.com/alankct/Geo-Guesser/assets/86837040/2cc17641-fac0-47c1-835e-7fe4729c5074">

## Performance
Because we had accumulated a dataset of around 100,000 images, our training was slow and expensive. We tackled performance issues by optimizing our transfer learning—and using tensors instead of images. Using a ResNet152 backbone, and our own classification model—we were able to speed epochs by 83%. We did this by creating a new dataset of tensors with the extracted features from ResNet.

<img width="824" alt="Screenshot 2023-12-19 at 10 19 27 PM" src="https://github.com/alankct/Geo-Guesser/assets/86837040/48b1b779-69e1-485f-82c3-aa6d0e265bd8">
