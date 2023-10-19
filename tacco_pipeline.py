import argparse
 
import sys
    
import os
try:
    import scanpy as sc
except:
    os.system("pip install scanpy")
    import scanpy as sc

try:
    import tacco as tc
except:
    os.system("pip install tacco")
    import tacco as tc
    
try:
    import pandas as pd
except:
    os.system("pip install pandas")
    import pandas as pd



if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage="it's usage tip.", description="help info.")
    parser.add_argument("--output_h5ad_file", type=str, default=None, help="the output file with h5ad format.")
    parser.add_argument("--output_csv_file", type=str, default=None, help="the output file with csv format.")
    parser.add_argument("--input_spatial_file_type", type=str, default="h5ad", required=True, help="the input file format.")

    parser.add_argument("--input_spatial_h5ad_file", type=str, default="./spatial_h5ad_file.h5ad", help="the spatial input data file with h5ad format.")
    parser.add_argument("--input_reference_h5ad_file", type=str, required=True, help="the reference input data file with h5ad format.")
    parser.add_argument("--input_reference_annotation_id", type=str, default="cell_id", help="the reference input data file with h5ad format.")
    
    parser.add_argument("--input_visium_folder", type=str, default="./visium_file/", help="the input visium folder which must include visium count file.")
    parser.add_argument("--input_visium_count_file_name", type=str, default="raw_feature_bc_matrix.h5", help="the input visium count file name which is included in the visium folder.")
    
    parser.add_argument("--input_csv_count_file", type=str, default="./csv_count_file.csv", help="the input spatial expression count file in csv format, in which columns name is gene name, and row name is spot name.")
    parser.add_argument("--input_csv_matadata_file", type=str, default=None, help="the input spatial metadata.")
    
    args = parser.parse_args()
    

    reference_path = args.input_reference_h5ad_file#"/users/PCON0022/jiangyi/test_data_file/reference.h5ad"
    reference_annotation_id = args.input_reference_annotation_id
    reference_data = sc.read_h5ad(reference_path)

    
    if args.input_spatial_file_type=="h5ad":
        annotate_data = sc.read_h5ad(args.input_spatial_h5ad_file)
    elif args.input_spatial_file_type=="visium":
        annotate_data = sc.read_visium(args.input_visium_folder, count_file=args.input_visium_count_file_name)
    elif args.input_spatial_file_type=="csv":
        annotate_data = sc.read_csv(args.input_csv_count_file)
        if args.input_csv_matadata_file is not None:
            try:
                annotate_data.obs = pd.read_csv(args.input_csv_matadata_file, index_col=0)
            except:
                print("please input matched metadata for spatial data")
    else:
        print(f"Your inputted spatial_file_type: {args.input_spatial_file_type} is out of h5ad, visium, and csv")
        sys.exit()
        
    if args.output_h5ad_file is None and args.output_csv_file is None:
        print("please provide at lease one type of output file")
        sys.exit()


    reference_data.var_names_make_unique()
    annotate_data.var_names_make_unique()
    annotate_data.raw = annotate_data
    annotated_result = tc.tl.annotate(annotate_data, reference_data, annotation_key=reference_annotation_id, result_key='tacco_annotation')
    if args.output_h5ad_file is not None:
        annotated_result.write_h5ad(args.output_h5ad_file)
    if args.output_csv_file is not None:    
        annotated_result.obsm["tacco_annotation"].to_csv(args.output_csv_file)
    
    
    
    