#!/bin/bash
# Usage: ./merge_meta.sh /path/to/target_directory
TARGET_DIR=${1:-.}

# Use find to locate all .meta files within the TARGET_DIR
find "$TARGET_DIR" -type f -name "*.meta" | while read -r meta_file; do
  # Derive the corresponding .md file name by replacing the .meta extension with .md
  md_file="${meta_file%.meta}.md"

  # Check if the markdown file exists
  if [ -f "$md_file" ]; then
    echo "Processing $md_file (merging in metadata from $meta_file)..."
    # Concatenate the meta file, add an empty line, and then the markdown file into a temporary file,
    # then replace the original .md file with it.
    {
      cat "$meta_file"
      echo ""
      cat "$md_file"
    } >"$md_file.tmp" && mv "$md_file.tmp" "$md_file"
    # Remove the meta file
    rm "$meta_file"
  else
    echo "No corresponding .md file for $meta_file."
  fi
done
