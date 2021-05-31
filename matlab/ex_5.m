%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%   @ Authors : SEKHRI Aymen
%               MOHAMMED HACENE Tarek
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

close all 
clear all 
clc

% Load image 
x = imread('rose.jpeg');

% extract (r--> height) (c--> width) (w--> channels) 
[r,c,w] = size(x);

% Maximum possible number of intensity values used in the quantization of the original image 
B = 256;

% q = 4
% q = 8
% q = 14

% desired Maximum possible number of intensity values used in the quantization of the new image 
q = input('Enter the number of quantization values:')

% (l) devides the interval [0-255] into multiple ranges , each range has lenght of (l)
l = B / q ;

% Array of zeros 
E = zeros(256, 1);

% Generate the quantization function 
for i = 0:255,
 E(i+1, 1) = floor(i / l) *l + l/2 ;
end

% Plot the quantization function
figure; plot(0:255,E);

% Genrate a black image with same size of the original image 
y = zeros(size(x));

% Generate the new image with the new intensity values
for ch = 1:w
 for i = 1:r,
  for j = 1:c,
    y(i, j,ch) = E(x(i,j,ch) + 1);
  end
 end
end

% plot the new image
figure(2); imagesc(uint8(y))