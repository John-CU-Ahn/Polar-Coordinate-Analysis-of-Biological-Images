# Principal-Component-Analysis-of-Biological-Images
![PC1-4](https://github.com/John-CU-Ahn/Principal-Component-Analysis-of-Biological-Images/assets/140204157/f04bb162-9b1f-491c-b9b6-b75c42d695e0)

## Description
Principal component analysis (PCA) is a powerful dimensionality reduction technique that reduces a large amount of variables that could explain trends in data to just a few parameters.
With my project, I had 360 dimensions describing the shape of a cancer cell over time, and I used PCA to reduce those dimensions to just 8 parameters that explained over 70% of the variance in the data.
This code can be used for any image-based analysis describing object shape changes over time.

## Implementation
The input data must be a matrix compiling all of the polar coordinate descriptions of an object over time and across different experimental conditons. This particular code is designed for a csv file.

Type in the file directory leading to your input csv file into the "Calculating principal components.py" script. The script will calculate the eigenvalues and associated eigenvectors that will explain the variance in the data, select the top eight eigenvectors, and save them as a csv file.

The "Generating PC weights.py" file will generate associated principal component (PC) weights with each of the eigenvectors from the previous script by applying them to the actual radii of the contour of interest, along with the average shape of the contour of interest over time. This script will need three inputs: first the principal components themselves, then the actual radii of the contour of interest, and then the average shape all as csv files.

The "Graphing PC weights.py" file will generate two graphs of the top eight principal component weights over time, using the output file from the previous script.

The "Top eight eigenvectors.jpeg" file is an image of the top eight eigenvectors calculated from example data.
![Top eight eigenvectors](https://github.com/John-CU-Ahn/Principal-Component-Analysis-of-Biological-Images/assets/140204157/0ca374ec-fb05-4f05-8730-c6ef5d6af8e3)

The "Percent variance explained.jpeg" file shows the top fifty eigenvectors/principal components ranked by percent variance of the data explained.
![Percent variance explained](https://github.com/John-CU-Ahn/Principal-Component-Analysis-of-Biological-Images/assets/140204157/a7f9a0d8-ebe6-49c2-bd46-480f389a1aac)

The "PC1-4.jpg" and "PC5-8.jpg" files show the PC weights generated over time.
![PC1-4](https://github.com/John-CU-Ahn/Principal-Component-Analysis-of-Biological-Images/assets/140204157/f04bb162-9b1f-491c-b9b6-b75c42d695e0)
![PC5-8](https://github.com/John-CU-Ahn/Principal-Component-Analysis-of-Biological-Images/assets/140204157/6488e121-d8a1-4040-9454-a4c58663accd)
