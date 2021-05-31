%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%   @ Authors : SEKHRI Aymen
%               MOHAMMED HACENE Tarek
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


clc 
close all
clear all

I = imread('rose.jpeg'); % load image 
[j, k,c] = size(I); % extract height , width , channles , from loaded image 

scale = 17; % scale factor

%x_new = round(j/scale); % new height based on original image height scaled with scale factor
%y_new = round(k/scale); % new width based on original image width scaled with scale factor

x_new = floor(j/scale); 
y_new = floor(k/scale); 

M = zeros(x_new,y_new,c); % initialize black image with the new height and width

for ch = 1:c % loop through every channel (R, G, B)
 for count1 = 1:x_new % loop through every col 
  for count2 = 1:y_new % loop through every row
    M(count1,count2,ch) = I(count1*scale,count2*scale,ch); % assign to every pixel of the black image a new value based on origial image pixel and scale factor 
  end
 end
end

subplot(1,2,1); imagesc(uint8(I)); axis tight; % plot origial image 
subplot(1,2,2); imagesc(uint8(M)); axis tight; % plot scaled image 