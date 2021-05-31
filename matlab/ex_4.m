%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%   @ Authors : SEKHRI Aymen
%               MOHAMMED HACENE Tarek
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

close all 
clear all 
clc 

image_name = 'rose.jpeg'

% load image
rose_img = imread(image_name)

% resize image using "nearest methode" interpolation 
resized_img = imresize(rose_img,[512,512],'nearest');

% plot original image
figure(1) 
imshow(rose_img);
title('original image')

% plot resized image
figure(2) 
imshow(resized_img);
title('resized + interpolated image with "nearest methode"') 