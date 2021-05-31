%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%   @ Authors : SEKHRI Aymen
%               MOHAMMED HACENE Tarek
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

close all 
clear all 
clc 

image_name = 'onion.png'

% load image
onion_img = imread(image_name)

% rotate image 45° anticlockwise
rotated = imrotate(onion_img,45)

% plot the image
figure(1)
imshow(rotated)
title("Rotated image 45° anticlockwise")