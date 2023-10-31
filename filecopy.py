def copy_and_convert(input_file,output_file):
    try:
        with open(input_file,'r') as source_file:
            content= source_file.read()
        # content=content.upper()
        with open (output_file,'w') as destination_file:
            destination_file.write(content)
        print(f"File '{input_file}' copied and converted to '{output_file}' successfully.")    

    except Exception as e :
        print(f"Error ha bhai sorry{str(e)}")

input_file="toy.txt"
output_file="paradox.txt"

copy_and_convert(input_file,output_file)