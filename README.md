# HandMask_AutoLabel
A HandMask Autolabel Tool.


![plot](vis/image.gif)

## Annotation 
[Hand_mask.json](annotations/sample.json)
### Info
| Item         | Value                    | Data_Type |
|--------------|--------------------------|-----------|
| description  | "CRI 2023 Hand Datasets" | str       |
| version      | "1.0.0"                  | str       |
| date         | "2023-01-30"             | str       |
| organization | "Coretronic_CRI"         | str       |
***
### images
| Item          | Value                                                                    | Data_Type |
|---------------|--------------------------------------------------------------------------|-----------|
| image_path    | "./images/person/Gid/fid.png"                                            | str       |
| id            | 123                                                                      | int       |
 | frame_id      | 123                                                                      | int       |
| camera        | id (Camera category)<br/> retify (bool)<br/>width (int)<br/>height (int) |        |
***
### Mask
| Item      | Value                       | Data_Type |
|-----------|-----------------------------|-----------|
| mask_path | "./mask/person/Gid/fid.png" | str       |
| id        | 123                         | int       |
| frame_id  | 123                         | int       |
***
### camera
| Item       | Value                                                                                   | Data_Type |
|------------|-----------------------------------------------------------------------------------------|-----------|
| id         | 0:fisheye<br/>1:pinhole<br/> ...                                                        | int       |
| device     | "fisheye"<br/>"RealSense L515"<br/>...                                                  | str       |
| intrinsic  | 278.08321774513394, 279.113841127447, 309.19580091877737, 207.67952497223772, 0.0       | float     |
| distortion | -0.020306250909190218, 0.056496479357930875, -0.06768354885591037, 0.036626224288176815 | float     |
***
### annotations
| Item                   | Value                      | Data_Type |
|------------------------|----------------------------|-----------|
| id                     | 123                        | int       |
| image_id               | 123                        | int       |
| mask_id                | 123                        | int       |
| frame_id               | 1                          | int       |
| left_hand_accessories  | False                      | bool      |
| right_hand_accessories | False                      | bool      |
| left_arm_accessories   | False                      | bool      |
| right_arm_accessories  | False                      | bool      |
| mask_object            | category_id<br/>gesture_id |           |

***
### categories
| Category   | ID  | Intensity |
|------------|-----|-----------|
| background | 0   | 0         |
| Left_Hand  | 1   | 1         |
| Left_arm   | 2   | 2         |
| Right_hand | 3   | 3         |
| Right_arm  | 4   | 4         |
***
### Gesture_Categories (to be edited??????)
| Category | ID  | 
|----------|-----|
| ???        | 0   |
| ???        | 1   |
| ???        | 2   |
| ???        | 3   |
| ???        | 4   |
| ???        | 5   |
| ya       | 6   |
| ??????       | 7   |
| ??????       | 8   |
| ?????????      | 9   |
| ??????       | 10  |
| ??????       | 11  |
| ok       | 12  |
| pinch    | 13  |

***
### Position_Categories
| Category      | ID     | 
|---------------|--------|
| left_up       | 0      | 
| middle_up     | 1      | 
| right_up      | 2      | 
| middle_left   | 3      | 
| middle        | 5      | 
| middle_right  | 6      | 
| down_left     | 7      | 
| down_middle   | 8      | 
| down_right    | 8      | 
***
#### stop the build if there are Python syntax errors or undefined names
>flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
#### exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
>flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
***

# Docker
> $ sudo docker build -t [image_name]:[tag_name] . \
> ?????????
> * [image_name] ?????????????????????????????????????????????
> * [tag_name] ??????????????????????????????????????????
> * [ . ] ???????????????????????????????????????????????????????????? 

> $ sudo docker run [OPTIONS] IMAGE [COMMAND] [ARG...]\
>?????????
> * OPTIONS ??????????????? -p ??????????????????????????????????????????
> * IMAGE ??? Docker ??????????????????
> * COMMAND ????????????????????????????????????
> * ARG ?????????????????????
> 
> ???????????????????????????????????? my_image ????????????????????????????????????????????????\
> $ docker run -it my_image /bin/bash

### ??????????????????
> $ sudo docker build -t autohand:v1 .\
> $ sudo docker run autohand:v1


>?????????????????????????????????????????????????????????????????????????????????????????????????????? Docker ????????????????????? Docker Hub???
> * ????????????????????? Docker Hub 
> 
>???????????????????????????????????????????????????????????????????????????????????????????????????
> * $ docker tag <image_id> <your_dockerhub_username>/<image_name>:tag \
>
> ?????? Docker Hub???
> * $ docker login
>
> ?????????????????? Docker Hub???
> * docker push <your_dockerhub_username>/<image_name>:tag \
>
> ????????????????????? Docker Hub ??????????????????????????????????????????
> * docker pull <your_dockerhub_username>/<image_name>:<tag>




>???????????? GitHub ??????????????????????????????????????? commit?????????????????????????????????????????????
> * ??? GitHub ????????????????????????????????????????????????????????????????????????????????? 
> * ???????????????????????????????????????????????????????????????????????????????????????????????? commit??? 
> * ??????????????????????????????????????????????????????????????? 
> * ??????????????????????????????????????????????????????????????????????????? 
> * ?????????????????????????????????????????????????????????????????????????????????????????????????????????
>
> ???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????


pip list --format=freeze > requirements.txt