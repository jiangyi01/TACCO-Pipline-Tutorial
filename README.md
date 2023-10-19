# TACCO Pipline Tutorial

* There are some files needed for spatial data and reference data separatly.
* For reference data, you can only use h5ad format, and the label like "cell_id" should be put into obs domain of your h5ad data
* For spatial data, there are three types of data formats you can use (only one type you need input, and provide data type label in the command, h5ad, csv, visium):

  * h5ad format
  * csv format.

    * csv file of gene expression data, in which columns name must be gene name and row name must be spot name or index
    * csv file of metadata, in which row name must be same with gene expression data
  * visium h5 format(one file is needed, whose folder path and name are needed to input)


---

***For the correct running process, please make sure that your inputted expression data are raw counts without negative values.***

---


### Command for spatial h5ad format input

```
python tacco_pipeline.py \
    --input_spatial_file_type h5ad \
    --input_spatial_h5ad_file ./example_spatial.h5ad \
    --input_reference_h5ad_file ./example_reference.h5ad \ 
    --input_reference_annotation_id cell_id \
    --output_h5ad_file ./annotated_result.h5ad \
    --output_csv_file ./annotated_result.csv
  

```

### Command for spatial csv format input

```
python tacco_pipeline.py \
    --input_spatial_file_type csv \
    --input_csv_count_file ./example_spatial.csv \
    --input_reference_h5ad_file ./example_reference.h5ad \ 
    --input_reference_annotation_id cell_id \
    --output_h5ad_file ./annotated_result.h5ad \
    --output_csv_file ./annotated_result.csv
```

### Command for spatial visium h5 format input

```
python tacco_pipeline.py \
    --input_spatial_file_type visium \
    --input_visium_folder ./visium_data/ \
    --input_visium_count_file_name raw_feature_bc_matrix.h5 \
    --input_reference_h5ad_file ./example_reference.h5ad \ 
    --input_reference_annotation_id cell_id \
    --output_h5ad_file ./annotated_result.h5ad \
    --output_csv_file ./annotated_result.csv
```
