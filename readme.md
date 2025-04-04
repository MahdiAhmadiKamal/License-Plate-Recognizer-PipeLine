# License Plate Recognizer PipeLine 🔎🚘🚔🚖🚍

<img src="pics\1.jpg" width="600">

This repository is a supplement to my previous repository, [Persian-License-Plate-Recognition](https://github.com/MahdiAhmadiKamal/Persian-License-Plate-Recognition). In this repository, the process of recognizing license plates is got streamlined thanks to the pipeline. By giving the picture to the code, the text of the license plates in the picture will be directly recognized. This project is prepared with the aid of [deep-text-recognition-benchmark](https://github.com/clovaai/deep-text-recognition-benchmark) repository. This repository consists of two parts: **identification** and **verification**.

<img src="pics\2.jpg" width="500">

A [pretrained model](https://drive.google.com/drive/folders/15WPsuPJDCzhp2SvYZLRj8mAlT3zmoAMW) is selected and fine-tuned on a Persian license plates dataset called [IR-LPR](https://github.com/mut-deep/IR-LPR?tab=readme-ov-file). The data are labeled according to the following table.

<img src="pics\img5.png" width="800">


## How to install
Run this command:
```
pip install -r requirements.txt
```

## Identification
This section is related to recognizing and identifying the persian license plates directly from street images.

### How to run
+ Download the pre-trained weight for detection from the link below and put it in weights/yolov8-detector:
https://drive.google.com/file/d/1kKyQ6CnybU99A6zUVKAYweI-mx9o-GmH/view?usp=sharing

+ Download the pre-trained weight for recognition from the link below and put it in weights/dtrb-recognizer:
https://drive.google.com/file/d/1P-Biv-3iJ427swEFBl_i_zE2igyXrEpQ/view?usp=sharing

+ Place your input images in io/input.

+ Run this command:
```
python identification.py --input_image PATH/TO/YOUR_IMAGE.JPG
```
Also you can change the threshold using `--threshold` argument.

### Results

<img src="pics\image_result.jpg" width="600">

Output
<table>
  <tr>
    <td>Input image</td>
    <td><img src="pics\plate_image_result_1.jpg" width="150"></td>
    <td><img src="pics\plate_image_result_0.jpg" width="150"></td>
    <td><img src="pics\plate_image_result_2.jpg" width="150"></td>
  </tr>
  <tr>
    <td>Predicted label</td>
    <td>49i58332 (i=ی)</td>
    <td>78r48774 (r=ط)</td>
    <td>82v51842 (v=و)</td>
  </tr>
   <td>Confidence score</td>
    <td>0.9984</td>
    <td>0.3281</td>
    <td>0.9965</td>
  </tr>
</table>

## Verification
This section is related to recognizing and verifying the persian license plates. After being recognized, the license plate text is compared with those stored in the database. If the license plate is verified, the code sends the appropriate message to open the barrier.

<img src="pics\3.png" width="600">

### How to run
+ Similar to the previous section download the pre-trained weights.
+ Store the license plates in the database file according to the aforementioned table.
+ Place your input images in io/input.

+ Run this command:
```
python verification.py --input_image PATH/TO/YOUR_IMAGE.JPG
```
You can change the threshold using `--threshold` argument.