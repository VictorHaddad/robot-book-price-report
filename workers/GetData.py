from bs4 import BeautifulSoup
import pandas as pd
import requests
 

def scrape_books(base_url):
  try:
    books_data = []
    page = 1

    while True:
      url = f"{base_url}/catalogue/page-{page}.html"
      response = requests.get(url)
      
      if response.status_code != 200:
        break

      soup = BeautifulSoup(response.content, 'html.parser')
      books = soup.find_all('article', class_='product_pod')
      
      for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text.strip().replace('£', '')
        availability = book.find('p', class_='instock availability').text.strip()
        
        books_data.append({
          'Title': title,
          'Price': float(price),
          'Availability': availability
        })
      
      page += 1
  except Exception as e:
    return {
      'error': True,
      'message': f'Message: {e}',
      'data': None,
    }
    
  return {
    'error': False,
    'message': None,
    'data': books_data,
  }

if __name__ == "__main__":
  books_data = scrape_books("https://books.toscrape.com")
  df = pd.DataFrame(books_data['data'])

  output_file = r"C:\Users\vghaddad\Desktop\robot-book-price-report\docs\books_data.csv"
  
  df.to_csv(output_file, index=False)