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

% store height , width , channels 
[row, col, chs] = size(onion_img)

% retreive image info ( spacial + spectral resolutions)
whos onion_img

% Translate image to the right by 20 cols
a = imtranslate(onion_img,[20, 0]);
figure(1)
imshowpair(onion_img,a,'montage')
title("translation to the right by 20 cols ")

% Translate image to the right by 50 lines + 100 cols 
b = imtranslate(onion_img,[100, 50]);
figure(2)
imshowpair(onion_img,b,'montage')
title("translation to the right by 50 lines | 100 cols ")

% Translate image to hide the papper  
c = imtranslate(onion_img,[40, 40]);

% plot the image
figure(3)
imshowpair(onion_img,c,'montage')
title("translation to hide the papper ")