import os
import re
from bs4 import BeautifulSoup
import glob
import textwrap

def get_book_title_from_url(url):
    """Extract book title from Goodreads URL."""
    book_id = url.split('/')[-1]
    if '.' in book_id:
        title = book_id.split('.')[-1]
    else:
        title = book_id
    return title.replace('-', ' ').replace('_', ' ').title()

def get_book_title_from_page_title(content):
    """Extract book title from page title."""
    title_match = re.search(r'\.\. title: Book Review[:\-]\s*(.*)', content)
    if title_match:
        title = title_match.group(1)
        # Remove author name if present
        if ' By ' in title:
            title = title.split(' By ')[0]
        return title.strip()
    return None

def format_paragraphs(text, width=80):
    """Format text into paragraphs with proper line wrapping."""
    # Split text into paragraphs
    paragraphs = re.split(r'\n\s*\n', text)
    
    # Process each paragraph
    formatted_paragraphs = []
    for para in paragraphs:
        # Clean up the paragraph
        para = para.strip()
        if not para:
            continue
            
        # Split into sentences for better wrapping
        sentences = re.split(r'(?<=[.!?])\s+', para)
        
        # Format each sentence
        formatted_sentences = []
        for sentence in sentences:
            # Wrap the sentence
            wrapped = textwrap.fill(
                sentence,
                width=width,
                break_long_words=False,
                break_on_hyphens=False
            )
            formatted_sentences.append(wrapped)
        
        # Join sentences with proper spacing
        formatted_para = '\n'.join(formatted_sentences)
        formatted_paragraphs.append(formatted_para)
    
    # Join paragraphs with double newlines
    return '\n\n'.join(formatted_paragraphs)

def clean_text(text):
    """Clean and format the text properly."""
    # Fix common spacing issues
    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)  # Add space between camelCase
    text = re.sub(r'([a-z])([0-9])', r'\1 \2', text)  # Add space between letter and number
    text = re.sub(r'([0-9])([a-zA-Z])', r'\1 \2', text)  # Add space between number and letter
    
    # Fix common word joining issues
    text = text.replace('categoriesuch', 'categories such')
    text = text.replace('scientiststood', 'scientists stood')
    text = text.replace('thearliest', 'the earliest')
    text = text.replace('theirespectiveras', 'their respective eras')
    text = text.replace('werentertaining', 'were entertaining')
    text = text.replace('theethicallapse', 'the ethical lapse')
    text = text.replace('isupposed', 'is supposed')
    text = text.replace('abouthis', 'about this')
    text = text.replace('Valis', 'Vali is')
    text = text.replace('withis', 'with this')
    text = text.replace('Ramarexplained', 'Rama are explained')
    text = text.replace('buthe', 'but the')
    text = text.replace('abouthethicalapse', 'about the ethical lapse')
    text = text.replace('script,instead', 'script, instead')
    text = text.replace('know,but', 'know, but')
    text = text.replace('neways', 'new ways')
    text = text.replace('thathe', 'that the')
    text = text.replace('thathere', 'that there')
    text = text.replace('Inonlinearity', 'In nonlinearity')
    text = text.replace('Choas', 'Chaos')
    
    # Fix punctuation spacing
    text = re.sub(r'\s+([.,!?;:])', r'\1', text)  # Remove space before punctuation
    text = re.sub(r'([.,!?;:])([^\s\d])', r'\1 \2', text)  # Add space after punctuation
    
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with single space
    text = text.strip()
    
    # Format into paragraphs
    text = format_paragraphs(text)
    
    return text

def convert_goodreads_to_rst(content):
    # Find the raw HTML section
    raw_html_match = re.search(r'\.\. raw:: html\n\n(.*?)(?=\n\n|\Z)', content, re.DOTALL)
    if not raw_html_match:
        return content

    html_content = raw_html_match.group(1)
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract book information
    book_link = soup.find('a', href=lambda x: x and 'goodreads.com/book/show' in x)
    if not book_link:
        return content

    # Get book title from the URL and page title
    book_url = book_link['href']
    book_title = get_book_title_from_page_title(content)
    if not book_title:
        book_title = get_book_title_from_url(book_url)
    
    # Get cover image if available
    cover_img = soup.find('img')
    cover_img_html = ""
    if cover_img and 'src' in cover_img.attrs:
        cover_img_html = f""".. image:: {cover_img['src']}
   :alt: {book_title}
   :target: {book_url}
   :align: left
   :width: 98px

"""

    # Get author if available
    author_link = soup.find('a', href=lambda x: x and 'goodreads.com/author/show' in x)
    author_html = ""
    if author_link:
        author_html = f"by `{author_link.text.strip()} <{author_link['href']}>`_"

    # Get rating if available
    rating_link = soup.find('a', href=lambda x: x and 'goodreads.com/review/show' in x)
    rating_html = ""
    if rating_link:
        rating_text = rating_link.text.strip()
        rating_html = f"My rating: {rating_text}"
    
    # Get the review text (everything after the rating)
    review_text = ""
    if rating_link:
        # Get all text nodes after the rating link
        next_elements = rating_link.find_all_next(text=True)
        review_parts = []
        for text in next_elements:
            text = text.strip()
            if text and text not in ['br', '/br']:
                review_parts.append(text)
        review_text = ' '.join(review_parts).strip()
        
        # Remove duplicate rating text if present at the start
        if rating_text and review_text.startswith(rating_text):
            review_text = review_text[len(rating_text):].strip()
        
        # Clean up the review text
        review_text = clean_text(review_text)

    # Create RST format with proper structure and spacing
    rst_content = f"""{cover_img_html}
`{book_title} <{book_url}>`_ {author_html}

{rating_html}

{review_text}

"""

    # Replace the raw HTML section with the new RST content
    new_content = content.replace(raw_html_match.group(0), rst_content)
    return new_content

def main():
    # Find all RST files in the posts directory
    rst_files = glob.glob('posts/**/*.rst', recursive=True)
    
    # Counter for processed files
    processed_count = 0
    error_count = 0
    
    for file_path in rst_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Only process files that contain Goodreads HTML content
            if ('.. raw:: html' in content and 
                ('goodreads.com/book/show' in content or 
                 'goodreads.com/author/show' in content or
                 'gr-assets.com/images' in content)):
                
                new_content = convert_goodreads_to_rst(content)
                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    processed_count += 1
                    print(f"Processed {file_path}")
        except Exception as e:
            print(f"Error processing {file_path}: {str(e)}")
            error_count += 1
    
    print(f"\nProcessing complete!")
    print(f"Successfully processed: {processed_count} files")
    print(f"Errors encountered: {error_count} files")

if __name__ == '__main__':
    main() 