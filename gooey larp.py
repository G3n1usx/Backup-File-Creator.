from gooey import Gooey, GooeyParser

# 1. Add the @Gooey decorator right above your main function
@Gooey(program_name="My Backup Utility")
def main():
    # 2. Define your inputs using GooeyParser
    parser = GooeyParser(description="Easily back up your files")
    
    # Gooey automatically converts widget="FileChooser" into a browse button!
    parser.add_argument('input_file', help="Select the file to back up", widget="FileChooser")
    parser.add_argument('output_file', help="Where to save the backup", widget="FileSaver")
    
    # 3. Parse the arguments
    args = parser.parse_args()
    
    # 4. Use args.argument_name to run your original code
    with open(args.input_file, 'r') as f:
        data = f.read()

    with open(args.output_file, 'w') as f:
        f.write(data)

    print("Backup complete!")

if __name__ == '__main__':
    main()
