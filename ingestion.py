import json

input_file = "/Users/allakkihome/Documents/yelp_reviews/yelp_academic_dataset_review.json"
output_prefix = "split_file"
num_files = 25

#count total lines (objects) in the file
with open(input_file, "r", encoding= "utf8") as f:
    total_lines = sum(1 for line in f)

lines_per_file = total_lines // num_files

print(f"Total lines in file: {total_lines}")
print(f"Lines per file: {lines_per_file}")

#now split the file
with open(input_file, "r",encoding= "utf8") as f:
    for i in range(num_files):
        output_filename = f"{output_prefix}{i+1}.json"

        with open(output_filename,"w",encoding= "utf8") as out_file:
            for j in range(lines_per_file):
                line = f.readline()
                if not line:
                    break
                out_file.write(line)
print(" JSON file split completed")
            

