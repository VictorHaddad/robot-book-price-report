from reportlab.lib.pagesizes import letter
from database.MongoDB import MongoDB
from reportlab.pdfgen import canvas
import pandas as pd

mongodb = MongoDB("robot-book-price-report") 

def generate_pdf_with_reportlab(expensive_books, available_books, summary):
    try:
        output_path = r'C:\Users\vghaddad\Desktop\robot\docs\books_report.pdf'
        
        c = canvas.Canvas(output_path, pagesize=letter)
        width, height = letter
        y_position = height - 130

        def draw_title_and_summary():
            c.setFont("Helvetica-Bold", 16)
            c.drawString(200, height - 50, "Relatório de livros")
            c.setFont("Helvetica", 12)

            c.drawString(100, height - 70, f"Preço médio: ${summary['avg_price']:.2f}")
            c.drawString(100, height - 85, f"Total de livros: {summary['total_books']}")
            c.drawString(100, height - 100, f"Livros disponíveis: {summary['available_books_count']}")

        draw_title_and_summary()
        
        c.setFont("Helvetica-Bold", 14)
        c.drawString(200, y_position, "Livros acima de $20")
        c.setFont("Helvetica", 12)
        y_position -= 15
        
        def draw_wrapped_text(x, y, text, max_width):
            
            c.setFont("Helvetica", 12)
            lines = []
            line = ''
            for word in text.split():
                if c.stringWidth(line + ' ' + word) < max_width:
                    line += ' ' + word
                else:
                    lines.append(line)
                    line = word
            lines.append(line)  

            for line in lines:
                c.drawString(x, y, line)
                y -= 15  
            return y 

        for _, row in expensive_books.iterrows():
            if y_position < 50: 
                c.showPage()  
                y_position = height - 130  

            title = row['Title']
            price = f"${row['Price']:.2f}"
           
            y_position = draw_wrapped_text(100, y_position, f"Nome: {title}", width - 200)
            y_position = draw_wrapped_text(100, y_position, f"Valor: {price}", width - 200)
            y_position -= 20

        c.save()
        
    except Exception as e:
        mongodb.create({'event': 'Erro ao realizar download', 'error': True})
        return {
            'error': True,
            'message': f'Message: {e}',
            'data': None,
        }
        
    return {
        'error': False,
        'message': 'PDF gerado com sucesso',
        'data': None,
    }


def manipulate_data(data):
    try:
        df = pd.read_csv(data)
        print(df.columns)
        
        expensive_books = df[df['Price'] > 20]
        
        summary = {
            'avg_price': df['Price'].mean(),
            'total_books': len(df),
            'available_books_count': df[df['Availability'] == "In stock"].shape[0]
        }
        
        return expensive_books, df[df['Availability'] == "In stock"], summary
    
    except Exception as e:
        mongodb.create({'event': 'Erro ao realizar download', 'error': True})
        return {
            'error': True,
            'message': f'Message: {e}',
            'data': None,
        }

if __name__ == "__main__":
  data = r'C:\Users\vghaddad\Desktop\robot\docs\books_data.csv'
  expensive, available, summary = manipulate_data(data)
  generate_pdf_with_reportlab(expensive, available, summary)