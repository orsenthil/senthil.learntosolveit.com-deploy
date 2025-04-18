import os

# Define the directory where your posts are located
directory = 'posts'

# Walk through the directory
for root, _, files in os.walk(directory):
    for file in files:
        if file.endswith('.wpcomment'):
            # Construct the full path to the .wpcomment file
            wpcomment_path = os.path.join(root, file)

            # Extract the base file name without the .NUMBER.wpcomment part
            base_file_name = file.rsplit('.', 2)[0]
            # Construct the corresponding .md file path
            md_file_name = base_file_name + '.md'
            md_path = os.path.join(root, md_file_name)

            # Check if the corresponding .md file exists
            if os.path.exists(md_path):
                comments = ["comments:\n\n"]
                author = "Anonymous"  # Default author if not specified

                # Read the contents of the .wpcomment file
                with open(wpcomment_path, 'r') as wpcomment_file:
                    for line in wpcomment_file:
                        if line.startswith('.. author:'):
                            author = line.split(':', 1)[1].strip()
                        elif not line.startswith('..'):
                            comments.append(f"{line.strip()}\n\n")
                    comments.append(f"_{author}_\n\n---\n")
                with open(md_path, 'a') as md_file:
                    md_file.write('\n\n')  # Add some spacing
                    md_file.write(''.join(comments).rstrip('\n---\n'))  # Remove the last horizontal line

                # Delete the .wpcomment file
                os.remove(wpcomment_path)

                print(f"Appended comments from {wpcomment_path} to {md_path} and deleted the .wpcomment file.")
            else:
                print(f"Corresponding .md file for {wpcomment_path} not found.")
