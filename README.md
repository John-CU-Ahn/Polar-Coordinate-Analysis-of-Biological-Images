# Principal-Component-Analysis-of-Biological-Images

## Description
Principal component analysis (PCA) is a powerful dimensionality reduction technique that reduces a large amount of variables that could explain trends in data to just a few parameters.
With my project, I had 360 dimensions describing the shape of a cancer cell over time, and I used PCA to reduce those dimensions to just 8 parameters that explained over 70% of the variance in the data.
This code can be used for any image-based analysis describing object shape changes over time.

## Implementation
The input data must be a matrix compiling all of the polar coordinate descriptions of an object over time and across different experimental conditons. This particular code is designed for a csv file.

Type in the file directory leading to your input csv file into the "Polar coordinate description.py" script. The script will locate the center of the object, collect a series of line profiles containing pixel values sweeping out from the center point, and then calculate the radii associated with each degree (theta value). It will output a csv file of each radii at each degree over time.

The "Polar coordinate graphs.py" file will generate graphs of the radii from the csv file.

The "Make movie.py" file will generate a movie of the polar coordinate graphs in an mp4 file.

The "Polar coordinate graph movie.mp4" file showcases the polar coordinate graphs generated from the tif file used to create the "Thresholded p collini cell.avi" movie file.
