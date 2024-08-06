from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import tldextract

app = Flask(__name__)

@app.errorhandler(400)
def bad_request_error(error):
    return render_template('error.html', error_code=400, error_message="Bad Request"), 400

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('error.html', error_code=500, error_message="Internal Server Error"), 500

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form.get('url')
    
    if not url:
        return render_template('error.html', error_code=400, error_message="URL is required"), 400
    
    try:
        response = requests.get(url)
        response.raise_for_status()


        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract information
        title = soup.title.string if soup.title else 'No title found'
        description = soup.find('meta', attrs={'name': 'description'})
        description = description['content'] if description else 'No description found'
        
        # Extracting all headings
        headings = {f'h{level}': [h.get_text(strip=True) for h in soup.find_all(f'h{level}')] for level in range(1, 7)}
        
        # Extracting all hyperlinks
        links = [{'href': link.get('href'), 'text': link.get_text(strip=True)} for link in soup.find_all('a')]
        urli = get_base_domain(url)
        # Render template with scraped data
        return render_template('result.html', title=title, description=description, headings=headings, links=links, url=url,urli=urli)
        
    except requests.exceptions.RequestException as e:
        return render_template('error.html', error_code=500, error_message=str(e)), 500


def get_base_domain(url):
    # Extract the components of the URL
    extracted = tldextract.extract(url)
    
    # Combine the domain and the suffix (TLD)
    domain = f"{extracted.domain}.{extracted.suffix}"
    
    # Prepend 'www.' if not present
    return f"www.{domain}"

if __name__ == '__main__':
    app.run(debug=True)
