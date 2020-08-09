## Description

The repository contains the code to solve the id switches of tracks labelled using Intel's CVAT tool.

## Configuration
| Configuration Option | Description  | Possible Values |
| ------------- | ------------- | ------------- |
| **[data]**  | Section Name, this contains the path to input and output xml files. | |
| input_cvat_xml_path = data/annotations.xml  | Path to input cvat xml file | string |
| output_cvat_xml_path = data/annotations_corrected.xml  | Path to output cvat xml file | string |
|  |  |
| **[swap_labels]**  | Section Name, this contains the information of id-switches to be resolved. | |
| track_ids_list = 0,1:1,0  | List of track ids to swap. The pairs of track ids should be separated by colon (:). In each pair, track ids should be separated by comma (,). | string |
| frame_no_list = 40:40  | The list of frame numbers after which the corresponding track ids should be swapped. The frame numbers should be separated by colon (:) for each corresponding pair of track ids.| string |

## Requirements

The code is tested using Python 3.7. No other external library is required to run this project.

## Run
1. Update the configurations `config.ini` as per your requirements.
2. From the main directory, run the following command
```
# python __main__.py
```

## Contribution
Pull requests optimizing the implementation or increasing the scope of the projects are welcome.

## Note
If you are having difficulty in running or understanding the code, please create an issue on this repository.